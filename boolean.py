age=input("enter age:")
if age.isdigit():
    age=int(age)
    print("valid age☆*: ｡ o")
else:
    print("invalid age ❁´◡`❁")
n=int(input("enter a number:"))
if 1<n<10:
      print("valid ●◡ ●")
else:
    print("INVALID")
p=input("enter password:")
if len(p)>=6 and '☠☠' in p:
    print("STRONG☠☠")
else:
    print("TOO WEAK^_____^")
    g=input("enter g mail:")
if '@' in g and '.' in g:
    print("VALID G MAIL")
else:
    print("INVALID G MAIL")


numbers =[10,20,30,40]
total=0
for num in numbers:
    total=total+num
    print("\nRUNNING TOTAL:",total)



n=int(input("how many numbers?"))
total=0
for  i in range (n):
    num=int(input("\nenter number:"))
    total+=num
    print("\nRUNNING TOTAL :",total)
