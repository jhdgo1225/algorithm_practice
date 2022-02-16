# 거스름돈 = n, 거스름 돈 개수 = count
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

# 500원, 100원, 50원, 10원 순으로 거스름 돈을 나누고 각 동전의 수를 count
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)