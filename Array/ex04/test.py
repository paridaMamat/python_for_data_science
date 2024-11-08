# Original array
original_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposing without NumPy
transposed_array = [[original_array[j][i] for j in range(len(original_array))] for i in range(len(original_array[0]))]

print("Transposed Array:")
for row in transposed_array:
    print(row)

