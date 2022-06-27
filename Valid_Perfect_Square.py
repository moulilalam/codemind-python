n=int(input())
for i in range(0,n):
    a=int(input())
    for i in range(0,a):
        if int(i)**2 == a:
            print('True')
            break
    else:
        print('False')
        

    