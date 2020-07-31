import csv, json
import os

class DataStage(object):
    def __init__(self, db_connection, pending_dir='upload-pending'):
        self.db_connection = db_connection
        self.pending_path = os.path.join('.',pending_dir)
        csv_list = self._get_CSV_list()
        self.sorted_csv_list = self._prioritize(csv_list)
        # TODO move base queries to a json fixture
        self.base_queries={
            'select_all': 'SELECT * FROM :%(table)s',
            'insert': '',
            'update': ''
        }

    def process_file(self, file_name):
        table_name = file_name[:-4]
        raw_data_list = self._read_data(os.path.join(self.pending_path, file_name))
        fields, values = self._clean_headers(raw_data_list)

        update_values, insert_values = self._make_updates(fields, values, table_name)
        # TODO make inserts
        # self.db_connection.execute(insert_query, [fields, insert_values])

        # TODO think about meaningful return
        return 0, 0 # returns list of (query, args) tuples

    def _get_CSV_list(self):
        # Renames CSV files to lower case and return list with new names
        for file in os.listdir(self.pending_path):
            if file[-4:]=='.csv':
                os.rename(os.path.join(self.pending_path,file),
                        os.path.join(self.pending_path,file.lower()) )
        return [file for file in os.listdir(self.pending_path)
                if file[-4:]=='.csv']

    def _prioritize(self, file_list):
        # Sorts a list of files in priority order
        priority_list = self._load_priority_list()
        return [file for file in priority_list if file in file_list]

    def _load_priority_list(self):
        # Loads the list of tables in priority order
        with open(os.path.join('.','fixtures','table_priority_order.txt'), "r") as priority_file:
            priority_list = json.load(priority_file)
        return [f.lower()+'.csv' for f in priority_list] # return everything in lower case

    def _read_data(self, file_path):
        # Reads data from a file, without any processing
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data_list = [tuple(row) for row in reader]
        return data_list

    def _clean_headers(self, data_list):
        fields = [row for row in data_list if row[0].lower()=='index']
        drop_list = ['index', 'datatype', 'data size'] # TODO this should be a fixture
        clean_list = [ row for row in data_list if row[0].lower() not in drop_list ]
        return fields, clean_list

    def _make_updates(self, fields, values, table_name):
        update_values = []
        insert_values = []

        for row in values:
            if self._row_exists(fields, row, table_name):
                # self.db_connection.execute(query, args)
                update_values.append(row)
            else:
                insert_values.append(row)
        # else, add to insert list

        return update_values, insert_values

    def _row_exists(self, fields, row, table_name):
        # TODO complete function

        # Iterate over values looking for match
        # rules are different for each table... so a new fixture?
        return False
