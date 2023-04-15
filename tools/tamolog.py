from datetime import datetime
FORMAT = "%Y-%m-%d %H:%M:%S"
RESET = '\033[0m'

class TamoLogger():
    @staticmethod
    def log(level, message):
        # Format Time
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        level_color = '\033[31m'
        if level == 'INFO':
            level_color = '\033[36m'

        # Print Message
        print(f"\033[33m{formatted_time}{RESET} {level_color}{level}{RESET} {message}")