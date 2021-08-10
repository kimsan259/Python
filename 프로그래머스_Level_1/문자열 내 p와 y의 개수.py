def solution(s):
    return s.lower().count('P') == s.lower().count('Y')
    
print("결과:{}".format(solution("pPoooyY")))