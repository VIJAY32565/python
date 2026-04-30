def sum1():
    a = 10
    b = 200
    add = a + b
    print("sum is:", add)

sum1()


def sum2(x=10, y=30, z=40):
    add = x + y + z
    print("sum is:", add)

sum2(x=10, y=90, z=20)
sum2(x=10)
sum2(x=30, y=20)


def display(name="kartheek", age=20):
    print(f"MY NAME IS {name} AND AGE IS {age}")

display()
display("Karthik", 21)