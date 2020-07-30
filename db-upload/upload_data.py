import json
import os
import pymysql

from tools.google_proxy import GoogleProxy
from tools.data_stage import DataStage

# Load credentials
credentials_path = os.path.join('..','credentials','connect_credentials.json')
with open(credentials_path) as f:
    credentials = json.load(f)

# Start proxy
proxy = GoogleProxy(credentials)
proxy.open()

# Instantiate connection
connection = pymysql.connect(host=credentials.get('host','localhost'),
                             port=credentials.get('port',3306),
                             user=credentials.get('user','user'),
                             password=credentials.get('password','password'),
                             db=credentials.get('db','db'))

# Read data from CSVs
stage = DataStage()
if stage.sorted_file_list:
    for file in stage.sorted_file_list:
        query, args = stage.process_file(connection, file)
        # cursor.executemany(query, args)
        # connection.commit()
else:
    print('\nNenhum arquivo encontrado para upload\n')

# Finalize connection
while connection.open:
    connection.close()
print('Conexão com o banco de dados finalizada.')

# close proxy
proxy.close()

print('\n\n***** Script terminado sem erros *****\n\n')
