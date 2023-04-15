import mysql.connector
import datetime
from tamo_secrets import TamoSecrets
from tools.tamolog import TamoLogger

class MySQLConnection:
    def __init__(self):
        self.host = TamoSecrets.get_db_host()
        self.user = TamoSecrets.get_db_user()
        self.password = TamoSecrets.get_db_pass()
        self.database = TamoSecrets.get_db_database()
        self.connection = None

    # Connect / Disconnect to Database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            TamoLogger.log("INFO", "Connected successfully to MySQL database")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            TamoLogger.log("INFO", "Disconnected successfully from MySQL database")

    ##########################################
    ##########################################
    ##########################################
    # Create Operations
    ##########################################
    ##########################################
    ##########################################

    def create_user(self, user_id: int):
        """
        Creates a user in the database

        Args:
            user_id (int): The user's discord ID
        """
        sql = f'''
                INSERT INTO user
                (id, tokens, stime, zoneid, hex, trivia)
                VALUES
                ({user_id}, 0, 0, UTC, 383838, 0)
            '''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        TamoLogger.log("INFO", f"Created new user with id {user_id}")

    def create_user_monthtime_entry(self, user_id):
        """
        Creates a user monthtime entry in the database.
        Gets the current month of based off of the time in UTC.
        The monthly time will be set to zero by default.

        Args:
            user_id (int): The user's discord ID
        """
        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year
        
        sql = f'''
                INSERT INTO monthtime
                (id, mth, yr, stime)
                VALUES
                ({user_id}, {current_month}, {current_year}, 0)
            '''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        TamoLogger.log("INFO", f"Created monthtime entry for user {user_id} for month {current_month} and year {current_year}")

    def create_user_dailytime_entry(self, user_id):
        """
        Creates a user monthtime entry in the database.
        Gets the current month of based off of the time in UTC.
        The monthly time will be set to zero by default.

        Args:
            user_id (int): The user's discord ID
        """
        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_day = now_utc.day               # Integer value of day
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year
        
        sql = f'''
                INSERT INTO dailytime
                (id, d, mth, yr, stime)
                VALUES
                ({user_id}, {current_day}, {current_month}, {current_year}, 0)
            '''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        TamoLogger.log("INFO", f"Created monthtime entry for user {user_id} for month {current_month} and year {current_year}")

    ##########################################
    ##########################################
    ##########################################
    # Read Operations
    ##########################################
    ##########################################
    ##########################################

    def fetch_user_profile_by_id(self, user_id):
        # TODO
        pass

    def fetch_top_3_stime_users(self):
        # TODO
        pass

    def fetch_top_3_stime_monthly_users(self):
        # TODO
        pass

    def fetch_top_3_trivia_users(self):
        # TODO
        pass

    ##########################################
    ##########################################
    ##########################################
    # Update Operations
    ##########################################
    ##########################################
    ##########################################

    def update_user_total_entry(self, user_id, seconds):
        # Add Tamo Tokens based off of amount of seconds studied, user.tokens

        # Updates daily time, dailytime.stime

        # Updates monthly time, monthtime.stime

        # Updates total time, user.stime

        #TODO
        pass

    def update_user_hex(self, user_id, hex):
        # Update user.hex attribute
        pass

    def update_user_feat(self, user_id, feat):
        # Update user.feat attribute
        pass

    ##########################################
    ##########################################
    ##########################################
    # Delete Operations
    ##########################################
    ##########################################
    ##########################################