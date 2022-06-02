a=int(input())
c=0
for i in range(a):
    if(i*i==a):
        print(True)
        c=1
        break
if(c==0):
    print(False)