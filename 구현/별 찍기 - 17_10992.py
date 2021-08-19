n = int(input())

if n == 1:
    print('*')
else:
    print(' ' * (n-1) + '*')
    for i in range(n-2):
        print(' ' * (n-i-2) + '*' + ' ' * (2*i+1) + '*')
    print('*' * (2*n-1))