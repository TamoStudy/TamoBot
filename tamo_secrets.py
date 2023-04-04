import os

"""

"""
class TamoSecrets:
    @staticmethod
    def read(file_name):
        path = os.getenv("HOME") + os.sep + "Documents" + os.sep + "TamoStudyBotSecrets" + os.sep + file_name

        with open(path, "r") as file:
            contents = file.read()
            return contents
        
    @staticmethod
    def get_token():
        return TamoSecrets.read("token")

    @staticmethod
    def get_server():
        return TamoSecrets.read("server_id")
        
    @staticmethod
    def get_client_id():
        return TamoSecrets.read("client_id")

    @staticmethod
    def get_client_secret():
        return TamoSecrets.read("client_secret")
