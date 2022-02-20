def solution(array, commands):
    answer = []
    # commands에 있는 command(i, j, k)를 뽑는다.
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j] # array에서 슬라이스를 하고
        slice.sort() # 정렬하고
        answer.append(slice[k-1]) # 인덱싱하자

    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))