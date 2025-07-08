# Continuously process input strings until EOF
while True:
    try:
        text = input() # Read input line

        # Apply character replacements using built-in string methods
        text = text.replace("O", "0").replace("o", "0")
        text = text.replace("l", "1").replace(",", "").replace(" ", "")

        # Check if resulting string is a valid integer
        if text.isdigit():
            number = int(text)
            # Validate integer size against 32-bit signed max value
            if number > 2147483647:
                print("error")
            else:
                print(number)
        else:
            print("error")

    except EOFError:
        break