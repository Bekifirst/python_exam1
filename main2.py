import random

def get_user_choice():
    user_choice = input("Выберите: камень (r), ножницы (s) или бумага (p): ")
    while user_choice not in ['r', 's', 'p']:
        user_choice = input("Некорректный выбор. Попробуйте еще раз: ")
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(['r', 's', 'p'])
    return computer_choice

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_again():
    choice = input("Хотите сыграть снова? (да/нет): ")
    return choice.lower() == 'да'

def main():
    print("Приветствую вас в игре 'камень, ножницы, бумага'!")
    play = True
    while play:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = compare_choices(user_choice, computer_choice)
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        print(result)
        play = play_again()

    print("Спасибо за игру! До свидания!")

if __name__ == "__main__":
    main()