def lonelyinteger(a):
    unique = 0
    for number in a:
        unique ^= number
    return unique
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().strip().split()))
    result = lonelyinteger(a)
    print(result)
