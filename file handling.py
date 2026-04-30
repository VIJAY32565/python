f=open("C:\\Users\\karth\\OneDrive\\Documents\\file handling\\file.txt","r")
ICE_BLUE= "\033[38;5;123;48;5;0m"
ROSE="\033[38;5;205;48;5;0m"
NEON_GREEN="\033[38;5;46;48;5;0m"
RESET="\033[0m"
print(ICE_BLUE+f.read()+ RESET)
f.close()
f=open("C:\\Users\\karth\\OneDrive\\Documents\\file handling\\file.txt","a")
f.write("\nThis is a new line added to the file")
f.write( NEON_GREEN +"\n NARUTO UZUMAKI DATTEBAYO" + RESET)
f.write( ROSE + "\nOREWA MONKEY D LUFFY " + RESET)
f.close()
f=open("C:\\Users\\karth\\OneDrive\\Documents\\file handling\\file.txt","r")
print(ROSE+f.read()+ RESET)
f.close()