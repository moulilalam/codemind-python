n=int(input())
c=k=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]%2==0:
        c+=1
    else:
        k+=1
print(c,k)
