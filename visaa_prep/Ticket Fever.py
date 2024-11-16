a=int(input())
for i in range(0,a):
    p,q=map(int,input().split())
    if p>=q:
        print(p-q)
    else:
        print("0")
