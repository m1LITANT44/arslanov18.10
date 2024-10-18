import random
try:
    for i in range (1, 12):
        with open(f'input{str(i).zfill(2)}.txt', 'r', encoding="utf-8")as file:
            l_read = file.readline().split()
            random_word = random.choice(l_read)
            word = (l_read[0])
            attemps = 6
            g_w = []
            word_count = list(word)
            #print(l_read)
            print('Добро пожаловатьв игру "Угадай Слово"')
            print('Угадайте слово с {attemps} попыток')
        #while len(word_count) > 0 and attemps > 0:
            #print('угаданные буквы:' , "".join(g_w))
        l_read = [letter if letter in g_w else "_"for letter in random_word]
        word_choice = input("ведите букву:").lower()
        if word_choice in word_count:
            print('Верно')
            word_count.remove(word_choice)
            g_w.append(word_choice)
        else:
            print('неверно')
            attemps -= 1
            g_w.append(word_choice)
        if len(word_count) == 0:
            print(f'Вы угадали слово{random_word}.')
        else:
            print(f'Попытки закончились. Слово было:{random_word}.')
except FileNotFoundError as e:
    print('Фаёл не найден')