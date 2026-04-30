try:
    marks=25
    result=25/0
    print(result)
except ZeroDivisionError:
       print(" A number cannot be divide by zero")

finally:
    print("code runs succesfully")


x=-7
if x<0:
   raise Exception("sorry we con't accept below zero")
