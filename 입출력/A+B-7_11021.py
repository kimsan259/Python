T = int(input())

num = 1

for i in range(T):
    A, B = map(int, input().split())
    print("Case #%s : %s" % (num, A+B))
    num += 1