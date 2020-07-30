import csv, json
import os

class DataStage(object):
    def __init__(self, pending_dir='upload-pending'):
        # get file_list
        # sort files according to priority
        self.sorted_file_list = [1,2]
        return None

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
