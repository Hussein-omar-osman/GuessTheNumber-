import random

logo = """
█▀▀ █ █ █▀▀ █▀ █▀   ▀█▀ █ █ █▀▀   █▄░█ █ █ █▀▄▀█ █▄▄ █▀▀ █▀█
█▄█ █▄█ ██▄ ▄█ ▄█    █  █▀█ ██▄   █░▀█ █▄█ █ ▀ █ █▄█ ██▄ █▀▄
"""
print(logo)
numbers = [n for n in range(1, 101)]
# print(numbers)
answer = random.choice(numbers)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
print(f"The comp's answer is {answer}, this is just to counter check")

attempts = 5
start_game = True


while start_game:
    print(f"You have {attempts} attempts.")
    user_input = int(input("Make a guess: "))
    attempts -= 1


    def check_status(user_answer, comp_answer, total_attempts):
        """Checks if the user has got the correct answer or out of attempts"""
        if user_answer == comp_answer:
            print(f"You Won! The answer was {comp_answer}.")
        elif total_attempts == 0:
            print(f'Your attempts are over and the answer was {comp_answer}')
        elif user_answer > comp_answer:
            print("Too high, guess again.")
        elif user_answer < comp_answer:
            print("Too low, guess again.")

    check_status(user_input, answer, attempts)

    if user_input == answer or attempts == 0:
        start_game = False
