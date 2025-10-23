"""Exception chain practice"""
try:
    raise ValueError("Invalid input")
except ValueError as e:
    raise RuntimeError("something failed") from e
