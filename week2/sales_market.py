#Question
#
def sockMerchant(n, ar):
    from collections import Counter
    color_count = Counter(ar)
    return sum(count // 2 for count in color_count.values())

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(sockMerchant(n, ar))
