a, b = list(map(int,input().split()))
num2 = max(a,b)
num1 = min(a,b)
btw_num = num2 - num1 - 1

if num1 == num2 or num1 + 1 == num2:
    btw_num = 0

print(btw_num)

for m in range(num1+1, num2):
    print(m, end = ' ')