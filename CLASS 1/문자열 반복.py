t = int(input())
for i in range(t):
    a, b = input().split()
    for x in b:
        print(int(a)* x, end='')
    print()