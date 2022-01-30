# 12 77 38 41 53 92 85
# 256 41
# 첫째줄에 홀수들의 합, 둘째줄에 홀수들 중 최솟값 출력

import sys
input = sys.stdin.readline
li = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        li.append(num)

if li:
    print(sum(li))
    print(min(li))

else:
    print(-1)
    
    