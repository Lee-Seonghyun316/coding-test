N, K = map(int, input().split())
print(N, K)

count = 0

while N > 1:
    if N % 2 == 0:
        if K % 2 == 0:
            N /= K
            count += 1
        else:
            N -= 1
            count += 1
    else:
        if K % 2 == 0:
            N -= 1
            count += 1
        else:
            if N % K == 0:
                N /= K
                count += 1
            else:
                N -= 1
                count += 1

print(count)
