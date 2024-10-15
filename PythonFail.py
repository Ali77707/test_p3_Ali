# # Списки
# names = ["Петя", "Вася", "Коля"]
# print(names)
# print(names[0], names[1], names[2])
# print(names[-1], names[-2], names[-3])
# names[-1] = "Эдик"
# print(names)
# # Добавление
# names.append("Коля") # добавляет элемент в конец списка
# print(names)
# names.insert(3, "Толя")
# print(names)
# names.extend(["Сеня", "Вася"])
# print(names)
# # Удаление
# # names.remove("Сеня")
# # print(names)
# # name = names.pop(0)
# # print(name, names)
# # del names[-1]
# # print(names)
# # names.clear()
# # print(names)
# # Поиск элементов
# print(names.index("Петя"))
# print(names.count("Вася"))
# # Сортировка и обратный порядок
# names.sort()
# print(names)
# names.reverse()
# print(names)
# sorted_list = sorted(names)
# print(sorted_list, names)
# print(len(names))

# print([1,2,3] + names)
# print("строка", "ааввавав")
# print(names * 4)



# Кортеж
names = ("Петя" ,"Вася", "Коля")
print(names)
print(names[0], names[1], names[2])
print(names[-1], names[-2], names[-3])

names[0] = "Вася"
print(names.count("Коля"))
print(names.index("Коля"))