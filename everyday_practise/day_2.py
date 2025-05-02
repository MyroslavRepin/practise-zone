# This code should find digits and sum them from the strig

def sum_digit(text):
    total = []
    current_nums = ""
    for char in text:
        if char.isdigit():
            current_nums = char
        else:
            total.append(current_nums)
    return sum(total)


print(sum_digit("anbvdesn45367e8ducjb4367"))

# DONE :)
