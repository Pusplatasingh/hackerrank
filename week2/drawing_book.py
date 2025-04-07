def pageCount(n, p):
    front = p // 2
    back = (n // 2) - (p // 2)
    return min(front, from_back)

if __name__ == "__main__":
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)
