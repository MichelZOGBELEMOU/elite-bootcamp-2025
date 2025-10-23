"""Module providing a safe division function"""
def safe_divide(a: float, b: float) -> float | None:
    """divide a by b safely.
    
    Returns:
        The result of a / b if b is not zero.
        None if division by zero occurs.
    """
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: You can't divide by zero")
        return None
 
    
def main() -> None:
    """Demonstration of safe_divide usage."""
    try:
        # Devide whithout exception
        print(safe_divide(12, 2))

        # Devide whit exeption
        print(safe_divide(12, 0))
    except ZeroDivisionError as e:
        print(e)

    # Validations
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None

if __name__ == "__main__":
    main()
