# # 1:
# def vivod(name = []):
#     print("Hello", name, end="!\n\")
# name = input("Введите своё имя: ")
# vivod(name)
import time

# # 2:
# i1 = int(input("Введите первое число: "))
# i2 = int(input("Введите второе число: "))
# i3 = int(input("Введите третье число: "))
# i1 += i2
# print("Сумма чисел: ",i1 + i3, "\n")

# 3:
# def deleniye(skol, yabloki):
#     print("Досталось: ", yabloki // shkol, "\nОсталось: ", yabloki % shkol, "\n")
#
# shkol = int(input("Введите число школьников: "))
# yabloki = int(input("Введите число яблок: "))
# deleniye(shkol, yabloki)

# # 4
# def ryad(chislo):
#     print("Следуюшее число для", chislo, " - ", chislo + 1, "\nПредыдушее число для", chislo, " - ", chislo - 1, "\n")
# chislo = int(input("Введите число: "))
# ryad(chislo)

# 5:
# def vivod:
#     print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\tUp above the world so high,\n\t\t\tLike a dimond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!\n")

# # 6:
# def vozmojnost(dengi, quant, price, towar):
#     if dengi >= quant * price:
#         print("У меня есть", dengi, "единиц, поэтому я смогу купить", quant, tovar, "за", quant * price, "единиц.\n")
#     else:
#         print("У меня не хватает денег!!!\n")
#
# dengi = int(input("TotalMoney: "))
# quant = int(input("Quantity: "))
# price = int(input("Price: "))
# tovar = input("Nazvaniye tovara: ")
# vozmojnost(dengi, quant, price, tovar)

# # 1:
# def vozrast(voz):
#     if voz <= 18:
#         print("Вам нужно учиться!\n")
#     elif voz <= 50:
#         print("Вам нужно работать!\n")
#     elif voz <= 59:
#         print("Вам скоро на работу!\n")
#     elif voz <= 110:
#         print("Вы пенсионер\n!")
#     else:
#         print("Вы не эльф!!!\n")
# voz = int(input("Введите свой возраст: "))
# vozrast(voz)

# # 2:
# def opredeleniyemesyaca(chislo):
#     if chislo == 1:
#         print("Месяц: Январь; Число дней: 31\n")
#     elif chislo == 2:
#         print("Месяц: Февраль; Число дней: 28\n")
#     elif chislo == 3:
#         print("Месяц: Март; Число дней: 31\n")
#     elif chislo == 4:
#         print("Месяц: Апрель; Число дней: 30\n")
#     elif chislo == 5:
#         print("Месяц: Май; Число дней: 31\n")
#     elif chislo == 6:
#         print("Месяц: Июнь; Число дней: 30\n")
#     elif chislo == 7:
#         print("Месяц: Июль; Число дней: 31\n")
#     elif chislo == 8:
#         print("Месяц: Август; Число дней: 31\n")
#     elif chislo == 9:
#         print("Месяц: Сентябрь; Число дней: 30\n")
#     elif chislo == 10:
#         print("Месяц: Октябрь; Число дней: 31\n")
#     elif chislo == 11:
#         print("Месяц: Ноябрь; Число дней: 30\n")
#     elif chislo == 12:
#         print("Месяц: Декабрь; Число дней: 31\n")
#     elif chislo == 13:
#         print("Вы не в Эфиопии!!!\n")
#     elif chislo > 13:
#         print("Вы не в паралельной вседенной!!!\n")
# chislo = int(input("Введите номер месяца: "))
# opredeleniyemesyaca(chislo)

# 3:
# def sovpadeniya(i1, i2, i3):
#     if not (i1 == i2 and i1 == i3):
#         print("Число совпадений: 0\n")
#     elif i1 == i2 and i1 == i3:
#         print("Число совпадений: 3\n")
#     else:
#         print("Число совпадений: 2\n")
# i1 = int(input("Введите первое число: "))
# i2 = int(input("Введите второе число: "))
# i3 = int(input("Введите третье число: "))
# sovpadeniya(i1,i2,i3)
#
# def usloviya(ch1, ch2):
#     if ch1 * ch2 < 1000:
#         print("Результат:", ch1 * ch2, "\n")
#     else:
#         print("Результат:", ch1 + ch2, "\n")
# ch1 = int(input("Введите первое число: "))
# ch2 = int(input("Введите второе число: "))
# usloviya(ch1,ch2)

# 5:
# def usloviye1(ch):
#     if ch % 5 == 0:
#         print("Hello!!!\n")
#     else:
#         print("Bye!!!\n")
# ch = int(input("Введите число: "))
# usloviye1(ch)

# 6:
# def vesokosnost(god):
#     if god % 400 == 0 or god % 4 == 0:
#         print("Весокосный!")
#     elif god % 100 != 0:
#         print("Обычный!")
# god = int(input("Введите год: "))
# vesokosnost(god)

#1
# def pyaterka(spisok):
#     length = len(spisok)
#     spisok1 = []
#     spisok2 = []
#     for i in range(length):
#         if int(spisok[i]) <= 5:
#             a = spisok[i]
#             spisok1.append(a)
#             print("Меньше 5:", spisok1, end=", ")
#         else:
#             a = spisok[i]
#             spisok2.append(a)
#             print("Больше 5:", spisok2, end=", ")
# spisok = input("Введите числа: ").split(", ")
# pyaterka(spisok)

# 2
# def list1(name, surname, age):
#     list1 = []
#     list1.append([name, surname, age])
#     print("Ваше имя, фамилия, возраст: "list1)
# name, surname, age = input("Введите своё имя, фамилию и отчество").split()

#3
# def spitej(spisokchisel = []):
#     print("Список: [", ", ".join(list(spisokchisel)), end = "]\n")
#     print("Картеж: (", ", ".join(list(spisokchisel)), end = ")")
# spisokchisel = input("Введите список чисел: ").split(", ")
# spitej(spisokchisel)

#4
# def slojeniye(slojeniye):
#     summa = 0
#     for i in slojeniye:
#         summa += int(i)
#     print(summa)
# slojeniye = input("Введите сумму: ").split("+")
# slojeniye(slojeniye())

# print(eval(input())) # eval - все мат функции

#6
# def kvadrat(spisok1):
#     spisok2 = []
#     for i in range(0, len(spisok1) + 1):
#         a = int(i) * int(i)
#         spisok2.append(a)
#         print(spisok2[i], end=", ")
# spisok1 = input("Введите числа: ").split()
# kvadrat(spisok1)

# 1
# def spiskiblud(moyspisokblud):
#     spisokbludmoegodruga = moyspisokblud
#     if moyspisokblud == spisokbludmoegodruga:
#         moyspisokblud1 = input()
#         spisokbludmoegodruga1 = input()
#         print("Мой список блюд:", moyspisokblud, moyspisokblud1, "\nСписок блюд моего друга:", spisokbludmoegodruga, spisokbludmoegodruga1)
#     else:
#         print("Мой список блюд:", moyspisokblud, "\nСписок блюд моего друга:", spisokbludmoegodruga)
# moyspisokblud = input("Введите список блюд через запятую: ").lower()
# spiskiblud(moyspisokblud)
#
# # 2
# def spumma(ser_num):
#     print("Сумма:", sum(range(1, user_num + 1)), "\nСписок:", list(range(user_num + 1)))
# ser_num = int(input("Введите число: "))
# spumma(ser_num)
#
# # # 3
# # print("\t0-100 чётные:",list(range(0,101,2)),"\n\t0-100 нечётные",list(range(1,100,2)),"\n\tСписок",sum(range(0,101)))
#
# # 4
# def slist(list1):
#     for i in list1:
#         if i == 815:
#             break
#         elif i % 2 == 0:
#             print(i)
# list1 = [1, 2, 3, 5, 6, 8, 815, 44, 5, 7, 88]
# slist(list1)
#
# # # 5
# # ?chislo = int(input("Введите число: "))
# # ktsifr = 0
# # while chislo > 0:
# #     chislo //= 10
# #     ktsifr += 1
# # print(ktsifr)?
# # print(len(input())
#
# # print(len(input))
#
# # 6
# chislo = int(input("Введите число: "))
# for i in range (2, chislo):
#     if chislo % i == 0:
#         print("Составное!")
#         break
#     else:
#         i += 1
# else:
#     print("Простое!")

# 2
# def procenti(P, r, n, t):
#     for i in range(1, t + 1):
#         A = P * ((1 + r / n) ** (n * t))
#         print(i, "Год", A, "- стоимость")
# P = int(input("Начальная цена вклада = "))
# r = int(input("Годовой процент = ")) / 100
# n = int(input("Учёт процентов за год - "))
# t = int(input("Количество лет - "))
# procenti(P,r,n,t)
#
# # 3
# def vivodsusloviyami(spisok):
#     for i in spisok:
#         if int(i) > 500:
#             break
#         elif int(i) > 150:
#             continue
#         elif int(i) % 5 == 0:
#             print(i, end=", ")
#
# spisok = input("Введите список чисел: ").split()
# vivodsusloviyami(spisok)
#
# # 4
# def Fibonnachi(razmerryada):
#     ryadFibonachi = [0, 1]
#     nach = 0
#     while nach < razmerryada:
#         ryadFibonachi.append(ryadFibonachi[nach] + ryadFibonachi[nach + 1])
#         nach += 1
#     print("Последовательность Фибоначчи: ", ryadFibonachi)
# razmerryada = int(input("Введите размер ряда Фиббоначи: "))
# Fibonnachi(razmerryada)

# 1
# def magazine(prduct_list = []):
#     pass
#     while True:
#         commanda = input("Введите команду\n\t"
#         "add: Добавить продукт на склад\n\t"
#         "delete: Удалить продукт со складаn\n\t"
#         "list: Список продуктов\n\t"
#         "search: Найти продукт\n\t"
#         "stop: Остановить поиск\n\t"
#         "clear: Очистить склад\n\nВвод: ").lower()
#         if commanda == "add":
#             product_name = input("Введите название продукта: ")
#             if product_name in products_list:
#                 print("Продукт на складе!")
#                 continue
#             products_list.append(product_name)
#             print("Добавил успешно!")
#         elif commanda == "list":
#             if not products_list:
#                 print("Продуктов нет")
#                 continue
#             else:
#                 print(", ".join(products_list))
#         elif commanda == "delete":
#             product_name = input("Введите название продукта: ")
#             if product_name not in products_list:
#                 print("Продукта нет на складе")
#                 continue
#             products_list.remove(product_name)
#             print("Удалил успешно!")
#         elif commanda == "search":
#             name = input("Введите название продукта: ")
#             if not products_list:
#                 print("Нечего искать!")
#                 continue
#             else:
#                 for i in products_list:
#                     if name == products_list(i):
#                         print(product_name, ": ", i)
#                         continue
#         elif commanda == "clear":
#             if len(products_list) == 0:
#                 print("Склады пусты!!!")
#                 continue
#             else:
#                 for i in range(len(products_list)):
#                     products_list.clear()
#         elif commanda == "stop":
#             break
#         else:
#             print("Такой функции нет!!!")
#             continue
#     print("Операция завершена!!!")
# products_list = []
# magazine(products_list)

# 1
# def dicts(dicts = {}):
#     for i in range(1, 6):
#         dict1 = {i: i ** 2}
#         dicts = dicts | dict1
#     print(dicts, end=", ")
#     print("\n\n")
# dicts = {}
# dicts(dicts)
#
# # 2
# def dictsloj(dict4):
#     srarif = 0
#     for values in dict4.values():
#         srarif += int(values)
#     print(srarif / len(dict4))
# dict2 = ()
# dict2 = input("Введите имена участников через запятую: ").split(",")
# dict3 = []
# dict3 = input("Введите возраст участников через запятую: ").split(",")
# print("Ваш сроварь:")
# dict4 = dict(zip(dict2, dict3))
# dictsloj(dict4)
#
# # 3
# def dictsup(keys, values):
#     print("Ваш словарь", dict(zip(keys, values)))
# keys = input("Введите ключи через запятую: ").split(",")
# values = input("Введите значения через запятую: ").split(",")
# dictsup(keys, values)
#
# # 4
# def distance(cities = {}):
#     moscow = cities['Moscow']
#     london = cities['London']
#     paris = cities['Paris']
#     dist1 = ((int(moscow[0]) - int(london[0])) ** 2 + (int(moscow[1]) - int(london[1])) ** 2) ** 0.5
#     dist2 = ((int(london[0]) - int(paris[0])) ** 2 + (int(london[1]) - int(paris[1])) ** 2) ** 0.5
#     dist3 = ((int(moscow[0]) - int(paris[0])) ** 2 + (int(moscow[1]) - int(paris[1])) ** 2) ** 0.5
#     distances = {
#         'moscow-london': dist1,
#         'moscow-paris': dist2,
#         'london-paris': dist3
#     }
#     print("Словарь:", distances)
# cities = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480)
# }
# distance(cities)

# # 1
# def poiskmax(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > c and b > a:
#         return b
#     elif c > a and c > b:
#         return c
#     elif a == b == c:
#         print("Все числа равны!")
#     return a
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print(poiskmax(a, b, c))

# # 2
# def summachiselvspiske(spisok = []):
#     summa = 0
#     for i in spisok:
#         summa += int(i)
#     print("Ваша сумма = ", end = " ")
#     return summa
#
# spisok = []
# spisok = input("Введите список через запятую: ").split(",")
# print(summachiselvspiske(spisok))

# # 3
# def summachiselvspiske(spisok = []):
#     summa = 1
#     for i in spisok:
#         summa *= int(i)
#     print("Ваша сумма = ", end = " ")
#     return summa

# spisok = []
# spisok = input("Введите список через запятую: ").split(",")
# print(summachiselvspiske(spisok))

# # 4
# def perevorotstrok(stroka = ""):
#     for i in range(0, len(stroka)):
#     return stroka
#
# stroka = input("Введите строку: ")
# print(perevorotstrok(stroka))

# # 5
# def factorial(chislo1):
#     fact1 = 1
#     x = 2
#     while x < chislo1 + 1:
#         fact1 *= x
#         x += 1
#     return fact1
#
# chislo = int(input("Введите число: "))
# print(factorial(chislo))

# # 6
# def definer(stroka = ""):
#     bukvaupper = 0
#     bukvalower = 0
#     for bukva in stroka:
#         if bukva.isupper():
#             bukvaupper += 1
#             continue
#         bukvalower += 1
#         elif bukva.islower():
#             bukvalower += 1
#     print("Число букв в верхнем регистре:", bukvaupper)
#     print("Число букв в нижнем регистре:", bukvalower)
#
# stroka = input("Введите строку: ")
# definer(stroka)

# # 7
# def palindrom(stroka = []):
#     stroka1 = stroka[::-1]
#     if stroka == stroka1:
#         print(True)
#     else:
#         print(False)
#
# stroka = input("Введите числа через запятую: ").split(",")
# palindrom(stroka)

# # 8
# def bank(vklad, kolvolet, kolvouchyotov):
#     procent = 10 / 100
#     for i in range(1, kolvolet + 1):
#         itog = vklad * (1 + procent / kolvouchyotov) ** (kolvouchyotov * i)
#         print(i, "- Год", "%.2f" % itog, "- Рублей")
#         # print(i, "- Год", format(% itog.f2), "- Рублей")
#
# vklad = int(input("Введите сумму вклада: "))
# kolvolet = int(input("Введите срок: "))
# kolvouchyotov = int(input("Сколько раз учитывать: "))
# bank(vklad, kolvolet, kolvouchyotov)

# # 9
# def izvlecheniye(spisokchisel = []):
#     listnumeral = []
#     for i in spisokchisel:
#         if int(i) % 15 == 0:
#             listnumeral.append(i)
#     return listnumeral
#
# listofnumels = input("Введите число: ").split(",")
# print(izvlecheniye(listofnumels))

# 1
# def summutsifr(chislo):
#     summa = 0
#     while chislo > 0:
#         summa += (chislo % 10)
#         chislo //= 10
#     print("Итого:", summa)
#     return summa
#
# chislo = int(input("Введите число: "))
# summutsifr(chislo)
#
# # 2
# def time(chilsosekund):
#     minuts = chilsosekund // 60
#     chilsosekund -= minuts * 60
#     hours = minuts // 60
#     minuts -= hours * 60
#     days = hours // 24
#     hours -= days * 24
#     print("Дни -", days, "\tЧасы -", hours, "\tМинуты -", minuts, "\tСекунды -", chilsosekund, "\n\n")
#
# chislosecund = int(input("Введите число секунд: "))
# time(chislosecund)

# urok 10
# urok 11
# def check_nums(num: Union[int, float, bool]): return num >= 20
#
# my_func = lambda num: num >= 20
# my_func()
DCUE = 0
# 1
# def firstUp(names = []):
#     stringof = ""
#     for i in range(len(names)):
#         stringof = str(i)
#         names.pop(names[i])
#         names += stringof.upper()
#     print(names)
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# firstUp(names)

# # 2
# def score_75(listof = []):
#     for i in listof:
#         if int(i) > 75:
#             print(i, end=", ")
#
# filter_nums = [11, 68, 94, 55, 88, 60, 90, 99]
# score_75(filter_nums)

# # 3
# def palind(list1 = ''):
#     for i in list1:
#         if i.lower() == i[::-1].lower():
#             print(i)
#         else:
#             continue
#
# list1 = ['Anna', 'kazak', 'Alla', 'roma', 'Starkiller']
# palind(list1)

# # 5
# def lengthof(list1 = []):
#     k = ""
#     for i in list1:
#         k += str(len(i))
#         k += " "
#     print(k)
#
# list1 = ['apple', 'banana', 'orange']
# lengthof(list1)

# # 4
# def createList(n):
#     list1 = []
#     for i in range(1, n + 1):
#         list1.append(i)
#     start = time.time()
#     print(list1, "\n\n", len(list1), "\n\n", time.time() - start)
#
# n = int(input("Введите число: "))
# createList(n)

# 6
# def UniON(list1 = [], list2 = []):
#     list3 = ""
#     for i in list2:
#         list3[i] += list1 | list2
#     print(list3)
#
# list1 = ['banana', 'apple', 'cherry']
# list2 = ['orange', 'lemon', 'pineapple']
# UniON(list1, list2)

# urok 12

