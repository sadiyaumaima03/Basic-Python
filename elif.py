a = int(input("enter a val:"))
b = int(input("enter b val:"))
c = int(input("enter c val:"))

if(a>b and a>c):
    print("Greater = ", a)
elif(b>a and b>c):
    print("Greater = ",b)
else:
    print("Greater = ", c)