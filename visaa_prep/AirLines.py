x,N=map(int,input().split())
if N%100==0:
    print((N//100)-x)
else:
    print((N//100)+1-x)
