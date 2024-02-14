def find_maximum(numbers, compare_func):
    if not numbers:
        return None

    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = compare_func(maximum, num)

    return maximum

numbers = [5, 3, 9, 1, 7, 2]
greater_of_two = lambda x, y: x if x > y else y

maximum = find_maximum(numbers, greater_of_two)
print("Maximum number:", maximum)
