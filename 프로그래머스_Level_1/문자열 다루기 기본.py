# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, 
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
print(solution("a234"))