def max_number(raw_list):
    bigger_num = []
    smaller_num = []

    # for digit in raw_list:
    #     digit_index = raw_list.index(digit) + 1
    #     print(digit_index)
    #     print(f"Index 1: {raw_list[digit_index]}")

    #     # if digit > raw_list[digit_index + 1]:
    #     #     print('Bigger')
    #     # print(digit)

    # for index, digit in enumerate(raw_list):
    #     if index + 1 > len(raw_list):
    #         print(f"Bigger: {digit}")
    #     else:
    #         print('Less')
    #     # print(index, digit)

    for i, digit in enumerate(raw_list):
        if i + 1 < len(raw_list):  # чтобы не выйти за границу
            # print(f"Текущий: {digit}, Следующий: {raw_list[i + 1]}")
            if digit > raw_list[i + 1]:
                print(
                    f"Bigger  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")
            if digit < raw_list[i + 1]:
                print(f"Less  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")


max_number(raw_list=[10, 2, 1, 4])
