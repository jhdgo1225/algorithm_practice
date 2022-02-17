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
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)