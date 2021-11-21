def directionOfReading(numbers):
    l = len(numbers)
    a = [str(n).zfill(l) for n in numbers]
    return [int(''.join(n)) for n in zip(*a)]