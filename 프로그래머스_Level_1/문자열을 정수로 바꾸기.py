def solution(s):
    answer = 0

    if len(s) >=1 and len(s) <=5 :
        answer = int(s)
    
    return answer

print(solution("1234"))