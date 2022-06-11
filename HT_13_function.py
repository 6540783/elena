# Hometask_13_1 Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию
#
# def lst_sum_sorted(lst):
#     lst_sum = []
#     for i in lst:
#         sumj = 0
#         for j in i:
#             sumj += int(j)
#         lst_sum.append(sumj)
#     return sorted(lst_sum)
#
# print(lst_sum_sorted(input().split()))

# def function(x):
#     if x <= -2:
#         y = 1 - (x+2)**2
#     elif x > -2 and x <= 2:
#         y = -x/2
#     else:
#         y = (x - 2)**2 + 1
#     return y
#
# print(function(4.5))

# Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.

def nums(lst):
    lst_finish = []
    for i in lst:
        if int(i) % 2 == 0:
            lst_finish.append(int(i)//2)
    return lst_finish

print(nums(input().split()))

