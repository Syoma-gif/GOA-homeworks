def sum_of_odds(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total


print(sum_of_odds([1, 2, 3, 4, 5]))  
