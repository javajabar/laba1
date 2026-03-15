def task1():
    text = input("Введите текст из строчных латинских букв, оканчивающийся точкой: ")

    if len(text) < 2 or text[-1] != ".":
        print("Ошибка: текст должен заканчиваться точкой.")
        return

    for char in text[:-1]:
        if char < "a" or char > "z":
            print("Ошибка: до точки должны быть только строчные латинские буквы.")
            return

    counts = {}
    for char in text[:-1]:
        counts[char] = counts.get(char, 0) + 1

    result = ""
    for char in text[:-1]:
        if counts[char] >= 2 and char not in result:
            result += char

    print("Буквы, которые встречаются не менее двух раз:", result)


def task2():
    text = input("Введите непустую последовательность символов: ")

    result = set()
    for char in text:
        if "T" <= char <= "X" or "1" <= char <= "4":
            result.add(char)

    print("Полученное множество:", result)


while True:
    print("\n1 - Задача 1")
    print("2 - Задача 2")
    print("0 - Выход")
    choice = input("Выберите номер задачи: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "0":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор.")
