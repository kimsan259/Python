def solution(arr,divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
print(solution([5,9,7,10],5))