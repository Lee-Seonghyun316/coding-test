string_num = input()

list_num = list(string_num)

list_new = []

for i in range(0, len(list_num)):
    list_new.append(int(list_num[i]))


print(list_new)
result = 0

for i in range(0, len(list_new)):
    # if 조건 수정
    if list_new[i] <= 1 or result <= 1:
        result += list_new[i]
    else:
        result *= list_new[i]

print(result)
