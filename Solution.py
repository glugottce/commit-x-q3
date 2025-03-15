def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

N = int(input())
arr = list(map(int, input().split()))
print(single_number(arr))
 
