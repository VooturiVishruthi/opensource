x,y,z=map(int,input().split())
z=z-y
c=0
for i in range(1,z):
    if i*x<=z:
        c=c+1
print(c)
