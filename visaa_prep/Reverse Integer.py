a=int(input())
s=-1 if a<0 else 1
a=abs(a)
rev_n=int(str(a)[::-1])
if(rev_n<-2**31 or rev_n>2**31-1):
    print(0)
else:
    print(s*rev_n)
