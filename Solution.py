def findSingleNumber(arr):
    count = {} 
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    for num in arr:
        if count[num] == 1: 
            return num

n = int(input()) 
arr = list(map(int, input().split()))  
print(findSingleNumber(arr)) 
