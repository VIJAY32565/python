n=int(input("enter n value:"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


a=[[1,2,3],
      [4,6,7],
     [8,9,10],]
b=[[4,67,89],
      [3,6,8],
     [56,78,9]]
res=[[0,0,0],
         [0,0,0],
        [0,0,0]]
for i in range (3):
    for j in range (3):
        res[i][j]=a[i][j]+b[i][j]

for i in range (3):
    for j in range (3):
         print("%d"%res[i][j],end=" ")
    print()

