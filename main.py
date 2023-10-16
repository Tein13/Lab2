# 4
# def temp_cat(x): # Создаем функцию и проверяем условия
#     if x < -20:
#         temp = 0
#     elif -20 < x < 0 or x == 0:
#         temp = 1
#     elif 0 < x < 15:
#         temp = 2
#     elif 15 < x < 25:
#         temp = 3
#     else:
#         temp = 4
#     return temp # Возврат переменной 
# x = int(input("Введите температуру в градусах цельсия:")) # Запрос температуры пользователя
# print(temp_cat(x)) # Вывод

# 3
# numlist = 0
# max_num = 0
# n = 0
# def lim_max(nums):
#     for i in nums:
#         if nums[n] < limit:
#             max_num = nums[n]
#         if nums[n + 1] > nums[n]:
#             max_num = nums[n + 1]
#     return max_num
# limit = 50
# nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)
# print(lim_max(nums))

# 2
# def del_rep(num): # Создание функции
#     num = list(set(num))
#     num.sort() # Сортируем список
#     return num # Возвращаем переменную
# num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
# print(del_rep(num))
    
# 1
# n = 1
# def list_reorder(ref_list):
#     tuple
#     name = ref_list[1]
#     lastname = ref_list[0]
#     return name, lastname
# ref_list = ['Александр', 'Анастасия'], ['Смирнов', 'Иванова']
# print(list_reorder(ref_list))

