def binary_search(sorted_list, target):
    # Need to create a function for a dividing a list

    def deleting_half(sorted_list, first_part):
        global middle_index
        middle_index = len(sorted_list) // 2
        if first_part:
            return sorted_list[middle_index:]
        if not first_part:
            return sorted_list[:middle_index]

    print(deleting_half(sorted_list, False))
    last_element = sorted_list[:middle_index][-1]
    print(last_element)
    if last_element >= 7:
        print('Last element bigger than target')
    else:
        print("Last element is smaller than target")


target = 7

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"Sorted list: {sorted_list}")
binary_search(sorted_list, target)
