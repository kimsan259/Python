S = input()
ans = [0 for _ in range(26)]
for i in S:
    ans[ord(i)-97] += 1
for k in ans:
    print(k, end = ' ')