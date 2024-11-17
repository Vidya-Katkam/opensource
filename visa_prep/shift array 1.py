n=int(input())
arr=list(map(int,input().split()))
k=arr[0]
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
arr[n-1]=k
for i in arr: 
    print(i,end=' ')
