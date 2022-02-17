data = input()
prev = int(data[0])

if len(data) > 1:
    for i in data[1:]:
        # 문자열의 인덱스 1번 위치부터 한 글자씩 바로 이전 글자와의 
        # 덧셈과 곱셈 결과 중 더 큰 결과를 선택
        summary = prev + int(i)
        multiply = prev * int(i)
        if summary > multiply:
            result = summary
        else:
            result = multiply
        prev = result

print(result)
########################################################
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)