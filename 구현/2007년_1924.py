A = ['SUN','MON','TUE','WED','THU','FRI','SAT']
B = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
X, Y = map(int,input().split())
Day = 0
for i in range(0, X-1):
 Day += B[i]
Day = (Day + Y) % 7
print(A[Day])