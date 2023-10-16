## 4
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
# def lim_max(nums, limit): 
#     max_num = -1 
# 
# 
#     for num in nums: 
#         if num < limit and num > max_num: 
#             max_num = num 
#     return max_num
# 
# 
# nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)
# limit = 50

# 2
# def del_rep(num): # Создание функции
#     num = list(set(num))
#     num.sort() # Сортируем список
#     return num # Возвращаем переменную
# num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
# print(del_rep(num))
    
# 1
# def list_reorder(ref_list):
#     first_names = ref_list[0]
#     last_names = ref_list[1]
#     result = []
# 
#     for i in range(len(first_names)):
#         result.append([first_names[i], last_names[i]])
# 
#     return result
