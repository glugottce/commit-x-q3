def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num 
    return result

n = int(input()) 
arr = list(map(int, input().split()))  

print(find_single_number(arr))
