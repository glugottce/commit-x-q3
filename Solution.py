n= int(input())
a=list(map(int,input().split()))
flag=0
res=[]
for i in a:
    va=a.count(i)
    if va==1 and i not in res:
        res.append(i)
    flag=1
if flag==0:
    print(-1)
else:
    print(*res)