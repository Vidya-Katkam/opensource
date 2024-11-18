n=int(input())
l=[]
for i in range(n):
    k=list(map(int,input().split()))
    l.append(k)
r=[]
s=0
for i in range(n): 
    for j in range(n): 
        s+=l[i][j]
        s+=l[j][i]
    r.append(s)
    s=0
for i in r:
    print(i,end=' ')
