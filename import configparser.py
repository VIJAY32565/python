import configparser 
# create object 
config = configparser.ConfigParser()
# read file 
config.read('config.ini')
# access values 
host = config['DATABASE']['host']
user = config['DATABASE']['user']
password = config['DATABASE']['password']
port = config['SETTINGS']['port']
debug = config['SETTINGS']['debug']
NEON_PINK = "\033[38;5;200;48;5;0m"
NEON_CYAN = "\033[38;5;51;48;5;0m"
RESET="\033[0m"
print(NEON_PINK + host + RESET, NEON_CYAN + user + RESET, NEON_PINK + password + RESET)
print(NEON_CYAN + debug + RESET, NEON_PINK + port + RESET)