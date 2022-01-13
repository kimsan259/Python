T = int(input())
for tt in range(0, T):
    nums = list(map(int, input().split()))
    print("#%d %d" % (tt+1, round(sum(nums)/10)))