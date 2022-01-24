number = int(input())
list = []

for i in range(1, number+1):
    if number % i == 0:
        list.append(i)
    
for j in list:
    print(j, end = ' ')