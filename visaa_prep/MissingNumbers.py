a1=int(input())
arr=list(map(int,input().split()))
a2=int(input())
brr=list(map(int,input().split()))
a={}
b={}
for i in arr:
    a[i]=a.get(i,0)+1
for i in brr:
    b[i]=b.get(i,0)+1
m=[]
for i ,f in b.items():
    if i not in a or a[i]<f:
        m.append(i)
print(*sorted(set(m)))
