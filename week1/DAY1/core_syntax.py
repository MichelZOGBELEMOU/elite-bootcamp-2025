import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pause(prompt: str = "Press any key to continue") -> None:
    input(prompt)


def print_triangle(height: int) -> None:
    """Print a triangle of * """
    # variable with a nomber of start by line initial value = 1
    # looping till the height
    for line in range(height):
        spaces = height - line - 1
        stars = 2 * line + 1
        print(" " * spaces + "*" * stars)


def min_number(numbers: list[int]) -> int:
    """Return the minimum of the list"""
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number

    return smallest


def max_number(numbers: list[int]) -> int:
    """Return the maximum of the list"""
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest


def avg_number(numbers: list[int]) -> float:
    total = 0
    counter = 0
    for number in numbers:
        total += number
        counter += 1
    average = total / counter
    return average


def items_index_values(languages: list[str]) -> None:
    """Print each item index and value"""
    for index, value in enumerate(languages):
        print(f"{index}: {value}")


def dict_to_string(countries: dict) -> None:
    for key, value in countries.items():
        print(f"Capital of {key.title()} is {value.title()}")


def collect_numbers() -> list[int]:
    print('Enter a list of number (q, exit, quit to finish)')
    numbers = []
    while True:
        user_input = input(">")
        if user_input.lower() in ['q', 'exit', 'quit']:
            break
        else:
            numbers.append(int(user_input))
    return numbers


def main():

    while True:
        clear()
        print("""======Day 1 practice menu======
            1. Print triangle
            2. Numbers statistics
            3. Language index lis
            4. Country-capital printer
            0. Quit(q, exit, quit)
            """)
        option = input('Choose an option')
        if option in ['q', 'quit', 'exit', '0']:
            break
        elif option == '1':
            clear()
            print("Enter the Height of the triangle:")
            height = int(input(">"))
            print_triangle(height)
            pause()

        elif option == '2':
            clear()
            numbers = collect_numbers()
            print(f"Minimum: {min_number(numbers)}")
            print(f"Maximum: {max_number(numbers)}")
            print(f"Average: {avg_number(numbers)}")
            pause()

        elif option == '3':

            # list of language:
            clear()
            languages = ['English', 'French', 'Korean', 'Spanish', 'Dutch']
            items_index_values(languages)
            pause()
        elif option == '4':

            clear()
            # list of countries
            countries = {'guinea': 'conakry',
                         'korea': 'seoul', 'usa': 'washington dc'}
            dict_to_string(countries)
            pause()


if __name__ == "__main__":
    main()
