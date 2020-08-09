import json
import os
import pymysql

import sys
sys.path.insert(1, os.path.join('..','credentials'))
from google_mysql_connection import GoogleMySQLConnection

from tools.data_stage import DataStage

# Load credentials
credentials_path = os.path.join('..','credentials','connect_credentials.json')

# Open connection
db_connection = GoogleMySQLConnection(credentials_path)

# Read data from CSVs
stage = DataStage(db_connection.connection)
if stage.sorted_csv_list:
    for file in stage.sorted_csv_list:
        stage.process_file(file)
        stage.archive_file(file)
    db_connection.connection.commit()
else:
    print('\nNenhum arquivo encontrado para upload\n')

# Finalize connection
db_connection.finish()

print('\n\n***** Script terminado sem erros *****\n\n')
