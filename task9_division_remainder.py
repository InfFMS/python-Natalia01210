# Задача 9: Деление с остатком
# Напишите программу, которая запрашивает у пользователя два числа и выводит результат их целого деления и остаток.
# Пример:
# Ввод: 9, 4
# Вывод: Целое деление: 2, Остаток: 1
a, b = int(input()), int(input())
print("Целое деление: " + str(a // b) + ", Остаток: " + str(a % b))