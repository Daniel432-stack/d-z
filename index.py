import random

igra = ["камень", "ножницы", "бумага"]

men = input("Выберай: камень ножницы  или бумага: ")

compyter = random.choice(igra)

print("компютер выбрал:", compyter)


if men == compyter:
    print("Ничья!")
elif (men == "камеень" and compyter == "ножницы") or \
     (men == "ножницы" and compyter == "бумага") or \
     (men == "бумага" and compyter == "камень"):
    print("Сен уттун!")
elif men in igra:
    print("Ты проиграл!")
else:
    print("Такого нету.")
    