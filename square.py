import time
def square(h, n):
    try:
        int(h)
        int(n)
    except:
        raise IndexError
    slist = [int(h), int(n)]
    result = slist[0] * slist[1]
    realresult = str(result) + "가 사각형의 넓이입니다."
    return realresult #출력
def age(n):
    try:
        int(n)
    except:
        raise IndexError
    result = int(time.strftime('%Y', time.localtime(time.time()))) - int(n) + 1
    realresult = str(result) + "살입니다."
    return realresult #출력
h = input("세로값:")
n = input("가로값:")
print(square(int(h), int(n)))
n = input("생년월일:")
print(age(int(n)))
    
