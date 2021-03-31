N = int(input())

arr = list(map(int, input().split()))
arr.sort()
print(arr)

count = 0
for i range(0, len(arr)):
    plus_index = arr[i]-1
    if arr[i+plus_index] > arr[i]:
        plus2_index = arr[i+plus_index]-1
