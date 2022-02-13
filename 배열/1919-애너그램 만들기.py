la = [0] * 26
lb = [0] * 26
a = input()
b = input()
for i in a:
    la[ord(i)-97] += 1
for j in b:
    lb[ord(j)-97] += 1
cnt = 0
for i in range(26):
    if la[i] or lb[i]:
        cnt += abs(la[i] - lb[i])
print(cnt)