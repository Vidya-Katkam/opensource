n=int(input())
s=input()
t=input()
a={}
b={}
for i in s:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
for j in t:
    if j in b:
        b[j]+=1
    else:
        b[j]=1
flag=True
if sorted(a.values()) == sorted(b.values()):
    print("true")
else:
    print("false")
