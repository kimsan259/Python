num = input()
num = int(num)
result = 0
for i in range(0,num):
    result += num % 10
    num //= 10
print(result)