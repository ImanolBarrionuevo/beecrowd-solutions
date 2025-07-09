"""
    Function to calculates the number of pages needed to fit the given words
    based on maximum lines per page and maximum characters per line.

    Parameters:
    - words: list of strings, each representing a word
    - max_lines: int, maximum number of lines per page
    - max_chars_pl: int, character limit per line

    Returns:
    - int: total number of pages required
    """
def count_pages(words, max_lines, max_chars_pl):
    line = 1 # Current line number on the page
    chars = 0 # Character count on the current line
    pages = 1 # Page counter

    for word in words:
        if chars > 0:
            # Add a space before the word if it's not the first
            if chars + len(word) + 1 > max_chars_pl:
                line += 1
                chars = len(word)
            else:
                chars += len(word) + 1
        else:
            # First word on the line
            chars += len(word)

        if line > max_lines:
            # Start a new page if line limit is exceeded
            pages += 1
            line = 1
            chars = len(word)

    return pages

while True:
    try:
        nums = input().split()
        words = input().split()

        max_lines = int(nums[1])
        max_chars_pl = int(nums[2])

        print(count_pages(words, max_lines, max_chars_pl))

    except EOFError:
        break