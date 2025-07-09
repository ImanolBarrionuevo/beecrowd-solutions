# Read operation type
operation = input()

# Read the 12x12 matrix
matrix = []
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    matrix.append(row)

# Process the upper triangle (excluding diagonals)
total = 0

for i in range(12):
    for j in range(12):
        if j > i and j < 11 - i:
            total += matrix[i][j]

# Output result
if operation == "S":
    print(f"{total:.1f}")
elif operation == "M":
    print(f"{(total / 30):.1f}") # 30 is the fixed number of elements in the upper region
