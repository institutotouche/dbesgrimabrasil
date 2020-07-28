import json
import os, subprocess
import pymysql


# Load credentials
credentials_path = os.path.join('..','credentials','connect_credentials.json')
with open(credentials_path) as f:
    credentials = json.load(f)

# Start proxy
proxy_path = os.path.join('..','credentials','cloud_sql_proxy.exe')
instances_string = '-instances=memoriadaesgrimabrasileira:us-central1:memoriadaesgrimabrasileira=tcp:' + \
                    str(credentials.get('port',3306))
proxy_credentials_string = '-credential_file=' + os.path.join('..','credentials','proxy_credentials.json')
proxy_subprocess = subprocess.Popen([proxy_path, instances_string, proxy_credentials_string])

if proxy_subprocess and not proxy_subprocess.poll():
    print('\n\nProxy do Google aberto na porta', credentials.get('port',3306))
    print('Subprocess ID: ', proxy_subprocess.pid, '\n\n')

# Instantiate connection
# connection = pymysql.connect(host=credentials.get('host','localhost'),
#                              port=credentials.get('port',3306),
#                              user=credentials.get('user','user'),
#                              password=credentials.get('password','password'),
#                              db=credentials.get('db','db'))

# Find rows already in db


# Split new data into inserts and updates


# Update old rows with new data

# Insert completely new rows


# commit
# connection.commit()
# connection.close()

# close proxy
while not proxy_subprocess.poll():
    proxy_subprocess.terminate()
print('\nProxy do Google terminado.')

print('\n\n\n\n')
