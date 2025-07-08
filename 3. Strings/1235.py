def fix_string(str):

    # Function to transform a string by reversing its first and second halves independently

    pivot = len(str) // 2 # Calculate the midpoint of the string
    j = pivot - 1 # Start from the end of the first half
    res = ""

    # Reverse the first half of the string
    while j >= 0:
        res += str[j]
        j -= 1

    k = len(str) - 1 # Start from the end of the string

    # Reverse the second half of the string
    while k >= pivot:
        res += str[k]
        k -= 1

    return res

# Read the number of lines to process
line_count = int(input())

# Initialize a list to store transformed strings
string_list = [""] * line_count

# Read each string, transform it using fix_string, and store the result
for i in range(line_count):
    string_list[i] = fix_string(input())

# Output each transformed string
for l in range(line_count):
    print(string_list[l])