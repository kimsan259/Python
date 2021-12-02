L, P = map(int,input().split())
news = list(map(int,input().split()))
N = L * P
for i in range(len(news)):
    news[i] -= N
for new in news:
    print(new, end = ' ')
    
