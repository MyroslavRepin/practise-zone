# This code should find digits and sum them from the strig

def sum_digit(text):
    sum_list = []
    for char in text:
        if char.isdigit():
            sum_list.append(int(char))
        else:
            print('No digit')
    return sum(sum_list)


print(sum_digit("anbvdesn45367e8ducjb4367"))

# DONE :)
