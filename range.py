import random

def create_list(length: int) -> list[int]:
    """
    Create a list with random numbers (linear complexity)
    """
    return [random.randint(0, 100) for _ in range(length)]
