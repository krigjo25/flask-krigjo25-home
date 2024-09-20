import os
import pytest

from core import SQL

class TestDatabase:

    #   
    sql = SQL(database='test_database.db')
    table = 'test_table'

    def test_sql_connection(self) -> None:

        """ Testing sqlite connection"""

        #   Asserts the name of the database
        assert os.path.exists('test_database.db')

    #   Table tests
    def test_createTable(self):

        #   Initialize a database connection

        #   Initialize query
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data1':'BLOB NOT NULL DEFAULT FALSE', 'data2':'REAL NOT NULL DEFAULT 0', 'date':'NUMERIC NOT NULL DEFAULT DATE'}

        #   Initialize data into the database
        self.sql.TableConfigurations(self.table, 'CREATE', mock)
        
        #   Fetch table information
        actual = self.sql.conn.execute('SELECT name FROM sqlite_master;').fetchall()

        #   Test the data
        assert actual[0][0] == self.table

        #   Sweep Data
        del mock, actual

        return
    
    #   Update
    #def test_updateTable(self): pass

    # Value tests
    def test_insertdata(self):
        
        data = {}
        columns = ('data', 'data1', 'data2')
        mock = ('Sometext', 'image.jpg', 2.0)

        for i in range(len(columns)):
            for j in range(len(mock)):
                data[columns[i]] = mock[i]
         
        self.sql.insert_into_table(self.table, 'INSERT', columns, data)
        actual = self.sql.conn.execute(f'SELECT data, data1, data2 FROM {self.table}').fetchall()
        assert actual == [mock]

    #   Select
#    def test_selectRecord(self): pass


