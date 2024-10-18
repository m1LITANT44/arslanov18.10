import random

try:
    words = []
    for i in range(1,12):
    with open(f"input01.txt", "r", encoding="utf-8" ) as file:
        lines = file.readlines() # массив из слов из файла
        words = [] # массив из слов
        for item in lines:
            words.append(item.strip())
        print(words)
        random_index = random.randint(0, len(words) - 1) #случайный индекс
        secret_world = words[random_index] # случайное слово из массива words
        world = list(secret_world) # массив из букв
        answerArray = ["_"] * len(world) #
        print(answerArray)
    print("Угадайте слово" , " " .join(answerArray))
    while answerArray != world:
        letter = input("Введите букву или exit для выхода:")




except FileNotFoundError:
    print("Файл не найден.")