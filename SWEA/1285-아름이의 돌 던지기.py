for tc in range(1,int(input())+1):
    N = int(input())
    arrlist=list(map(int,input().split()))
    # print(arrlist)
    # 거리가 제일 작은 값을 찾고 그것을 센다.
    length = abs(arrlist[0])
    result = 0
    for item in arrlist:
        if length > abs(item):
            length = abs(item)
    result += arrlist.count(length)
    result += arrlist.count(-1*length)
    print("#{} {} {}".format(tc,length,result))