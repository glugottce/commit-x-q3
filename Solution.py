def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result


n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

print("Single number:", find_single_number(arr))
