n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    k=k+l[i]
print(k)