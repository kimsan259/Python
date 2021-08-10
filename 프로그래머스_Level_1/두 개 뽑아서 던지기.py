# 정수 배열 numbers가 주어진다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성하라
# [2,1,3,4,1] // [2,3,4,5,6,7]
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))
print("결과 : {}".format(solution([2,1,3,4,1])))