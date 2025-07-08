# Function to check if a word contains only alphabetic characters (including 'ñ')
def is_valid_word(word):
    word = word.lower()
    for char in word:
        if char not in 'abcdefghijklmnñopqrstuvwxyz':
            return False
    return True

# Main processing loop for multiple inputs
while True:
    try:    
        # Read and split the input line into words manually
        input_words = input().split()

        total_chars = word_count = 0
        for i in range(len(input_words)):
            is_valid = True

            # Remove period if present at the end
            if (input_words[i])[len(input_words[i])-1] == ".":
                input_words[i] = (input_words[i])[:len(input_words[i])-2]
            
            # Validate the word characters
            if not is_valid_word(input_words[i]):
                is_valid = False
            
            # Accumulate stats if valid word
            if is_valid == True:
                total_chars += len(input_words[i])
                word_count += 1
        
        # Calculate average characters per valid word
        avg = int(total_chars/word_count) if total_chars != 0 else 0

        # Output based on average character length
        if avg <= 3: 
            print(250)
        elif avg <= 5: 
            print(500)
        else: 
            print(1000)

    except EOFError:
        break