def add(n):
    sum=0
    if n<=9:
        return n
    else:
        while n:
            d=n%10
            sum+=d
            n//=10
    n=sum
    return add(n)
n=int(input())
print(add(n))