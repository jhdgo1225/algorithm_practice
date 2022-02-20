n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누었을 때 나머지가 발생하면 1번 과정 한번에 시행
    if n % k:
        result += (n % k)
        n -= (n % k)
    # N이 K로 나누어떨어질 때 2번 과정 시행
    else:
        n //= k
        result += 1
    # N이 1이면 반복문 탈출
    if n == 1:
        break

print(result) # 최종 답안 출력
