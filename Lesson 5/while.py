import random

secret_number = random.randint(0, 10)
attempts = 0

print("Угадай число от 0 до 10")

# Добавить подсказку: загаданное число больше или меньше
# Число попыток

while True:
    user_guess = int(input("Введите ваше число: "))
    attempts += 1

    if user_guess < secret_number:
        print("Загаданное число больше")

    elif user_guess > secret_number:
        print("Загаданное число меньше")
    
    else:
        print(f"Вы угадали число {secret_number} за {attempts} попыток")
        break