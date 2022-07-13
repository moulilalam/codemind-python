n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(0,len(l)):
    for j in range(1,l[i]+1):
        if l[i]==j*j:
            k=k+l[i]
print(k)