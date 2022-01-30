# 10
# 40
# 30
# 60
# 30
# 출력 : 34
# 출력 : 30
numbers = []
for i in range(5):
    number = int(input())
    numbers.append(number)

average = int(sum(numbers)/5)
median = sorted(numbers)[2]

print(average)
print(median)