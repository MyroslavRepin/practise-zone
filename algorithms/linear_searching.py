def linear_searching(raw_list, searching_number):
    for i in raw_list:
        if searching_number == i:
            value_index = raw_list.index(i)
            print(f"Finded a value {i} at index: {value_index}")
            break
        if searching_number != i:
            print('Keep trying')
        else:
            return "Out of index"


searching_number = 12
raw_list = my_list = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

linear_searching(raw_list, searching_number)
