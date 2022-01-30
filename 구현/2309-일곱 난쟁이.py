array = []
sum = 0

for i in range(9):
    array.append(int(input()))
    sum += array[i]
    
for j in range(9):
    for k in range(9):
        if sum - (array[j] + array[k]) == 100 and j != k:
            remove = {array[j], array[k]}

result = [m for m in array if m not in remove]
for m in sorted(result):
    print(m)