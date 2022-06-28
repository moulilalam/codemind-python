a=int(input())
c=k=l=0
while a>0:
    d=a%10
    c=c+1
    if d%2==0:
        k=k+1
    if d%2!=0:
        l=l+1
    a=a//10
if c==k:
    print('Even')
elif c==l:
    print('Odd')
else:
    print('Mixed')