from collections import Counter
def freq_digit(num: int) -> int:
    numbers = list(str(num))
    c = Counter(numbers)
    return int(c.most_common()[0][0])