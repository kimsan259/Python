case = int(input())

dp = [0,0,1,1]

# dp[n] = min(dp[n-1] , dp[n//2], dp[n//3) + 1
for i in range(4, case+1):
    dp.append(dp[i-1]+1)
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[case])