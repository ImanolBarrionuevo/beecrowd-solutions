entry = input() # Read the next input line

# Continue processing until "0 0" is received
while entry != "0 0":
    res = ''

    # Iterate over characters from the third position onward
    for char in entry[2:]:
        # Keep characters that do not match the first character
        if char != entry[0]:
            res += char

    # If no characters remain after filtering, set result to "0"
    if res == '':
        res = "0"

    print(int(res)) # Print the numeric value of the resulting string
    entry = input() # Read the next input line