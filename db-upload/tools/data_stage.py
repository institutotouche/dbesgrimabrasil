import csv, json
import os

class DataStage(object):
    def __init__(self, pending_dir='upload-pending'):
        self.pending_path = os.path.join('.',pending_dir)
        csv_list = self._get_CSV_list()
        self.sorted_csv_list = self._prioritize(csv_list)

    def process_file(self, db_connection, file_name):
        table_name = file_name[:-4]
        raw_data_list = self._read_data(os.path.join(self.pending_path, file_name))
        fields, values = self._clean_headers(raw_data_list)

        # split inserts vs updates (updates go first)
        # fill cross-references
            # for both inserts and updates
            # watch out for inserts that refer to the same table (e.g. entities)
        # build list of (query, args) tuples
        return 0, 0 # returns list of (query, args) tuples

    def _get_CSV_list(self):
        # Renames CSV files to lower case and return list with new names
        for file in os.listdir(self.pending_path):
            if file[-4:]=='.csv':
                os.rename(os.path.join(self.pending_path,file),os.path.join(self.pending_path,file.lower()))
        return [file for file in os.listdir(self.pending_path) if file[-4:]=='.csv']

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
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data_list = [tuple(row) for row in reader]
        return data_list

    def _clean_headers(self, data_list):
        fields = [row for row in data_list if row[0].lower()=='index']
        drop_list = ['index', 'datatype', 'data size'] # TODO this should be a fixture
        clean_list = [ row for row in data_list if row[0].lower() not in drop_list ]
        return fields, clean_list
