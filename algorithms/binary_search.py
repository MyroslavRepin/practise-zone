def binary_search(sorted_list, target):
    middle = len(sorted_list) // 2
    last_element = sorted_list[:middle+1][:-1]
    print(last_element[-1])
    #     print('Less')
    # else:
    #     print('else')


target = 7

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"Sorted list: {sorted_list}")
binary_search(sorted_list, target)
