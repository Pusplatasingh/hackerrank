#Question
#An
def sumXor(n):
    count_of_zeros = 0
    while n > 0:
        if n & 1 == 0:  
            count_of_zeros += 1
        n >>= 1  
    return 1 << count_of_zeros 

if __name__ == "__main__":
    n = int(input())
    result = sumXor(n)
    print(result)
