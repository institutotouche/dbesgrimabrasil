import json
import os
import pymysql

from tools.google_proxy import GoogleProxy

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

# Just testing
cursor = connection.cursor()
query = 'SELECT * FROM StatusCombates'
cursor.execute(query)
data = cursor.fetchall()
print(data)


# Read data from CSVs

# Find rows already in db

# Split new data into inserts and updates


# Update old rows with new data

# Insert completely new rows


# Finalize connection
# connection.commit()
connection.close()

# close proxy
proxy.close()

print('\n\n***** Script terminado sem erros *****\n\n')
