from datetime import datetime
import psutil
import time


def hello():
    """Display a simple hello message to start the bootcamp"""
    print(f"Hello, Bootcamp!")


def variables():
    """Declare variable and print their types"""
    integer = 25
    real = 14.5
    name = 'michel'
    is_married = True
    cars = ['veloster', 'cle 53 amg', 'genesis g90l']
    person = {'first name': 'michel',
              'last name': 'zogbelemou', 'field': 'computer science'}
    print(f"{f'{integer=}'.split('=')[0]}: {type(integer)}")
    print(f"{f'{real=}'.split('=')[0]}: {type(real)}")
    print(f"{f'{name=}'.split('=')[0]}: {type(name)}")
    print(f"{f'{is_married=}'.split('=')[0]}: {type(is_married)}")
    print(f"{f'{cars=}'.split('=')[0]}: {type(cars)}")
    print(f"{f'{person=}'.split('=')[0]}: {type(person)}")


def add_numbers(smallest: int, largest: int) -> int:
    """sum numbers for smallest to largest"""

    # total variable contening the sum
    total = 0

    # looping to sum
    for num in range(smallest, largest + 1):
        total += num

    # returning the sum
    return total


def count_down(largest: int) -> None:
    """count from largest to 0"""
    counter = largest
    while counter >= 0:
        print(counter, end=", ")
        counter -= 1


def sign_of_number(number: float) -> None:
    """Classify a number as positive, negative, or zero"""
    if number < 0:
        print("Negative")
    elif number == 0:
        print("zero")
    elif number > 0:
        print("Positive")


def square(x: int) -> int:
    """Return the square of the number"""
    return x ** 2


def square_numbers(numbers: list[int]) -> list[int]:
    # empty list wich will contain the squares:
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    # returning the list of squares
    return squares


def system_uptime():
    boot_time_stamp = psutil.boot_time()
    boot_datetime = datetime.fromtimestamp(boot_time_stamp)
    now = datetime.now()
    uptime = now - boot_datetime
    return uptime


def main():

    hello()

    print('\n')

    variables()

    print('\n')

    print(f"Sum of number from 1 to 100: {add_numbers(1, 100)}")

    print("\nCount down for 10 to 0:")
    count_down(10)

    print("\nsigne of 15 : ", end="")
    sign_of_number(15)

    print("the Square of 15 is ", square(15))

    print(
        f"Numbers :[1, 2, 3, 4, 5, 6, 7, 8, 9]   Squares :{square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])}")

    uptime = system_uptime()

    print(
        f"Systemem uptime: {uptime.days} days {uptime.seconds // 3600}  hours {(uptime.seconds % 3600) // 60} mn ")


if __name__ == '__main__':
    main()
