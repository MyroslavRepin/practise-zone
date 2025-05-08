def max_number(raw_list):
    bigger_num = []
    smaller_num = []
    for digit in raw_list:
        digit_index = raw_list.index(digit) + 1
        print(digit_index)
        print(f"Index 1: {raw_list[digit_index]}")

        # if digit > raw_list[digit_index + 1]:
        #     print('Bigger')
        # print(digit)
"""I should use enmurate(), bocause my code works not properly"""

max_number(raw_list=[10, 2, 3, 4])
