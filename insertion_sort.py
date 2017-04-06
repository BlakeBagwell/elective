def insertion_sort(array):
    for i in range(1, len(array)):
        position = i
        currentValue = array[i]
        while position > 0 and array[position - 1] > currentValue:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = currentValue
    return array

my_array = [2, 45, 23, 4, 5, 12, 20, 27, 20]

print insertion_sort(my_array)
