def solution(arr):
    if len(arr) > 1:
        arr.remove((min(arr)))
        return arr
    else:
        return [-1]
arr = [4,3,2,1]
print("결과 {} ".format(solution(arr)))