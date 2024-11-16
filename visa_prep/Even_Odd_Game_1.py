n=int(input())
s=0
while n>0 : 
    r = n%10
    n=n//10
    s=s+r
if s%2==0:
    print("Vignesh")
else:
    print("Charan")
