import csv
with open("Book1.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","city"])#header
    writer.writerow(["Harshitha",20,"hyderabad"])
    writer.writerow(["rohith",19,"kurnool"])
