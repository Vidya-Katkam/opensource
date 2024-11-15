n=int(input())
if n>=3 and n<=5:
    print("Spring")
elif n>=6 and n<=8:
    print("Summer")
elif n>=9 and n<=11:
    print("Autumn")
elif n==1 or n==2 or n==12:
    print("Winter")
else:
    print("Invalid")
