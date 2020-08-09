import json
import os
import pymysql

import sys
sys.path.insert(1, os.path.join('..','credentials'))
from google_proxy import GoogleProxy

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
stage = DataStage(connection)
if stage.sorted_csv_list:
    for file in stage.sorted_csv_list:
        stage.process_file(file)
        stage.archive_file(file)
    connection.commit()
else:
    print('\nNenhum arquivo encontrado para upload\n')

# Finalize connection
while connection.open:
    connection.close()
print('Conexão com o banco de dados finalizada.')

# close proxy
proxy.close()

print('\n\n***** Script terminado sem erros *****\n\n')
