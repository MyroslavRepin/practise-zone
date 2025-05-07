# FILTERING EVEN NUMBERS
def return_even(raw_list):
    even_list = []
    for odd in raw_list:
        if odd % 2 == 0:
            even_list.append(odd)
    return even_list


raw_list = [1, 4, 7, 10]
print(return_even(raw_list))
