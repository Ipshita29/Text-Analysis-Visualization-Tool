def analyze_numbers(numbers):
    if len(numbers) == 0:
        return None

    total = 0
    for n in numbers:
        total += n

    mean = total / len(numbers)

    min_val = numbers[0]
    max_val = numbers[0]

    for n in numbers:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n

    return {
        "count": len(numbers),
        "mean": mean,
        "min": min_val,
        "max": max_val
    }
