def Operation():
    oper = int(input("1 - Вывести справочник \n2 - Добавить пользователя \n3 - Вывести только имя и фамилию \n4 - Отсортировать по имени \n5 - Отсортировать по id \n6 - Выход \n"))
    return oper

def AddDirectiry():
    id = input("Введите id: ")
    name = input("Введите Имя: ")
    lastName = input("Введите Фамилию: ")
    tel = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    record = f"{id} {name} {lastName} {tel} {comment}\n"
    with open("directory.txt", "a") as file:
        file.write(record)
    print("Пользователь добавлен")

def PrintDirrectory():
    with open("directory.txt", "r") as file:
        for line in file.readlines():
            print(line)

def PrintName():
    with open("directory.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        for line in lst:
            lstLine = line.split(" ")
            print (f"{lstLine[1]} {lstLine[2]}")

def SortName():
    with open("directory.txt", "r") as file:
        lst = file.readlines()
        lst1 = []
        for line in lst:
            lstLine = line.split(" ")
            lst1.append(lstLine)
        lst1 = sorted(lst1, key = lambda x: x[1])
        result = ""
        for line in lst1:
            s = " ".join(line)
            result += s
    with open("directory.txt", "w") as file:
        file.writelines(result)

def SortId():
    with open("directory.txt", "r") as file:
        lst = file.readlines()
        lst1 = []
        for line in lst:
            lstLine = line.split(" ")
            lst1.append(lstLine)
        lst1 = sorted(lst1, key = lambda x: x[0])
        result = ""
        for line in lst1:
            s = " ".join(line)
            result += s
    with open("directory.txt", "w") as file:
        file.writelines(result)   

