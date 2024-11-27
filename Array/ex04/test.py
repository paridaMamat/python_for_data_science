import numpy as np

# Original array
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
# array = np.array(original_array)

print(f"len(array) = {len(array)}")
print(f"len(array[0] = {len(array[0])}")
print(f"test array[2][1] = {array[2][1]}")
# height, width = array.shape
# print(height)
# print(width)
transposed_array = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
# transposed_array = array.T
print(f"Transposed Array: {transposed_array}")
for row in transposed_array:
    print(row)

