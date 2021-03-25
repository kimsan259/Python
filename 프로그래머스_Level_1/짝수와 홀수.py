def solution(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + solution(3))
print("결과 : " + solution(2))