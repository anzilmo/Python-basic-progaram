def reverse_array(arr):
    
    reversed_arr = arr[::-1]
    return reversed_arr

my_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(my_array)
print("Original array:", my_array)
print("Reversed array:", reversed_array)
