# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# data(리스트) 정렬
data.sort()

# data 변수 안의 첫 번째로 큰 수
first = data[n-1]

# data 변수 안의 두 번째로 큰 수
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
    if m == 0:
        break
    result += second
    m -= 1

print(result)