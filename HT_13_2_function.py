# Напишите функцию, которая создает список случайных элементов. На вход функция
# принимает кол-во элементов, минимальное и максимальное значение
# import random
#
# n = int(input())
# min_el = int(input())
# max_el = int(input())
#
# def rand_nums(n, min_el, max_el):
#     lst = []
#     for i in range(n):
#         lst.append(random.randint(min_el, max_el))
#     return(lst)
#
#
# print(rand_nums(n, min_el, max_el))

# Напишите функцию, вычисляющую значение факториала числа N.
# Используйте рекурсию

# x = int(input())
#
# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
#
# print(fact(x))


# Преобразуйте задачу с покупкой торта из экзамена 2 в функцию.

pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'мед'], 4, 1025],
          'киевский': [['сахар', 'фундук', 'масло'], 5, 985]}

buy = input('Какой торт Вы хотели бы приобрести: ').lower()
look = input('Что Вы хотели бы уточнить: ').lower()

def func_for_pastry(buy, look):
    for k, v in pastry.items():
        if k == buy:
            if look == "описание":
                return f"торт {k} состоит из {v[0]}"
            elif look == "цена":
                return f"торт {k} стоит рублей {v[1]}"
            elif look == "количество":
                return f"торта {k} осталось грамм {v[-1]}"
            elif look == "купить":
                gr = int(input("Сколько торта Вам положить: "))
                return f"к оплате {v[1] * gr / 100}, торта {k} осталось грамм {v[-1] - gr}"


print(func_for_pastry(buy, look))
