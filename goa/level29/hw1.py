def four_letter_names(names):
    result = []
    for name in names:
        if len(name) == 4:
            result.append(name)
    return result

print(four_letter_names(["Luka", "Nino", "Ana", "Giorgi"]))  
