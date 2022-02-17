n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
mini = 1

while True:
    a = mini
    for i in data:
        if a - i < 0:
            continue
        a -= i
        if a == 0:
            mini += 1
            break
    if a > 0:
        print(mini)
        break
########################################################