n,x,y = map(int,input().split())
for i in range(n): 
    if i*x==y: 
        print("YES")
        break
else : 
    print("NO")
