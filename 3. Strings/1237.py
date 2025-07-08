from difflib import SequenceMatcher

# Continuously read pairs of strings until end of input
while True:
    try:
        string1 = input()
        string2 = input()

        # Create a SequenceMatcher object to compare both strings
        matcher = SequenceMatcher(None, string1, string2)

        # Find the longest matching substring between the two strings
        match = (matcher.find_longest_match(0, len(string1), 0, len(string2)))

        # Print the length of the longest match found
        length = match.size
        print(length)

    except EOFError:
        break