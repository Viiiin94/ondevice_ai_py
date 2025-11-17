def add(x, y):
    return x + y


def sayHello():
    return "Hello world!"


def sayGoodbye():
    print("Good bye!")


def function_tuple(*wargs):
    print(type(wargs))
    print(wargs)


function_tuple(1, 2, 3, 4, 5, 6)


def function_dict(**kwargs):
    print(type(kwargs))
    print(kwargs)


function_dict(name="yyb", age=18, gender="Male")

a = input("더할 첫 숫자 입력 : ")
b = input("두 번째 숫자 입력 : ")
print(a + b)  # 문자열끼리의 합
print(int(a) + int(b))  # 정수로 치환해서 합쳐야 더해짐

# 먼저 치환해도 됨
a1 = int(input("더할 첫 숫자 입력 : "))
b1 = int(input("두 번째 숫자 입력 : "))

print("a", "b", "c", sep=" ")  # default가 띄어쓰기
print(a, b)

for i in range(10):
    print(i, end=' ')  # default가 \n 지금은 띄어쓰기

for i in range(10):
    print(i, end='\n')

f = open("새파일.txt", 'w')
f.close()
