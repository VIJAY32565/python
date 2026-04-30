HOT_PINK = "\033[38;5;200;48;5;0m"
GOLD="\033[38;5;220;48;5;0m"
NEON_CYAN = "\033[38;5;51;48;5;0m"
RESET="\033[0m"
try:
    marks=int(input("Enter your marks: "))
    result=100/marks
    print("Your result is: ",result)
except ZeroDivisionError:
    print(HOT_PINK + "Marks cannot be zero. Please enter a valid number."+ RESET)
except ValueError:
    print(GOLD + "INVALID INPUT PLEASE ENTER AN INTEGER VALUE" + RESET)
finally:
    print(NEON_CYAN +"THANK YOU FOR USING OUR SERVICE"+ RESET)
try:
    f=open("non_existent_file.txt","r")
    content=f.read()
    print(HOT_PINK + content + RESET)
except FileNotFoundError:
    print(GOLD + "FILE NOT FOUND. PLEASE CHECK THE FILE NAME AND TRY AGAIN." + RESET)
finally:
    print(NEON_CYAN + "THANK YOU FOR USING OUR SERVICE" + RESET)
x=-7
if x<0:
    raise ValueError("SORRY WE DO NOT ACCEPT NEGATIVE NUMBERS")
class ValueToSmallError(Exception):
    """RAISES WHEN THE VALUE IS TOO SMALL"""
    pass
class ValueTooLargeError(Exception):
    """RAISES WHEN THE VALUE IS TOO LARGE"""
    pass
number=10
while True:
    try:
        user_input=int(input("Enter a number between 1 and 20: "))
        if user_input<1:
            raise ValueToSmallError
        elif user_input>20:
            raise ValueTooLargeError
        else:
            print("You entered: ",user_input)
            break
    except ValueToSmallError:
        print(HOT_PINK + "VALUE TOO SMALL. PLEASE ENTER A NUMBER BETWEEN 1 AND 20." + RESET)
    except ValueTooLargeError:
        print(GOLD + "VALUE TOO LARGE. PLEASE ENTER A NUMBER BETWEEN 1 AND 20." + RESET)