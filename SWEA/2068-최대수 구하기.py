# 1
# 3 17 1 39 8 41 2 32 99 2 / #1 99
T = int(input())
for i in range(T):
    nums = list(map(int,input().split()))
    print("#"+str(i+1),str(max(nums)))