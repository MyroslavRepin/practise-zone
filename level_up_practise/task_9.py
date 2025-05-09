def max_number(raw_list):
    # I WAS TRYING TO USE IT, BUT DIDN'T FIGURE OUT.....
    # for i, digit in enumerate(raw_list[::-1]):
    #     if i + 1 < len(raw_list):
    #         if digit > raw_list[i + 1]:
    #             print(
    #                 f"Bigger  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")
    #             max_list.append(digit)
    #         if digit < raw_list[i + 1]:
    #             print(
    #                 f"Less  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")

    # print(max_list)

    current_max = float("-inf")
    for number in reversed(raw_list):
        if number >= current_max:
            current_max = number
    print(current_max)


max_number(raw_list=[10, 2, 1, 4, 12])
