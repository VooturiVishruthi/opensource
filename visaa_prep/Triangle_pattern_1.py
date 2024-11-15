n=int(input())
nu=1
for i in range(1,n+1):
    for j in range(0,i):
        print(nu,end=" ")
        nu=nu+1
    print()
