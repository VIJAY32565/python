import json

with open('config.json') as f:
    config = json.load(f)

host = config["DATABASE"]["HOST"]
port = config["DATABASE"]["PORT"]
user = config["DATABASE"]["USER"]
password = config["DATABASE"]["PASSWORD"]
debug = config["SETTINGS"]["debug"]
GOLD= "\033[38;5;220;48;5;0m"
HOT_PINK = "\033[38;5;200;48;5;0m"
RESET="\033[0m"

print( GOLD + host + RESET, HOT_PINK + str(port) + RESET, GOLD + user + RESET, HOT_PINK + password + RESET)
print( GOLD + str(debug) + RESET )