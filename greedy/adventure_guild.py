N = int(input())
mohum = list(map(int, input().split()))
count = 0  # 총 그룹 수

# 모험가 집단 내림차순 => 공포도가 큰 모험가 순서
mohum.sort(reverse=True)

while True:
    big = mohum[0]  # 공포도가 가장 큰 모험가
    mohum = mohum[big:]  # 조건에 따라 그룹 결성 후 슬라이싱
    count += 1  # 그룹 수 증가
    # 모든 모험가들이 그룹을 결성을 했거나 공포도가 큰 모험가의 조건을 충족하기 어려운 경우 탈출
    if len(mohum) == 0 or len(mohum[:big]) != big :
        break

print(count)  # 총 그룹수 출력

#################################################################
N = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0  # 현재 그룹에 포함된 모험가의 수
result = 0  # 총 그룹 수



for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 포험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹 수 증가
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹수 출력
