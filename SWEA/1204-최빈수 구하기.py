from collections import Counter
 
T = int(input())
for _ in range(1,T+1):
    n = int(input())
    
    li = list(map(int, input().split()))
    most_num = Counter(li).most_common()[0][0]
    print("#"+str(n),str(most_num))