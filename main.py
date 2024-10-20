num = int(input("Введите число от 1 до 5: "))
numbers = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}

if num < 6:
    print(numbers[num])
else:
    print("Ошибка, до свидания!")