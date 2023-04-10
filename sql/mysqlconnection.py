import mysql.connector
from tamo_secrets import TamoSecrets

class MySQLConnection:
    def __init__(self):
        self.host = TamoSecrets.get_db_host()
        self.user = TamoSecrets.get_db_user()
        self.password = TamoSecrets.get_db_pass()
        self.database = TamoSecrets.get_db_database()
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Connected to MySQL database")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def search(self, table, column, value):
        if not self.connection.is_connected():
            self.connect()
        cursor = self.connection.cursor()
        query = "SELECT * FROM {} WHERE {} = %s".format(table, column)
        cursor.execute(query, (value,))
        result = cursor.fetchall()
        cursor.close()
        return result