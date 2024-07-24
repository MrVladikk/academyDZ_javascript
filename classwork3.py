# N = 10
# i = 0
# while i <= N:
#     print(N - i)
#     i += 1


# N = 10
# summ = 0
# i = 0
# while i <= N:
#     summ += i
#     i += 1
# print(summ)


# n = 8
# p = 5
# r = 1
# while p > 0:
#     r *= n
#     p -= 1
# print(r)


# n = 1
# summ = 0
# while n <= 20:
#     if n % 2 != 0:
#         summ += n
#     n += 1
# print(summ)


# summ = 0
# n = 1
# while n <= 10:
#     if n % 2 == 0:
#         summ += n
#     n += 1
# print(summ)


# a = 10
# b = 5
# if a >= b:
#     a, b = b, a
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i)


# n = 89
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(n, fact)


# n = 5
# print("*" * n)


# n = 100
# while n < 999:
#     if n % 11 == 0:
#         print(n)
#     n += 1


# while True:
#     x = int(input("Введите первое число: "))
#     y = int(input("Введите второе число: "))
#
#     sum = x + y
#     print("Сумма чисел", x, "и", y, "равна", sum)
#
#     exit = input("Завершить ввод? (Y/y): ")
#     if exit.lower() == "y":
#         break