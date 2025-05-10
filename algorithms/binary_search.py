def binary_search(sorted_list):
    central_index = len(sorted_list) // 2

    print(f"First part: {sorted_list[:central_index]}")

    def delete_half(central_index_val, sorted_list):
        print(f"Will be removed: {sorted_list[central_index_val:]}")
        sorted_list[central_index_val:].clear()

    delete_half(central_index, sorted_list)


searching_number = 7

raw_list = [23, 7, 42, 15, 3, 19, 8, 34, 5, 1, 50, 27]
sorted_list = sorted(raw_list)

print(f"Sorted list: {sorted_list}")
binary_search(sorted_list)
