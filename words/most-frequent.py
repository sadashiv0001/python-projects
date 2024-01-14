# find the most frequent word in a file

from collections import Counter
import re

def most_frequent_word(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

    # Tokenize the text into words
    words = cleaned_text.split()

    # Use Counter to count the occurrences of each word
    word_counts = Counter(words)

    # Find the most common word and its count
    most_common_word, count = word_counts.most_common(1)[0]

    return most_common_word, count

#  path to the file
file_path = 'sadashiv.txt'
most_common_word, count = most_frequent_word(file_path)

print(f"The most frequent word is '{most_common_word}' with a count of {count} available in the file {file_path}.")
