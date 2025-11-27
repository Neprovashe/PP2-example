from configparser import ConfigParser

def load_config(filename="database.ini"):
    """ Load database configuration """
    parser = ConfigParser()
    parser.read(filename)
    return {
        "host": parser.get("postgresql", "host"),
        "database": parser.get("postgresql", "database"),
        "user": parser.get("postgresql", "user"),
        "password": parser.get("postgresql", "password")
    }
