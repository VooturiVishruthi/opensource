n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    s1=sum(a[:i])
    s2=sum(a[i+1:])
    s.append(abs(s1-s2))
print(*s)
