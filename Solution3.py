n=int(input());arr=[int(i) for i in input().strip().split()]
for i in arr:
    if arr.count(i)==1:
        print(i);exit()
