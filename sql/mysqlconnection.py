import mysql.connector
import datetime

from typing import List

from sql.model.dbUser import DBUser
from sql.model.dbMonthTime import DBMonthTime
from sql.model.dbDailyTime import DBDailyTime

from tamo_secrets import TamoSecrets
from tools.tamolog import TamoLogger

class MySQLConnection:
    def __init__(self, database):
        self.host = TamoSecrets.get_db_host()
        self.user = TamoSecrets.get_db_user()
        self.password = TamoSecrets.get_db_pass()
        self.database = database
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
            TamoLogger.loga("SUCCESS", "MySQLConnection.connect", "Connected successfully to MySQL database")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            TamoLogger.loga("SUCCESS", "MySQLConnection.disconnect", "Disconnected successfully from MySQL database")

    ##########################################
    ##########################################
    ##########################################
    # Create Operations
    ##########################################
    ##########################################
    ##########################################

    def create_user(self, user_id):
        """
        Creates a user in the database

        Args:
            user_id (int): The user's discord ID
        """
        sql = f'''
                INSERT INTO user
                (id, tokens, stime, zoneid, hex, trivia)
                VALUES
                ({user_id}, 0, 0, \'UTC\', \'383838\', 0)
            '''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        TamoLogger.log("INFO", f"Created new user with id {user_id}")

    def create_user_if_dne(self, user_id):
        """
        Ensures that the user exists in the database, creates user if they do not.

        Args
            user_id (int) : discord ID of user to create / lookup
        """
        if self.fetch_user_by_id(user_id) is None:
            TamoLogger.log("INFO", f"User ID {user_id} does not exist in user table. Calling create_user.")
            self.create_user(user_id)

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

    def create_user_monthtime_entry_if_dne(self, user_id):
        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year

        if self.fetch_month_time_of_user(user_id, current_month, current_year) is None:
            TamoLogger.log("INFO", f"User ID {user_id} does not have monthtime in monthtime table. Calling create_monthtime.")
            self.create_user_monthtime_entry(user_id)

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
        TamoLogger.log("INFO", f"Created dailytime entry for user {user_id} for month {current_month} and year {current_year}")

    def create_user_dailytime_entry_if_dne(self, user_id):
        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_day = now_utc.day               # Integer value of day
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year

        if self.fetch_daily_time_of_user(user_id, current_day, current_month, current_year) is None:
            TamoLogger.log("INFO", f"User ID {user_id} does not have dailytime in dailytime table. Calling create_dailytime.")
            self.create_user_dailytime_entry(user_id)

    def create_user_requirements_if_dne(self, user_id):
        self.create_user_if_dne(user_id)
        self.create_user_monthtime_entry_if_dne(user_id)
        self.create_user_dailytime_entry_if_dne(user_id)

    ##########################################
    ##########################################
    ##########################################
    # Read Operations
    ##########################################
    ##########################################
    ##########################################

    def fetch_user_by_id(self, user_id: int):
        """
        Fetches a user by their ID from the database.

        Args:
            user_id (int): The user's Discord ID.

        Returns:
            DBUser of the fetched user.
        """
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM user WHERE id={user_id}"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result is None:
            return None

        return DBUser(*result)

    def fetch_top_3_stime_users(self) -> List[DBUser]:
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

    def fetch_top_10_stime_monthly_users(self) -> List[DBUser]:
        """
        Fetches the top 10 users with the highest monthly stime from the monthtime table.

        Returns:
            dict: A dictionary containing user objects mapped to their corresponding monthly stime
        """
        TamoLogger.loga("INFO", "MySQLConnection.fetch_top_10_stime_monthly_users", f"Attempting fetching top 10 stime monthly users.")
        now_utc = datetime.datetime.utcnow()    # Normalize to UTC
        current_month = now_utc.month           # Integer value of month
        current_year = now_utc.year             # Integer value of year
        
        cursor = self.connection.cursor()
        query = f"""
                SELECT user_id, stime
                FROM monthtime
                WHERE yr = {current_year} AND mth = {current_month} AND user_id != 190552534019080193
                GROUP BY user_id
                ORDER BY stime DESC
                LIMIT 10;
                """
        cursor.execute(query)
        results = cursor.fetchall()
        top_users = []
        for result in results:
            user_id, monthly_stime = result
            top_users.append( (user_id, monthly_stime) )
        
        TamoLogger.loga("INFO", "MySQLConnection.fetch_top_10_stime_monthly_users", f"Returning top 10 monthly users {top_users}.")
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
            user_id, trivia = result
            top_users.append( (user_id, trivia) )
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

    def fetch_simple_stats_profile_by_id(self, user_id):
        """
        Simple fetch user, this will display
        - monthly time
        - user stime
        - tamo tokens
        - trivia wins
        - daily time
        """
        # Fetch User
        cursor = self.connection.cursor()
        query = f'SELECT stime, tokens, trivia FROM user WHERE id = {user_id}'
        cursor.execute(query)
        user_result = cursor.fetchone()

        stime = user_result[0]
        tokens = user_result[1]
        trivia = user_result[2]

        now_utc = datetime.datetime.utcnow()            # Normalize to UTC
        current_day = now_utc.day                       # Integer value of day
        current_month = now_utc.month                   # Integer value of month
        current_year = now_utc.year                     # Integer value of year
        self.create_user_requirements_if_dne(user_id)   # Special Check

        # Fetch Month Time
        query = f'SELECT stime FROM monthtime WHERE user_id={user_id} AND mth={current_month} AND yr={current_year}'
        cursor.execute(query)
        month_time = cursor.fetchone()[0]

        # Fetch Daily Time
        query = f'SELECT stime FROM dailytime WHERE user_id={user_id} AND d={current_day} AND mth={current_month} AND yr={current_year}'
        cursor.execute(query)
        daily_time = cursor.fetchone()[0]

        return (daily_time, month_time, stime, tokens, trivia)
    
    def fetch_hex_code_by_id(self, user_id):
        cursor = self.connection.cursor()
        query = f'SELECT hex FROM user WHERE id={user_id}'
        cursor.execute(query)
        return cursor.fetchone()[0]
    
    def fetch_tokens_by_id(self, user_id):
        cursor = self.connection.cursor()
        query = f'SELECT tokens FROM user WHERE id={user_id}'
        cursor.execute(query)
        return cursor.fetchone()[0]
    
    def fetch_random_trivia_question(self):
        """
        Fetches a random trivia question from the triviaquestion table.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM triviaquestion ORDER BY RAND() LIMIT 1;")
        result = cursor.fetchone()
        return result
    
    def fetch_trivia_by_id(self, user_id):
        cursor = self.connection.cursor()
        query = f'SELECT trivia FROM user WHERE id={user_id}'
        cursor.execute(query)
        return cursor.fetchone()[0]

    ##########################################
    ##########################################
    ##########################################
    # Update Operations
    ##########################################
    ##########################################
    ##########################################

    def update_user_total_entry(self, user_id, seconds, tokens):
        # Add Tamo Tokens based off of amount of seconds studied, user.tokens
        cursor = self.connection.cursor()
        query = f"UPDATE user SET tokens = tokens + {tokens} WHERE id = {user_id}"
        cursor.execute(query)
        self.connection.commit()

        # Updates daily time, dailytime.stime
        day = datetime.datetime.utcnow().day
        month = datetime.datetime.utcnow().month
        year = datetime.datetime.utcnow().year
        query = f"UPDATE dailytime SET stime = stime + {seconds} WHERE user_id = {user_id} AND d = {day} AND mth = {month} AND yr = {year}"
        cursor.execute(query)
        self.connection.commit()

        # Updates monthly time, monthtime.stime
        query = f"UPDATE monthtime SET stime = stime + {seconds} WHERE user_id = {user_id} AND mth = {month} AND yr = {year}"
        cursor.execute(query)
        self.connection.commit()

        # Updates total time, user.stime
        query = f"UPDATE user SET stime = stime + {seconds} WHERE id = {user_id}"
        cursor.execute(query)
        self.connection.commit()

    def update_user_hex(self, user_id, hex):
        """
        Updates the user's hex value in the database.

        Args:
            user_id (int): The user's Discord ID.
            hex_value (str): The new hex value to be assigned to the user.

        Returns:
            None
        """
        cursor = self.connection.cursor()
        query = "UPDATE user SET hex=%s WHERE id=%s"
        values = (hex, user_id)
        cursor.execute(query, values)
        self.connection.commit()

    def update_user_feat(self, user_id, feat):
        """
        Updates the user's feat value in the database.

        Args:
            user_id (int): The user's Discord ID.
            feat_value (str): The new feat value to be assigned to the user.

        Returns:
            None
        """
        cursor = self.connection.cursor()
        query = "UPDATE user SET feat=%s WHERE id=%s"
        values = (feat, user_id)
        cursor.execute(query, values)
        self.connection.commit()

    def update_subtract_user_tokens(self, user_id, tokens):
        current_tokens = int(self.fetch_tokens_by_id(user_id))
        updated_tokens = int(current_tokens) - int(tokens)
        TamoLogger.loga("INFO","MySQLConnection.update_subtract_user_tokens", f"current_tokens = {current_tokens}, tokens = {tokens}, updated_tokens = {updated_tokens}")

        cursor = self.connection.cursor()
        query = f"UPDATE user SET tokens = {updated_tokens} WHERE id = {user_id}"
        cursor.execute(query)
        self.connection.commit()

    def update_trivia_win(self, user_id):
        cursor = self.connection.cursor()
        query = f"UPDATE user SET trivia = trivia + 1 WHERE id = {user_id}"
        cursor.execute(query)
        self.connection.commit()

    ##########################################
    ##########################################
    ##########################################
    # Delete Operations
    ##########################################
    ##########################################
    ##########################################