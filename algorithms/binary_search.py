def binary_search(sorted_list, target):
    # Need to create a function for a dividing a list

    def deleting_half(sorted_list, first_part):
        global middle_index
        middle_index = len(sorted_list) // 2

        if first_part == True:     # Deleting first part
            del sorted_list[:middle_index]
            return sorted_list
        if first_part == False:  # Deleting second part
            del sorted_list[middle_index:]
            return sorted_list

    middle_index = len(sorted_list) // 2

    first_half = sorted_list[:middle_index]
    second_half = sorted_list[middle_index:]

    # последний из первой половины
    last_of_first = first_half[-1]
    first_of_second = second_half[0]              # первый из второй половины

    print("Последний из первой половины:", last_of_first)
    print("Первый из второй половины:", first_of_second)

    #     print('Target smaller')
    # else:
    #     print('Targer bigger')

    # deleting_half(sorted_list, False)


target = 7

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"Old list: {sorted_list}")
binary_search(sorted_list, target=target)
print(f"New list: {sorted_list}")
