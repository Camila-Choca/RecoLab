import sqlite3

class DatabaseManager():

    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    def executeQuery(self, queryToExecute):
        return self.cursor.execute(queryToExecute)

    def executeMany(self, queryToExecute):
        return self.cursor.executemany(queryToExecute)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def printAll(self):
        self.executeQuery('''
            SELECT * FROM test
        ''')
        print self.cursor.fetchall().__repr__

if __name__=="__main__":
    db = DatabaseManager()
    db.printAll()