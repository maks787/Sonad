# Меню
from fnmatch import translate


while True:
    print("""
    1. Перевод с эстонского на русский
    2. Перевод с русского на эстонский
    3. Добавить слово в словарь
    4. Исправить ошибку в словаре
    5. Проверить знание слов из словаря
    6. Выход
    """)
    choice = input("Выберите действие: ")
    if choice == "1":
        word = input("Введите слово на эстонском: ")
        translation = translate(word, est_to_rus)
        if translation is not None:
            print(f"Перевод: {translation}")
        else:
            print(f"Слово '{word}' отсутствует в словаре")

    elif choice == "2":
        word = input("Введите слово на русском: ")
        translation = translate(word, rus_to_est)
        if translation is not None:
            print(f"Перевод: {translation}")
        else:
            print(f"Слово '{word}' отсутствует в словаре")

    elif choice == "3":
        language = input("Введите язык, на котором добавляется слово (est или rus): ")
        word = input("Введите слово: ")
        translation = input("Введите перевод: ")
        if language == "est":
            add_word(word, translation, est_to_rus)
            add_word(translation, word, rus_to_est)
            print("Слово добавлено в словарь")
        elif language == "rus":
            add_word(word, translation, rus_to_est)
            add_word(translation, word, est_to_rus)
            print("Слово добавлено в словарь")
        else:
            print("Ошибка: неподдерживаемый язык")

    elif choice == "4":
        language = input("Введите язык, на котором исправляется ошибка (est или rus): ")
        word = input("Введите слово, в котором нужно исправить ошибку: ")
        new_translation = input("Введите новый перевод: ")
        if language == "est":
            fix_error(word, new_translation, est_to_rus)
            fix_error(new_translation, word, rus_to_est)
        elif language == "rus":
            fix_error(word, new_translation, rus_to_est)
            fix_error(new_translation, word, est_to_rus)
        else:
            print("Ошибка: неподдерживаемый язык")

    elif choice == "5":
        language = input("Выберите язык для проверки (est или rus): ")
        if language == "est":
            test_vocabulary(est_to_rus)
        elif language == "rus":
            test_vocabulary(rus_to_est)
        else:
            print("Ошибка: неподдерживаемый язык")

    elif choice == "6":
        print("Выход")
        break

    else:
        print("Ошибка: неправильный ввод. Попробуйте еще раз.")