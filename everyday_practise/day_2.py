# This code should find digits and sum them from the strig

def sum_digit(text):
    total = 0
    current_nums = ""
    for char in text:
        if char.isdigit():
            current_nums += char
            print(current_nums)
        else:
            print('else')

    if current_nums != "":
        total += int(current_nums)

    return total


print(sum_digit("a100b200c300d400e500"))

# FINALLY DONE. THAT'S WAS QUET HARD :)
