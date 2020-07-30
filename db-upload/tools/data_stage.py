import csv, json
import os

class DataStage(object):
    def __init__(self, pending_dir='upload-pending'):
        # get file_list
        file_list = os.path.listdir(os.path.join('.',pending_dir))
        csv_list = self._keep_only_csv(file_list)

        # sort files according to priority
        self.sorted_file_list = self._prioritize(file_list)

    def process_file(self, db_connection, file_path):
        # read data
        # clean headers
        # split inserts vs updates (updates go first)
        # fill cross-references
            # for both inserts and updates
            # watch out for inserts that refer to the same table (e.g. entities)
        # build list of (query, args) tuples
        return 0, 0 # returns list of (query, args) tuples

    def _keep_only_csv(self, file_list):
        return [file for file in file_list if file[-4:]=='.csv']

    def _prioritize(self, file_list):
        # load priority list
        with open(os.path.join('.','fixtures','table_priority_order.txt'), "r") as priority_file:
            priority_list = json.load(priority_file)
        priority_list = [f.lower() for f in priority_list] # ensure everything is lower case

        return sorted_file_list


    def _clean_headers(self):
        return None
