import numpy as np

# Initialize variables
total_sentences = 0
total_words = 0
total_characters = 0
unique_tokens = set()

# Open and read the file
with open('tokenized_hindi.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # i. Total number of sentences
        total_sentences += 1
        
        # Strip leading/trailing whitespace and split the line into words
        words = line.strip().split()
        
        # ii. Total number of words
        total_words += len(words)
        
        # Add words to the set of unique tokens
        unique_tokens.update(words)
        
        # iii. Total number of characters
        for word in words:
            total_characters += len(word)

# iv. Average Sentence Length
average_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

# v. Average word length
average_word_length = total_characters / total_words if total_words > 0 else 0

# vi. Type/Token Ratio (TTR)
ttr = len(unique_tokens) / total_words if total_words > 0 else 0

# Print the results
print(f"i. Total number of sentences: {total_sentences}")
print(f"ii. Total number of words: {total_words}")
print(f"iii. Total number of characters: {total_characters}")
print(f"iv. Average Sentence Length: {average_sentence_length:.2f}")
print(f"v. Average word length: {average_word_length:.2f}")
print(f"vi. Type/Token Ratio (TTR): {ttr:.8f}")