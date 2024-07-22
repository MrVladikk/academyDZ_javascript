# A = int(input("введите число "))
# if A >= 0:
#     print(A + 1)
# else:
#     print(A)


# speed = 80
# if speed >= 130 :
#     print("вы нарушили")
# else:
#     print("скорость в пределах нормы ")


# A = int(input("число А "))
# B = int(input("число В "))
# if A == B or B == A:
#     A = A + B
#     B = (B + A) - B
#     print(A,B)
# else:
#     A = 0
#     B = 0
#     print(A,B)



# user_data = -4
# if user_data == 5:
#     print("A")
# else:
#     if user_data == 4:
#         print("B")
#     else:
#         if user_data == 3:
#             print("C")
#         else:
#             if user_data == 2:
#                 print("D")
#             else:
#                 if user_data == 1:
#                     print("E")
#                 else:
#                     if user_data ==0:
#                         print("F")
#                     else:
#                         print("ERROR")


# time = 6
# ticket = 0
# money = 0
# luggage = 0
# if 6 <= time <= 24 and (money or ticket):
#     if luggage == 0:
#         print("можно ехать")
#     else:
#         print("есть багаж")
# else:
#     print("время вышло или нет денег или нет белета ")



# T = 200
# if T < 5:
#     print("холодно")
# else:
#     if T >= 5 and T < 20  :
#         print("на улице прохладно")
#     else:
#         if T >= 20:
#             print("на улице тепло")


# m = 85
# h = float(1.8)
# I = m/h**2
# if I >=18 and I < 26:
#     print(f"начение в норме {I} ")
# else:
#     if I < 18:
#         print(f"значение меньше нормы {I}")
#     else:
#         if I > 25:
#             print(f"значение больше нормы {I} ")


# a = 1
# b = 1
# c = 1
# D = b**2 - 4*a*c
# if D==0:
#     x= -b /(2*a)
#     print(f"D=0=>x={x}")
# elif D > 0:
#     x1 = -b + D**0.5 /(2*a)
#     x2 = -b - D**0.5 /(2*a)
#     print(f"D>0=>x1={x1: .2f}, x2={x2: .2f}")
# else:
#     print("корней нет ")


# summ = 25000
# if summ== 0 <= 5000:
#     dis = 0.05
# elif summ == 5000 <= 15000:
#     dis = 0.12
# elif summ == 15000 <= 25000:
#     dis = 0.20
# else:
#     dis = 0.30
# summdis = summ*dis
# fsum = summ - summdis
# print(f"скидка:{summdis}")
# print(f"сумма с учетом скидки:{fsum}")


# year = 2024
# if (year %4 ==0 and year %100 !=0) or (year %100 == 0):
#     print("год високосный ")
# else:
#     print("год не високосный")