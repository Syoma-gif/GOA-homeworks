def divisible_by_3_and_5(numbers):
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print(num)

divisible_by_3_and_5([10, 15, 30, 8, 45])  
