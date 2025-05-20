# list = [1,2,3,4,5,6,7,]
# list.append(8)
# list.pop(4)
# list.insert(1,3)
# print(len(list))
# list.clear()
# print(list)

# .\
from datetime import datetime, date

def get_zodiac_sign(day: int, month: int) -> str:
    zodiac_signs = [
        ((21, 3),  (19, 4),  "Aries"),
        ((20, 4),  (20, 5),  "Taurus"),
        ((21, 5),  (21, 6),  "Gemini"),
        ((22, 6),  (22, 7),  "Cancer"),
        ((23, 7),  (22, 8),  "Leo"),
        ((23, 8),  (22, 9),  "Virgo"),
        ((23, 9),  (23, 10), "Libra"),
        ((24, 10), (22, 11), "Scorpio"),
        ((23, 11), (21, 12), "Sagittarius"),
        ((22, 12), (20, 1),  "Capricorn"),
        ((21, 1),  (18, 2),  "Aquarius"),
        ((19, 2),  (20, 3),  "Pisces")
    ]

    current = date(2000, month, day)

    for start, end, sign in zodiac_signs:
        start_date = date(2000, start[1], start[0])
        end_date = date(2000, end[1], end[0])

        if start[1] > end[1]:  # через Новый Год (например Козерог)
            if current >= start_date or current <= end_date:
                return sign
        elif start_date <= current <= end_date:
            return sign

    return "Unknown"

# --- Основной код ---
try:
    input_str = input("Введите дату в формате ДД/ММ/ГГГГ: ")  # Пример: 01/12/2025
    user_date = datetime.strptime(input_str, "%d/%m/%Y")
    zodiac = get_zodiac_sign(user_date.day, user_date.month)
    print(f"Your zodiac sign is: {zodiac}")
except ValueError:
    print("Неверный формат даты. Используй ДД/ММ/ГГГГ, например: 01/12/2025")

        
    