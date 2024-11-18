a=int(input())
l=list(map(int,input().split()))
if(l==sorted(l)):
    print("true")
else:
    print("false")
