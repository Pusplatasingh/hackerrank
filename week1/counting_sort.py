def countingSort(arr):
    frequency = [0] * 100  
    for number in arr:
        frequency[number] += 1 
        
    return frequency

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = countingSort(arr)
    print(" ".join(map(str, result)))
