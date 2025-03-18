
def calculate_ratios(arr):
    pos=0     
    neg=0    
    zero=0     
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    n = len(arr)
    pos_r = pos / n
    neg_r= neg/ n
    zero_r = zero/ n

    return pos_r, neg_r, zero_r

def print_ratios(pos_r, neg_r, zero_r):
    print(f"{pos_r:.6f}")
    print(f"{neg_r:.6f}")
    print(f"{zero_r:.6f}")

n = int(input())
arr = list(map(int, input().split()))

pos_r, neg_r, zero_r = calculate_ratios(arr)
print_ratios(pos_r, neg_r, zero_r)
