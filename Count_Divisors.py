i,r,k=map(int,input().split())
c=0
for m in range(i,r+1):
    if(m%k==0):
        c+=1
print(c)
    
    