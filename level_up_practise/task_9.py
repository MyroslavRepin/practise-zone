def max_number(raw_list):

    for i, digit in enumerate(raw_list):
        if i + 1 < len(raw_list):
            # print(f"Текущий: {digit}, Следующий: {raw_list[i + 1]}")
            if digit > raw_list[i + 1]:
                print(
                    f"Bigger  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")
            if digit < raw_list[i + 1]:
                print(f"Less  ||  Digit: {digit}  |  Next: {raw_list[i + 1]}")


max_number(raw_list=[10, 2, 1, 4, 12])
