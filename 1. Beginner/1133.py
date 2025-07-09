# Read two integer inputs
x = int(input())
y = int(input())

# Define range boundaries
start = min(x, y)
end = max(x, y)

# Print all values strictly between x and y
# that leave a remainder of 2 or 3 when divided by 5
for number in range(start + 1, end):
    if number % 5 == 2 or number % 5 == 3:
        print(number)