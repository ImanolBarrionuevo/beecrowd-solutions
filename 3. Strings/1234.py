lines = []
# Read lines until end-of-file

while True:
    try:
        line = input()
        count = 0 # Non space count

        # Apply alternating casing to non-space characters
        for i in range(len(line)):
            if line[i] != " ":
                count += 1
                if count % 2 == 0:
                    # Even count: convert to lowercase
                    line = line[:i] + line[i].lower() + line[i+1:len(line)]
                else:
                    # Odd count: convert to uppercase
                    line = line[:i] + line[i].upper() + line[i+1:len(line)]

        # Store the transformed line
        lines.append(line)

    except EOFError:
        break

# Print all processed lines
for line in lines:
    print(line)