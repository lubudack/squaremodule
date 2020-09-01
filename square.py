import time
def square(h, n):
    try:
        int(h)
        int(n)
    except:
        raise IndexError
    slist = [int(h), int(n)]
    result = slist[0] * slist[1]
    return result
def age(n):
    try:
        int(n)
    except:
        raise IndexError
    result = int(time.strftime('%Y', time.localtime(time.time()))) - int(n) + 1
    return result
    