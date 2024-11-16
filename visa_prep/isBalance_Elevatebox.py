n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    left_sum = sum(a[:i])
    right_sum = sum(a[i+1:])
    print(abs(left_sum-right_sum),end=' ')
