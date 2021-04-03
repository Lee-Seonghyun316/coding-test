N = int(input())  # 7

horror = input()  # 3355777
arr = []
for i in range(0, N):
    arr.append(int(horror[i]))
# arr = list(map(int, input().split()))
print(arr)
arr_sort = sorted(arr)
print(arr_sort)
print("len", len(arr_sort))

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in arr_sort:
    count += 1
    if count >= i:
        result += 1
        count = 0
        print(result)
print("result:", result)
