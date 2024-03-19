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
#Ex25
words = []
word = input()
while word != 'КОНЕЦ':
    words.append(word)
    word = input()

for w in words:
    print(w)
#Ex26
words = []
word = input()
while word != 'КОНЕЦ' and word != 'конец':
    words.append(word)
    word = input()

for w in words:
    print(w)
#Ex27
words = []
word = input()
while word != 'стоп' and word != 'хватит' and word!='достаточно':
    words.append(word)
    word = input()
print(len(words))
#Ex28
while True:
    num = int(input())
    if num % 7 == 0:
        print(num)
    else:
        break
#Ex29
sum=0
num=int(input())
while num>0 and num<=5:
    if num==5:
        sum+=1
    num=int(input())
print(sum)
#Ex30
mylist=[25,10,5,1]
sum=0
num=int(input())
cnt=0
ss=0
while sum!=num:
    if sum+mylist[ss]<=num:
        while sum+mylist[ss]<=num:
            sum+=mylist[ss]
            cnt+=1
    else:
        ss+=1
        if ss>3:
            break
print(cnt)
#Ex31
num=int(input())
while num!=0:
    san=num%10
    print(san)
    num//=10
#Ex32
num=int(input())
mylist=[]
while num>0:
    mylist.append(num%10)
    num//=10
for i in mylist:
    print(i,end="")
#Ex33
num=int(input())
maximum=-999
minimum=999
while num>0:
    if num%10>maximum:
        maximum=num%10
    if num%10<minimum:
        minimum=num%10
    num//=10
print("Максимальная цифра равна",maximum)
print("Минимальная цифра равна",minimum)
#Ex34
num=int(input())
sum=0
cnt=0
product=1
srednee=0
first=0
sum_last=0
last=num%10
while num>0:
    sum+=num%10
    cnt+=1
    product*=num%10
    first=num%10
    num//=10
srednee=sum/cnt
sum_last=first+last
print(sum)
print(cnt)
print(product)
print(srednee)
print(first)
print(sum_last)
#Ex35
cnt=0
num=int(input())
num1=num
while num1>0:
    cnt+=1
    num1//=10
cnt-=2
if cnt==0:
    print(num%10)
else:
    while cnt>0:
        num//=10
        cnt-=1
    print(num%10)
#Ex36
num=int(input())
last=num%10
ans=True
mylist=[]
while num>0:
    mylist.append(num%10)
    num//=10
for i in mylist:
    if i!=last:
        ans=False
if ans:
    print("YES")
else:
    print("No")
#Ex37
num=int(input())
last=num%10
num//=10
ans=True
while num>0:
    if last>num%10:
        ans=False
        break
    else:
        last=num%10
    num//=10
if ans:
    print("YES")
else:
    print("NO")
#Ex38
num=int(input())
menshe=2
if num%menshe==0:
    print(menshe)
else:
    while num%menshe!=0:
        menshe+=1
    print(menshe)
#Ex39
num=int(input())
mylist=[]
for i in range(1,num+1):
    mylist.append(i)
for i in mylist:
    if i==0:
        continue
    if i<5:
        print(i)
    if i>9 and i<17:
        print(i)
    if i>37 and i<78:
        print(i)
    if i>87:
        print(i)
        