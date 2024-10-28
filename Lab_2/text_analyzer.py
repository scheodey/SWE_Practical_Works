def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

# Exercises: Modify the program to count the number of unique words in the text.
# 1.Count unique words
def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

# Add a function to find the longest word in the text.
# 2.Longest word
def find_longest_word(content):
    words = content.split()
    longest_word = ""
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    return longest_word, longest_word_length

# Implement a feature to count the occurrences of a specific word (case-insensitive).
# 3.Count Occurrences of a Specific Word
def count_specific_word(content, repeated_word):
    words = content.lower().split()
    repeated_word = repeated_word.lower()
    return words.count(repeated_word)


def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# Create a function to calculate the percentage of words that are longer than the average word length.
# Calculating the percentage of words
def percentage_words(content):
    words = content.split()
    avg_length = average_word_length(content)
    
    # Count words longer than the average length
    longer_than_avg_count = 0
    for word in words:
        if len(word) > avg_length:
            longer_than_avg_count += 1
    
    # Calculate and return the percentage
    percentage = (longer_than_avg_count / len(words)) * 100
    return percentage


def analyze_text(filename, specific_word=None):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_words_count = count_unique_words(content)
    longest_word,longest_word_length = find_longest_word(content)
    percentage_avg = percentage_words(content)

    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Unique words: {unique_words_count}")
    print(f"The longest word is '{longest_word}' with {longest_word_length} characters")
    print(f"Percentage of words longer than average length: {percentage_avg:.2f}%")


     # Count and display the specific word occurrences if specified
    if specific_word:
        specific_word_count = count_specific_word(content, specific_word)
        print(f"Occurrences of '{specific_word}': {specific_word_count}")


# Run the analysis
analyze_text('sample.txt', specific_word='women')
