a=int(input())
rev=rev1=0
m=a
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
    #print(rev)
k=m**2
l=rev**2
#print(k,l)
while l>0:
    d=l%10
    rev1=rev1*10+d
    l=l//10
   # print(rev1)
if rev1==k:
    print('True')
else:
    print('False')