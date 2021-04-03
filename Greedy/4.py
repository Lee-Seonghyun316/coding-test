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

# 문제점 :
# 0번 인덱스가 3일 떄
# 2번 인덱스가 5이면
# 다시 0번부터 4번까지하고
# 4번을 확인하는데 이떄 4가 7이면
# 0부터 6까지하고
# 6이 7이면 카운트 증가


# - 모험가의 공포도보다 남은 인원수가 적으면 그 모험가부터 다음모험가들은 모험에 참여시키지 않습니다. (반복문 탈출)
# 이부분도 구현 하지 못함
count = 0
i = 0
while(i != (len(arr_sort)-1)):
    print("ii:", i)
    plus_index = arr_sort[i]-1  # 3-1 = 2
    print(plus_index)
    while(arr_sort[i+plus_index] > arr_sort[i]):  # 5>3, 7>5
        print(arr_sort[i+plus_index], ">", arr_sort[i])
        temp = plus_index  # 2 # 2
        plus_index = arr_sort[i+plus_index]-arr_sort[i]  # 5-3 # 7-5
        i += temp  # 2 # 4
        print(plus_index)
        print(i)
    count += 1
    i += plus_index
    print("i:", i)
print("count", count)

# plus_index = arr[i]-1
# group = arr[i]
# while(arr[i+plus_index] > arr[i]):
#     plus_index = arr[i+plus_index]-arr[i]
#     i += plus_index -1
#     # for j in range(i,i+plus_index):

# if arr[i+plus_index] > arr[i]:
#     i += plus_index
#     for j in range(i,len(arr)):
#         plus2_index = arr[j]-1
#         if arr[i+plus2_index] > arr[i]:
#             j += plus_index
#             for k in range(j,len(arr)):
#                 pluss3_index = arr[k]-1
#         else:
#             count += 1
#             break;
# else :
#     count += 1
