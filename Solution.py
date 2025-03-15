def single(a):
    r = 0
    for x in a:
        r ^= x
    print(r)

n = int(input())
a = list(map(int, input().split()))
single(a)
