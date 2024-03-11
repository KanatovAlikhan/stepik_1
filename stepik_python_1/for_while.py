#Ex1
for i in range(10):
    print("Python is awesome!")
#Ex2
s=input()
n=int(input())
for i in range(n):
    print(s)
#Ex3
for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")
#Ex4
n=int(input())
for i in range(n):
    print("*******************")
#Ex5
i=0
s=input()
while i<10:
    print(i,s)
    i+=1
#Ex6
i=int(input())
s=0
while s<=i:
    print("Квадрат числа",s,"равен",s*s)
    s+=1
#Ex7
i=int(input())
while i>0:
    print("*"*i)
    i-=1
#Ex8
m=int(input())
p=int(input())
n=int(input())
print(1,float(m))
for i in range(2,n+1):
    m=m+m*(p/100)
    print(i,m)
#Ex9
n=int(input())
m=int(input())
for i in range(n,m+1):
    print(i)
#Ex10
n=int(input())
m=int(input())
if n>m:
    for i in range(n,m-1,-1):
        print(i)
elif n==m:
    print(n)
else:
    for i in range(n,m+1):
        print(i)
#Ex11
n=int(input())
m=int(input())
for i in range(n,m-1,-1):
    if i%2==1:
        print(i)
#Ex12
n=int(input())
m=int(input())
for i in range(n,m+1):
    if i%17==0:
        print(i)
    elif i%10==9:
        print(i)
    elif i%15==0:
        print(i)
#Ex13
n=int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#Ex14
n=int(input())
m=int(input())
cnt=0
for i in range(n,m+1):
    if (i**3)%10==4 or (i**3)%10==9:
        cnt+=1
print(cnt)
#Ex15
n=int(input())
sum=0
for i in range(n):
    a=int(input())
    sum+=a
print(sum)
#Ex16
import math 
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=1/i
print(sum-math.log(n))
#Ex17
n=int(input())
sum=0
for i in range(1,n+1):
    if (i**2)%10==2 or (i**2)%10==5 or (i**2)%10==8:
        sum+=i
print(sum)
#Ex18
n=int(input())
sum=1
for i in range(1,n+1):
    sum*=i
print(sum)
#Ex19
total=1
for i in range(10):
    a=int(input())
    if a!=0:
        total*=a
print(total)
#Ex20
n=int(input())
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum+=i
print(sum)
#Ex21
n=int(input())
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum+=i
    else:
        sum-=i
print(sum)
#Ex22
mylist=list()
n=int(input())
for i in range(n):
    a=int(input())
    mylist.append(a)
mylist.sort()
print(mylist[n-1])
print(mylist[n-2])
#Ex23
ans=True
for i in range(10):
    a=int(input())
    if a%2==1:
        ans=False
if ans:
    print("YES")
else:
    print("NO")
#Ex24
n=int(input())
mylist=[1,1,2]
if n>3:
    for i in range(3,n):
        mylist.append(mylist[i-2]+mylist[i-1])
    for i in mylist:
        print(i,end=" ")
else:
    for i in range(0,n):
        print(mylist[i],end=" ")