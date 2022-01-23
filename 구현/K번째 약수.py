# 두 개 자연수 n, k n의 약수들 중 k번째로 작은 수 를 출력
# 만일 n의 약수의 개수가 k개보다 적어서 k번째 약수가 존재하지 않을경우 -1을 출력 
# 6 3 / 3
import sys
n , k = map(int,input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)