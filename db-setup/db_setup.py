import json
import os
import pymysql

import sys
sys.path.insert(1, os.path.join('..','credentials'))
from google_proxy import GoogleProxy

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
