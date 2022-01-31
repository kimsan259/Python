arr = [i for i in range(0,21)]

for _ in range(10):
    a, b = map(int,input().split())
    b += 1
    arr_ = arr[:a] + arr[a:b][::-1] + arr[b:]
    arr = arr_

print(' '.join(map(str,arr[1:]))) 