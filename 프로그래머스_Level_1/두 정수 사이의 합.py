#def solution(a,b):
#    return (a+b)*(abs(b-a)+1)//2
def solution(a,b):
    return sum(range(min(a,b),max(a,b)+1))
print(solution(3,5))