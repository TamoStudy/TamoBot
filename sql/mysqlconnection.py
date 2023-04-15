import mysql.connector
import datetime

from sql.model.dbUser import DBUser
from sql.model.dbMonthTime import DBMonthTime
from sql.model.dbDailyTime import DBDailyTime

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
                (user_id, mth, yr, stime)
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
                (user_id, d, mth, yr, stime)
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

    def fetch_user_profile_by_id(self, user_id: int):
        """
        Fetches a user by their ID from the database.

        Args:
            user_id (int): The user's Discord ID.

        Returns:
            tuple: A tuple containing the user's data, or None if the user is not found.
        """
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM user WHERE id={user_id}"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result is None:
            return None

        return DBUser(*result)

    def fetch_top_3_stime_users(self):
        """
        Fetches the top 3 users with the highest stime values from the user table.

        Returns:
            A list of the top 3 users as `DBUser` objects, sorted by stime in descending order.
        """
        cursor = self.connection.cursor()
        query = "SELECT id, stime FROM user ORDER BY stime DESC LIMIT 3"
        cursor.execute(query)
        results = cursor.fetchall()
        top_users = []
        for result in results:
            user = DBUser(*result)
            top_users.append(user)
        return top_users

    def fetch_top_3_stime_monthly_users(self):
        """
        Fetches the top 3 users with the highest monthly stime from the monthtime table.

        Returns:
            dict: A dictionary containing user objects mapped to their corresponding monthly stime
        """
        cursor = self.connection.cursor()
        query = """
                SELECT user_id, stime
                FROM monthtime
                GROUP BY user_id
                ORDER BY stime DESC
                LIMIT 3
                """
        cursor.execute(query)
        results = cursor.fetchall()
        top_users = {}
        for result in results:
            user_id, monthly_stime = result
            user = self.fetch_user_by_id(user_id)
            top_users[user_id] = (user, monthly_stime)
        return top_users

    def fetch_top_3_trivia_users(self):
        """
        Fetches the top 3 users with the highest trivia scores from the database.

        Returns:
            list: A list containing the top 3 users with the highest trivia scores.
        """
        cursor = self.connection.cursor()
        query = "SELECT id, trivia FROM user ORDER BY trivia DESC LIMIT 3"
        cursor.execute(query)
        results = cursor.fetchall()
        top_users = []
        for result in results:
            user = DBUser(*result)
            top_users.append(user)
        return top_users

    def fetch_month_time_of_user(self, user_id, month, year):
        """
        Fetches the monthly stime of a user for a given month and year.

        Args:
            user_id (int): The user's Discord ID.
            month (int): The month (1-12) for which to fetch the stime.
            year (int): The year for which to fetch the stime.

        Returns:
            int: The monthly stime of the user for the specified month and year, or None if the user is not found.
        """
        cursor = self.connection.cursor()
        sql = f"SELECT stime FROM monthtime WHERE user_id = {user_id} AND mth = {month} AND yr = {year}"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result is None:
            return None

        return result[0]

    def fetch_daily_time_of_user(self, user_id, day, month, year):
        """
        Fetches the daily stime of a user for a given day, month, and year.

        Args:
            user_id (int): The user's Discord ID.
            day (int): The day of the month (1-31) for which to fetch the stime.
            month (int): The month (1-12) for which to fetch the stime.
            year (int): The year for which to fetch the stime.

        Returns:
            int: The daily stime of the user for the specified day, month, and year, or None if the user is not found.
        """
        cursor = self.connection.cursor()
        sql = f"SELECT stime FROM dailytime WHERE user_id = {user_id} AND d = {day} AND mth = {month} AND yr = {year}"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result is None:
            return None

        return result[0]

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