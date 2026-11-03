def calculate_bmr(gender, weight, height, age):
    # Формула Миффлина-Сан Жеора для базового обмена веществ
    if gender == 'м' or gender == 'm':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr