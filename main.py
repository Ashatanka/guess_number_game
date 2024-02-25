import random

if __name__ == '__main__':

    # программа генерирует случайное число в диапазоне от 1 до 100
    magic_num = random.randint(1, 100)

    # просит пользователя угадать это число
    print("I made a number from 1 to 100. Guess it!")

    while True:

        # Проверка что это целое неотрицательное число, и что оно в диапазоне от 1 до 100
        try:
            guess_num = int(input("My number is... "))
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            continue

        if not(1 <= guess_num <= 100):
            print("Oops! That was no valid number. Try again...")

        # Проверка на правильность ответа
        if guess_num == magic_num:
            print("You're absolutely right! My congratulations!")
            break
        elif guess_num < magic_num:
            print("Sorry, you're wrong. My number is bigger. Try again.")
            continue
        else: # guess_num > magic_num
            print("Sorry, you're wrong. My number is smaller. Try again.")
            continue