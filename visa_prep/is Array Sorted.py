n=int(input())
arr = list(map(int,input().split()))
flag=True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        flag=False
        break
print("true" if flag else "false")
