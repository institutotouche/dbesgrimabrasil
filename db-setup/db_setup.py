import json
import os
import pymysql

import sys
sys.path.insert(1, os.path.join('..','credentials'))
from google_mysql_connection import GoogleMySQLConnection


def main():

    # Load paths
    credentials_path = os.path.join('..','credentials','connect_credentials.json')
    queries_path = os.path.join('.', 'queries')

    # Open connection
    db_connection = GoogleMySQLConnection(credentials_path)

    process_queries('create', queries_path, db_connection.connection)
    process_queries('insert', queries_path, db_connection.connection)

    # Finalize connection
    db_connection.finish()

    print('\n\n***** Script terminado sem erros *****\n\n')


def process_queries(query_key, queries_path, connection):

    query_list = [os.path.join(queries_path, file)
                    for file in os.listdir(queries_path)
                    if file[:6].lower()==query_key]

    for file_path in query_list:
        print('Processando arquivo', file_path)
        query = read_query(file_path)
        print('Query:\n', query, '\n')
        with connection.cursor() as cursor:
            cursor.execute(query)

    connection.commit()


def read_query(file_path):
    with open(file_path, 'r') as f:
        query = f.read()
    return query


if __name__ == '__main__':
    main()
