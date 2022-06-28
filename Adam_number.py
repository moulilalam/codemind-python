a=int(input())#12
k=a
rev=rev1=rev2=0
while a>0:
    d=a%10
    rev=rev*10+d#21
    a=a//10
l=rev**2#441
m=k**2#144
while l>0:
    d=l%10
    rev1=rev1*10+d#144
    l=l//10
if rev1==m:
    print('True')
else:
    print('False')

