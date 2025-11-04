
name = input("Введите ваше имя: ")


print(f"Привет, {name}, начинаем тренировку!")


question_first = "My name ___ Vova"
question_second = "I ___ a coder"
question_third = "I live ___ Moscow"


answer_first = "is"
answer_second = "am"
answer_third = "in"


score = 0
correct_answers = 0


print(1, question_first)
ans_first = input("Ваш ответ: ").strip().lower()
if ans_first == answer_first:
    print("Ответ верный! Вы получаете 10 баллов!")
    score += 10
    correct_answers += 1
else:
    print(f"Неправильно. Правильный ответ: {answer_first}")


print(2, question_second)
ans_second = input("Ваш ответ: ").strip().lower()
if ans_second == answer_second:
    print("Ответ верный! Вы получаете 10 баллов!")
    score += 10
    correct_answers += 1
else:
    print(f"Неправильно. Правильный ответ: {answer_second}")


print(3, question_third)
ans_third = input("Ваш ответ: ").strip().lower()
if ans_third == answer_third:
    print("Ответ верный! Вы получаете 10 баллов!")
    score += 10
    correct_answers += 1
else:
    print(f"Неправильно. Правильный ответ: {answer_third}")


print(f"Вот и все, {name}!")
print(f"Количество правильных ответов: {correct_answers}")
print(f"Количество баллов: {score}")


percent = (correct_answers / 3) * 100 if correct_answers > 0 else 0
round_percent = round(percent, 2)
print(f"Процент правильных ответов: {round_percent}%")