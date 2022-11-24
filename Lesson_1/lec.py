print("привет, мир")

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)


# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.


namber1 = int(input("Введите число"))
namber2 = int(input("Введите второе число"))
if namber1 == namber2 * namber2:
    print("Да")
elif namber2 == namber1 * namber1:
    print("Да")
else:
    print("Нет")

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = [5, 17, -2, 0, 2]
max_ = a[0]

for i in a:
    if i > max_:
        max = i

print(max_)


# range(start, stop, step)
# range(5) -> [0, 1, 2, 3, 4]
# range(2, 5) -> [2, 3, 4]
# range(1, 7, 2) -> [1, 3, 5]


# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N


num = int(input("Введите число: "))
for i in range(-num, num+1):
    print(i, end=' ')

num = int(input("введите число: "))
print(*range(-num, num + 1))


# 4. Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.

n = float(input("Введите число: "))
if int(n) == n:
    print('нет')
else:
    print(int(n * 10) % 10)

# '6,78' -> ['6', '78'] -> '78' -> '7'
n = input('Input number: ')
print(n.split(',')[1][0])


# 5.Задача Написать программу, которая на вход принимает число и проверяет кратоно ли оно 5 и 10 или 15, но не 30.
x = int(input('--> '))
if (((x % 5 == 0) and (x % 10 == 0)) or (x % 15 == 0)) and (x % 30 != 0):
    print(True)
