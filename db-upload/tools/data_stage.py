import csv, json
import os

class DataStage(object):
    def __init__(self, pending_dir='upload-pending'):
        self.pending_path = os.path.join('.',pending_dir)
        csv_list = self._get_CSV_list()
        self.sorted_csv_list = self._prioritize(csv_list)

    def process_file(self, db_connection, file_path):
        # read data
        # clean headers
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

    def _clean_headers(self):
        return None
