n=int(input("enter n value :"))
for i in range (1,n+1):
    if(i%2 ==0 and i%3==0):
        print("%d\n"%i)
        
p=int(input("enter p value :"))
for i in range(1,p+1):
    if(i%4!=0 and i%6!=0):
        print("%d\n"%i)


list1=[0,1,2,3,4]
list2=[5,6,7,8,9]
print(list1+list2)
print(list2*3)

