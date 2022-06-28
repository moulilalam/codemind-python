a=int(input())
sum=0
c=0
temp=a
s=a
while a>0:
    d=a%10
    c=c+1
    a=a//10
while temp:
    d=temp%10
    d=d**c
    c-=1
    sum=sum+d
    temp=temp//10
if sum==s:
    print('True')
else:
    print('False')
    