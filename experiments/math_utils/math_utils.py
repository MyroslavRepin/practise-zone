def sum_of_digits(n: int) -> int:
    number = str(n)
    raw_list = []
    for char in number:
        raw_list.append(int(char))
    return sum(raw_list)
