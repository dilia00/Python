# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


number = int(input("Введите число: "))

list_fib = []


def fibonacci_neg(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fibonacci_neg(n+2) - fibonacci_neg(n+1)


def fibonacci(num):
    if (num == 1 or num == 2):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(number-1, -1):
    list_fib.append(fibonacci_neg(i))

number *= -1
list_fib.append(0)

for j in range(1, number+1):
    list_fib.append(fibonacci(j))
print(list_fib)


# Вторй способ

number_ = int(input("Введите число: "))


def fibonacci(num):
    list_fib = [0, 1]
    num1 = 0
    num2 = 1
    i = 2
    while i <= (num * -1):
        fib = num1 + num2
        list_fib.append(fib)
        num1 = num2
        num2 = fib
        i += 1
    return list_fib


list_fibonacci = fibonacci(number_)


def fibonacci_neg(numb, list_f):
    list_fib_neg = []
    for x in range(numb, 0):
        resalt = pow((-1), (numb+1)) * list_f[x]
        list_fib_neg.append(round(resalt))
    return list_fib_neg


list_fibonacci_neg = fibonacci_neg(number_, list_fibonacci)
list_fibonacci_neg.reverse()

print(list_fibonacci_neg + list_fibonacci)
