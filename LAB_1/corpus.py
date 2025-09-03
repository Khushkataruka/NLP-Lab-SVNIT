import numpy as np
import pandas as pd

total_sentences = 0
total_words = 0
total_characters = 0
unique_tokens = set()

# Open and read the file
with open('LAB_1/tokenized_hindi.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total_sentences += 1
        words = line.strip().split()
        
        total_words += len(words)
        unique_tokens.update(words)
        
        for word in words:
            total_characters += len(word)


average_sentence_length = total_words / total_sentences if total_sentences > 0 else 0


average_word_length = total_characters / total_words if total_words > 0 else 0


ttr = len(unique_tokens) / total_words if total_words > 0 else 0

results = {
    "Total Sentences": total_sentences,
    "Total Words": total_words,
    "Total Characters": total_characters,
    "Average Sentence Length": round(average_sentence_length, 2),
    "Average Word Length": round(average_word_length, 2),
    "Type/Token Ratio (TTR)": round(ttr, 8)
}

df = pd.DataFrame([results])


df.to_csv("hindi_text_statistics.csv", index=False, encoding="utf-8")

print("✅ Statistics saved to LAB_1/corpus.csv")
