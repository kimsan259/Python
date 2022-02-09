# def solution(arr,divisor):
#     return sorted([n for n in arr if n % divisor == 0]) or [-1]
# print(solution([5,9,7,10],5))
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        if not answer:
            answer = [-1]
        answer.sort()
    return answer
print(solution([5,9,7,10],5))