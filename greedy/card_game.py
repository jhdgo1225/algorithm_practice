# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 각 행의 가장 작은 수를 넣을 리스트 추가
data = []
for i in range(n): # n개의 행들에 각각 m개의 원소 입력
    sub_data = list(map(int, input().split()))
    data.append(min(sub_data)) # 각 행의 원소 중 가장 작은 수 추가

# 각 행의 가장 작은 수들 중 가장 큰 수 출력
print(max(data))
