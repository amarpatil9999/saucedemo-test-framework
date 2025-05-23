import configparser

# Initialize the parser
config = configparser.RawConfigParser()

# Read the configuration file
config.read("configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        urlValue = config.get("login credentials","url")
        return urlValue

    @staticmethod
    def getUsername():
        usernameValue = config.get("login credentials","username")
        return usernameValue

    @staticmethod
    def getPassword():
        passwordValue = config.get("login credentials","password")
        return passwordValue
