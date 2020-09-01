def square(h, n):
    try:
        int(h)
        int(n)
    except:
        raise IndexError
    slist = [int(h), int(n)]
    result = slist[0] * slist[1]
    return result