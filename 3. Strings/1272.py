# List to store all hidden messages
results = []

# Read and process each line
for _ in range(int(input())):
    hidden_message = ""
    words = input().split()

    # Build the hidden message by taking the first letter of each non-empty word
    for word in words:
        if len(word) > 1:
            hidden_message += word[0]
        elif len(word) == 1:
            hidden_message += word  # Keep single-letter words as-is

    results.append(hidden_message)

# Output each hidden message
for message in results:
    print(message)