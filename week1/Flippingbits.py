#Question

def flippingBits(n):
    mask = 0xFFFFFFFF
    return n ^ mask

if __name__ == "__main__":
    q = int(input())
    results = []
    for _ in range(q):
        n = int(input())
        result = flippingBits(n)
        results.append(result)
        
    for res in results:
        print(res)
