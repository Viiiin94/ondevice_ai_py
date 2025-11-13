str = "HELLO WORLD!"

list = [1, 2, 3, 4, 5]

list2 = [[1, 2], [3, 4], [5, 6]]

list3 = [[[1], 2], [3, 4], [5, 6]]

# [1, 2]
print(list2[0])

# [1]
print(list3[0][0])

# 1
print(list3[0][0][0])

# slicing idx
print(list[0:3])
print(list[:3])
print(list[2:])

# reverse idx
print(list[-1])

# list add
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# list 더하기 list는 list가 합쳐져서 나옴
print(list_a + list_b)  # [1, 2, 3, 4, 5, 6]
print(list_a * 3)

# list 더하기 숫자는 안됨
# print(list_a + 3) # 안됨

# calculation
numb = 3
print(numb + 1)
print(numb - 1)
print(numb * 2)
print(numb / 1)  # float 형태로 나옴
print(numb % 2)
print(numb // 2)

# python에는 증감 연산자가 없음 --, ++
