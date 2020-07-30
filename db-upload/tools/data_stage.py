import csv, json
import os

class DataStage(object):
    def __init__(self, pending_dir='upload-pending'):
        # get file_list
        file_list = os.path.listdir(os.path.join('.',pending_dir))
        # get only csvs
        for f in file_list:
            if f[-4:] != '.csv':
                file_list.remove(f)
        # load priority list
        with open(os.path.join('.','fixtures','table_priority_order.txt'), "r") as priority_file:
            priority_list = json.load(priority_file)
        priority_list = [f.lower() for f in priority_list] # ensure everything is lower case
        
        # sort files according to priority
        self.sorted_file_list = file_list

    def process_file(self, db_connection, file_path):
        # read data
        # clean headers
        # split inserts vs updates (updates go first)
        # fill cross-references
            # for both inserts and updates
            # watch out for inserts that refer to the same table (e.g. entities)
        # build list of (query, args) tuples
        return 0, 0 # returns list of (query, args) tuples

    def _clean_headers(self):
        return None
