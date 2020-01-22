def array_plus_array(arr1, arr2):
    result = [a1 + a2 for a1, a2 in zip(arr1, arr2)]
    return sum(result)

print(array_plus_array([1, 2, 3], [4, 5, 6]))



