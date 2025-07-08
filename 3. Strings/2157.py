# Read number of test cases
count = int(input())
results = []

# Process each test case
for i in range(count):
    nums = input().split()
    start = int(nums[0])
    end = int(nums[1])

    sequence = ''
    
    # Generate sequence of numbers from start to end (inclusive)
    while start <= end:
        sequence += str(start)
        start += 1

    sequence += sequence[::-1] # Create mirrored string by appending reverse of the sequence
    results.append(sequence) # Store the result

# Print each result on a new line
for output in results:
    print(output)