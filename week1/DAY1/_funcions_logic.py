import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pause(prompt: str = "Press any key to continue") -> None:
    input(prompt)


def is_even(n: int) -> bool:
    return n % 2 == 0


def factorial(n: int) -> int:
    """Compute the factorial and return it. will return 0 in case the number is
    < 0"""
    if n < 0:
        raise ValueError("the number must be positive")
    elif n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n


def temperatures_stat(temperatures: list[float]) -> dict[str, float]:
    """return a dictionaries stats with average, maximum, minimum  of
    temperatures"""
    if not temperatures:
        raise ValueError("No temperatures provided")
    stats = {}
    stats['average'] = sum(temperatures) / len(temperatures)
    stats['maximum'] = max(temperatures)
    stats['minimum'] = min(temperatures)
    return stats


def get_temperatures() -> list[float]:

    temperatures = []
    while True:

        user_input = input(
            "Enter a temperatures (or q, exit to quit): ").strip()
        if user_input.lower() in ['q', 'exit', 'quit']:
            break
        else:
            try:
                number = float(user_input)
                temperatures.append(number)
            except ValueError:
                print("Invalide input. Enter a valid input")
    return temperatures


def reverse_words(sentence: str) -> str:
    # reverse the given sentence
    list_new_words = sentence.split()
    list_new_words.reverse()
    reverse_sentence = " ".join(list_new_words)
    return reverse_sentence


def atm_simulation():
    # similate atm menu

    balance = 0.0
    while True:
        clear()
        print("====ATM===")
        print("1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("0. Exit(q, quit, exit)")
        option = input("Choose an option: ").strip()
        if option.lower() in ['q', 'quit', 'exit', '0']:
            break
        elif option == "1":
            clear()
            print(f"Your balance is ${balance:.2f}")
            pause()
        elif option == "2":
            clear()
            try:
                amount = float(input("Enter the amount: ").strip())
                if amount <= 0:
                    print("The deposit amount must be positive")
                    pause()
                else:
                    balance += amount
                    print(f"Deposit successful: ${amount:.2f}.")
                    print(f"Balance: ${balance:.2f}")
                    pause()
            except ValueError:
                print("Invalid input. Please enter a valid input")
                pause()
        elif option == "3":

            try:
                clear()
                amount = float(input("Enter the amount: ").strip())
                if amount <= 0:
                    print("Withdrawal amount must be positive:")
                    pause()
                elif amount > balance:
                    print("Insufficient balance.")
                    pause()
                else:
                    balance -= amount
                    print(f"${amount:.2f} withdrawn succesfully ")
                    pause()
            except ValueError:
                print("Invalid amout. Please enter a valid amout")
                pause()
        else:
            print("Invalid choice. Please select from 1 to 4")
            pause()


def main():

    while True:
        clear()
        print('======Applied logic and functions======')
        print("1. Check even number")
        print("2. calculate facturial")
        print("3. Temperatures statistics")
        print("4. Reverse sentence")
        print("5. ATM simulation")
        print("0. Exit (exit, q, quit)")
        option = input("Choose an option: ").strip()
        if option.lower() in ['exit', 'q', 'quit', '0']:
            print("Thank you.")
            pause()
            break
        elif option == '1':
            try:
                number = int(input("Enter a number: ").strip())
                if is_even(number):
                    print(f"{number} is an even number")
                    pause()
                else:
                    print(f"{number} is an odd number")
                    pause()
            except ValueError:
                print("Invalid input. Please enter a valid amount")
        elif option == '2':
            try:
                number = int(input("Enter a positive number: ").strip())
                fact = factorial(number)
                print("The number must be >= 0")
                pause()
                print(f'{number}! = {fact}')
                pause()
            except ValueError as e:
                print("Invalid input.", e)
        elif option == '3':
            clear()
            temperatures = get_temperatures()
            temperatures_stats = temperatures_stat(temperatures)
            for key, value in temperatures_stats.items():
                print(f'{key}: {value}')
            pause()
        elif option == '4':
            clear()
            sentence = input("Enter the sentence to reverse: ").strip()
            reversed_sentence = reverse_words(sentence)
            print("The reversed sentence is: ")
            print(f"\n{reversed_sentence}")
            pause()
        elif option == '5':
            atm_simulation()
        else:
            print("Invalid option. please choose form 0 to 5 ")


if __name__ == '__main__':
    main()
