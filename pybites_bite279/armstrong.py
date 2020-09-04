def is_armstrong(n: int) -> bool:
    if n < 10:
        return True
    numbers = list(str(n))
    return n == sum([int(number)**len(numbers) for number in numbers])
