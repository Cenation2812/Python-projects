import configparser

config = configparser.ConfigParser()

config.read("network.ini")

data = config.get("mysql","port")

print(config.sections())

print(config.options("mongodb"))