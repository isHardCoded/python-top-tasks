less_five = []

def find_less_five(numbers):
    for number in numbers:
        if number < 5:
            less_five.append(number)
    print(less_five)

numbers = [3, 6, 2, 8, 3, 1, 10]
filtred_numbers = find_less_five(numbers)
