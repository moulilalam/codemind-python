a=int(input())
b=int(input())
k=l=0
for i in range(1,a):
    if a%i==0:
        k=k+i
for j in range(1,b):
    if b%j==0:
        l=l+j
if k==b and l==a:
    print('Amicable')
else:
    print('Not Amicable')