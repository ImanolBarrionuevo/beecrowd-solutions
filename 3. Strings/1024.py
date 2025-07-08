# Read the number of input strings
l = int(input())
strings = []

# Process each input string
for i in range(l):
    original = input()
    transformed = ''

    # Shift alphabetic characters by +3 in ASCII
    for char in original:
        ascii_value = ord(char)
        if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):  # If it's an alphabetic letter (uppercase A–Z or lowercase a–z)
            ascii_value += 3
        transformed += chr(ascii_value)

    # Reverse the entire transformed string
    transformed = transformed[::-1]
    strings.append(transformed)

# Post-process each string in the list
for string in strings:
    midpoint = len(string) // 2
    res = string[:midpoint]
    second_half = string[midpoint:]

    # Shift characters in the second half by -1 in ASCII
    for char in second_half:
        res += chr(ord(char) - 1)

    # Output the final transformed string
    print(res)