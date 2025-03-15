def find_number(arr):
    re = 0
    for num in arr:
        re ^= num
    return re

n = int(input().strip())
arr = list(map(int, input().strip().split()))
no = find_number(arr)
print(no)