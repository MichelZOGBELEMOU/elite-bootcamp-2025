"""Module providing a custom exception and one of its use case."""
class InvalidAgeError(Exception):
    """Raised when age is negative or unrealistically high."""

def validate_age(age: int) -> bool:
    """Check age for validation return True if valid.
    Raises InvalidAgeError if age negative or too high.
    """
    if age < 0:
        raise InvalidAgeError("You can't have a negative age")
    if age > 110:
        raise InvalidAgeError("You can't be more than 110 years old")
    return True

def main() -> None:
    """Demonstration of validate_age usage"""

    # Without exception
    try:
        if validate_age(32) :
            print("Ok")
    except InvalidAgeError as e:
        print(e)


    # with exception
    try:
        validate_age(-10)
    except InvalidAgeError as e:
        print(e)

    try:
        validate_age(200)
    except InvalidAgeError as e:
        print(e)

if __name__ == "__main__":
    main()