x,y,z = map(int,input().split())
count=0
s=x+y
while(s<=z):
    i=1
    x=x*i
    s=s+x
    i=i+1
    count+=1
print(count) 
