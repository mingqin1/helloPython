import array

# Declare a list type object
list_object = [3, 4, 1, 5, 2]

# Declare an integer array object
array_object = array.array('d', sorted([3, 4, 1, 5, 2]))

print('Sorted list ->', sorted(list_object))
print('Sorted array ->', sorted(array_object))
