import csv, json
import os

class DataStage(object):
    def __init__(self, db_connection, pending_dir='upload-pending', archive_dir='upload-completed'):
        self.pending_path = os.path.join('.',pending_dir)
        self.complete_path = os.path.join('.',archive_dir)
        csv_list = self._get_CSV_list()
        self.sorted_csv_list = self._prioritize(csv_list)
        self.query_manager = QueryManager(db_connection)

    def process_file(self, file_name):
        table_name = file_name[:-4]
        raw_data_list = self._read_data(os.path.join(self.pending_path, file_name))
        fields, datatypes, values = self._clean_headers(raw_data_list)

        update_values, insert_values = self.query_manager.make_updates(fields, datatypes, values, table_name)
        self.query_manager.make_inserts(fields, insert_values, table_name)

        # TODO think about meaningful return
        return 0, 0 # returns list of (query, args) tuples

    def _get_CSV_list(self):
        # Renames CSV files to adequate case and return list with new names
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
        fields = list([row for row in data_list if row[0].lower()=='index'][0])
        datatypes = list([row for row in data_list if row[0].lower()=='datatype'][0])
        drop_list = ['index', 'datatype', 'data size'] # TODO this should be a fixture
        clean_list = [ row for row in data_list if row[0].lower() not in drop_list ]

        if fields[0].lower()=='index':
            fields.pop(0)
            datatypes.pop(0)
            clean_list = [row[1:] for row in clean_list]

        return fields, datatypes, clean_list

    def archive_file(self, filename):
        if not os.path.exists(self.complete_path):
            os.mkdir(self.complete_path)
        os.rename(os.path.join(self.pending_path,filename),
                os.path.join(self.complete_path,filename)
                )


class QueryManager(object):

    def __init__(self, db_connection):
        self.db_connection = db_connection
        # TODO read base queries from fixture (?)

    def make_updates(self, fields, datatypes, values, table_name):
        update_values = []
        insert_values = []

        for row in values:
            if self._row_exists(fields, datatypes, row, table_name):
                # TODO does the insert tag ON DUPLICATE KEY solve all of this? Only if having index?
                # TODO maybe "_row_exists" should return only fields to add?
                # cursor.execute(query, args)
                update_values.append(row)
            else:
                insert_values.append(row)

        return update_values, insert_values

    def make_inserts(self, fields, values, table_name):
        # TODO write query and function
        base_query = ' '.join(['INSERT INTO', table_name, '( )'])
        # with self.db_connection.cursor() as cursor:
            # cursor.execute(insert_query, [fields, values])
        return False

    def _row_exists(self, fields, datatypes, row, table_name):
        # TODO complete function

        base_query = ' '.join(['SELECT * FROM', table_name, 'WHERE'])
        with self.db_connection.cursor() as cursor:
            query = base_query
            for field, datatype, value in zip(fields, datatypes, row):
                if field.lower() == 'index':
                    continue
                elif value:
                    new_clause = self._add_field_to_where_clause(field, value, datatype)
                    query = ' '.join([query, new_clause])
            if query[-3:] == ' OR':
                query = query[:-3]
            cursor.execute(query)
            results = cursor.fetchall()
        # TODO assess results (is it enough that one value was found?)
        # TODO rules may be different for each table... so a new fixture?
        return False

    def _add_field_to_where_clause(self, field, value, datatype):
        # TODO move datatype variants into fixture
        text_types = ['Text', 'Varchar', 'Char']
        date_types = ['Date', 'Datetime']
        if datatype in date_types:
            # dates may frequently coincide between different entries so shouldn't be compared
            # TODO unless maybe in combination with other fields?
            return ''
        if datatype in text_types:
            where_clause = ''.join(['LOWER(', field, ') LIKE \'%', str(value).lower(), '%\' OR'])
        else:
            where_clause = ''.join([field, '=', value, ' OR'])
        return where_clause
