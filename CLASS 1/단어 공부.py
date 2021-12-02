inputData = input().upper() # 문자열을 대문자로 변환
searchKeys = list(set(inputData)) # 중복제거함수 set()
countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))
if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])