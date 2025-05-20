

# text =  input("enter text : ")
# print("Это буквы")

# else.Text =  list()
# print( 'это цифра')

# else.Text =  list()
# print( 'неправельно')

# else.Text =  list()
# print( 'это цифра')

# monday = int(input("Enter Monday: "))
# tuesday = int(input("Enter Tuesday: "))
# wednesday = int(input("Enter Wednesday: "))
# thursday = int(input("Enter Thursday: "))
# friday = int(input("Enter Friday: "))
# saturday = int(input("Enter Saturday: "))
# sunday = int(input("Enter Sunday: "))
# my_list = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]
# print("total amount",sum(my_list) , end="$\n")
# print("avarege amout",sum(my_list)/7,end="$\n")



from datetime import datetime

# Получаем дату от пользователя
date_input = input("Введите дату в формате ДД/ММ/ГГГГ: ")

try:
    date_obj = datetime.strptime(date_input, "%d/%m/%Y")
    day = date_obj.day
    month = date_obj.month

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        sign = "Gemini"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        sign = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        sign = "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        sign = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        sign = "Libra"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        sign = "Scorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        sign = "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
        sign = "Capricorn"
    elif (month == 1 and day >= 21) or (month == 2 and day <= 18):
        sign = "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        sign = "Pisces"
    else:
        sign = "Unknown"

    print(f"Zodiac sign: {sign}")

except ValueError:
    print("Неверный формат даты! Используй формат ДД/ММ/ГГГГ (например, 12/2/2010)")
