def combi(n):
    return n * (n-1) // 2

n, m = map(int, input().split())

data = list(map(int, input().split()))
cnt = combi(n)

for i in range(1, m+1):
    dc = data.count(i)
    if  dc > 1:
        cnt -= combi(dc)

print(cnt)