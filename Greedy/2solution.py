# N, K를 공백 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 뺴기
    target = (n // k) * k  # 소수점 이하 버리는 나눗셈 연산
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나누지 못하면) 반복문 탈출

    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (n - 1)
print(result)
