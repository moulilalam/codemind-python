def is_prime(n):
    if n==0 or n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
k=a+b+1
c=a+b
while 1:
    if is_prime(k):
        z=k
        break
    k=k+1
print(abs(c-z))