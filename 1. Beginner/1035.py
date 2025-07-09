# Read four integer values separated by space
numbers = input().split(" ")
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

# Apply the conditional rules
if b > c and d > a and (c + d) > (a + b) and (c > 0 and d > 0) and a % 2 == 0:
    print("Valores aceitos") # Accepted values
else:
    print("Valores nao aceitos") # Not accepted values
