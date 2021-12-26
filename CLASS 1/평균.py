# 자기점수 중 최댓값 M을 고르고 모든 점수를 점수/M*100 으로 고친다

n = int(input())
test_list = list(map(int,input().split()))
max_score = max(test_list)
new_list = []
for score in test_list:
    new_list.append(score/max_score*100) # 새로운 점수 생성
test_avg = sum(new_list)/n
print(test_avg)