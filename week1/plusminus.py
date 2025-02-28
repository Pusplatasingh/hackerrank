#Question 

#Answer
def calculate_ratios(arr):
    pos=0     # pos=count of +ve no
    neg=0    # neg=count of -ve no
    zero=0     # zero=count of 0s
# check no. of positive negative and zero present in array
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
# n is total no. of element
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
