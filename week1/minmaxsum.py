def miniMaxSum(arr):
    total_sum = sum(arr)

    min_value = min(arr)
    max_value = max(arr)
    
    min_sum = total_sum - max_value
    max_sum = total_sum - min_value
    
    print(min_sum, max_sum)


input_data = input()  
arr = list(map(int, input_data.split())) 
miniMaxSum(arr)  
