def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0 :
        return (sqrt+1)**2
    return -1

print("결과 : {}".format(solution(121)));