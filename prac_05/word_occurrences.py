"""
File: word_occurrences.py
Estimate: 15 minutes
Actual: 35 minutes
"""

# Ask user for input
text = input("Text: ")

# Split text into words
words = text.split()

# Create dictionary to store word counts
word_to_count = {}

# Count word occurrences
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Find the longest word length for formatting
max_word_length = max(len(word) for word in word_to_count)

# Print sorted word counts with aligned formatting
for word in sorted(word_to_count):
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
