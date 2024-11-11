# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

def guess_the_number():
    while True:
        number_to_guess = random.randint(1, 100)
        print("Я Задумал число от 1 до 100. Попробуй узнать!")

        user_guess = input("Вводи число: ")

        # Проверка, что пользователь вводит целое число
        try:
            user_guess = int(user_guess)
        except ValueError:
            print(" введи целое число:<")
            continue

        if user_guess == number_to_guess:
            print("Фига угадал, Крутой")
        else:
            print(f"твой ответ не соответствует моему числу. Моё число было: {number_to_guess}")

        continue_game = input("Хочешь начать игру заново? (да/нет): ").strip().lower()
        if continue_game != 'да':
            print("Не хочешь продолжать? Ну ладно, ПАКА! Надеюсь, ты пойдёшь *****!!! До встречи!")
            break

guess_the_number()



