n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    count = 0
    for j in arr:
        if(i==j):
            count+=1
    if count == 1:
        print(i)
        break
