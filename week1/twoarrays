#Question: Two Arrays(A,B) 

#Answer 

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    return "YES" if all(a + b >= k for a, b in zip(A, B)) else "NO"

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(twoArrays(k, A, B))
