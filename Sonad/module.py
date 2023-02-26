#def Loe_failist(fail:str)->list:
#    """читаем информацию из файла указывая его название
#    """
#    f=open(fail,"r",encoding="utf-8-sig")
#    jarjend=[]
#    for rida in f:
#        jarjend.append(rida.strip())
#    f.close()
#    return jarjend 
#def Kirjuta_failisse(fail:str,jarjend:list):
#    f=open(fail,"w",encoding="utf-8-sig")
#    for line in jarjend:
#        f.write(line+"\n")
#    f.close()

#from gtts import gTTS
#import os
#def Heli(text:str,keel:str):
#    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
#    os.system("heli.mp3")
      
#    est_to_rus = {
#    "õun": "яблоко",
#    "päike": "солнце",
#    "puu": "дерево",
#    "raamat": "книга",
#    "auto": "машина",
#    "kass": "кот"
#}

#with open("est.txt", "r", encoding="utf-8") as est_file:
#    est_words = est_file.readlines()

#rus_words = []
#for word in est_words:
#    est_word = word.strip()  # Удаляем символ переноса строки
#    rus_word = est_to_rus.get(est_word)  # Ищем соответствующее слово на русском языке
#    rus_words.append(rus_word)

#print(rus_words)
#Вывод:

#css
#Copy code
#['яблоко', 'солнце', 'дерево', 'книга', 'машина', 'кот']
#А вот пример, как мы можем реализовать перевод с русского на эстонский:

#python
#Copy code
## Словарь соответствия слов на русском и эстонском языках
#rus_to_est = {
#    "яблоко": "õun",
#    "солнце": "päike",
#    "дерево": "puu",
#    "книга": "raamat",
#    "машина": "auto",
#    "кот": "kass"
#}

#with open("rus.txt", "r", encoding="utf-8") as rus_file:
#    rus_words = rus_file.readlines()

#est_words = []
#for word in rus_words:
#    rus_word = word.strip()  # Удаляем символ переноса строки
#    est_word = rus_to_est.get(rus_word)  # Ищем соответствующее слово на эстонском языке
#    est_words.append(est_word)

#print(est_words)
#Вывод:

#css
#Copy code
#['õun', 'päike', 'puu', 'raamat', 'auto', 'kass']





import random

# Функция для чтения слов из файла
def read_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words

# Функция для записи слов в файл
def write_words(filename, words):
    with open(filename, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")

# Функция для перевода слов с помощью словаря
def translate(word, dictionary):
    return dictionary.get(word)

# Функция для добавления слова в словарь
def add_word(word, translation, dictionary):
    dictionary[word] = translation

# Функция для исправления ошибки в словаре
def fix_error(word, new_translation, dictionary):
    if word in dictionary:
        dictionary[word] = new_translation
    else:
        print(f"Слово '{word}' отсутствует в словаре")

# Функция для проверки знания слов из словаря
def test_vocabulary(dictionary):
    words = list(dictionary.keys())
    random.shuffle(words)
    correct = 0
    total = len(words)
    for word in words:
        print(f"Переведите слово '{word}':")
        answer = input().strip().lower()
        translation = dictionary[word].lower()
        if answer == translation:
            print("Правильно!")
            correct += 1
        else:
            print(f"Неправильно. Правильный ответ: '{translation}'")
    score = (correct / total) * 100
    print(f"Вы ответили правильно на {correct} из {total} слов ({score:.2f}%)")

# Чтение слов из файлов
est_words = read_words("est.txt")
rus_words = read_words("rus.txt")

# Создание словарей
est_to_rus = dict(zip(est_words, rus_words))
rus_to_est = dict(zip(rus_words, est_words))





