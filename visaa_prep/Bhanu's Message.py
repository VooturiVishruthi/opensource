a=input()
if(a[0]=='+' and a[1:3].isdigit() and a[3]==" " and len(a)==14 and a[4:].isdigit() and sum(int(digit) for digit in a[4:])>0):
    print("Correct")
else:
    print("Incorrect")
