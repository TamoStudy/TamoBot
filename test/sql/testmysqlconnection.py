import unittest
from tamo_secrets import TamoSecrets
from sql.mysqlconnection import MySQLConnection

class TestMySQLConnection(unittest.TestCase):

    def setUp(self):
        self.db = MySQLConnection(TamoSecrets.get_db_database())

    def test_db_object_not_null(self):
        self.assertIsNotNone(self.db)

    def test_fetch_user_by_id(self):
        user_id = 190552534019080193
        user = self.db.fetch_user_by_id(user_id)

        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
