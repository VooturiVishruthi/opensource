n=int(input())
a=list(map(int,input().split()))
for i in set(a):
    if a.count(i)==1:
        print(i)
        break
