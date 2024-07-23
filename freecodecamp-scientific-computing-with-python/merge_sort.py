def merge_sort(array):
    if len(array) <= 1:
        return

    middle_point = len(array) // 2

    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_part_index = 0
    right_part_index = 0

    sorted_index = 0

    while left_part_index < len(left_part) and right_part_index < len(right_part):
        if left_part[left_part_index] < right_part[right_part_index]:
            array[sorted_index] = left_part[left_part_index]
            left_part_index += 1
        else:
            array[sorted_index] = right_part[right_part_index]
            right_part_index += 1
        sorted_index += 1
    
    while left_part_index < len(left_part):
        array[sorted_index] = left_part[left_part_index]
        left_part_index += 1
        sorted_index += 1

    while right_part_index < len(right_part):
        array[sorted_index] = right_part[right_part_index]
        right_part_index += 1
        sorted_index += 1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ', numbers)
    merge_sort(numbers)
    print('Sorted array: ', numbers)