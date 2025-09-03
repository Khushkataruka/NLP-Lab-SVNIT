import pandas as pd
from collections import Counter
tokenized_path = "../LAB_1/tokenized_hindi.txt"

word_count = Counter()
print("Started Calculating.....\n")
with open(tokenized_path, 'r', encoding="utf-8") as f:
    for line in f:
        tokens = line.strip().split()
        word_count.update(tokens)
df = pd.DataFrame(list(word_count.items()), columns=["word", "freq"])


df.to_csv("word_freq.csv", index=False, encoding="utf-8")
print("Csv Saved.......")
print(df.head(10))  # show top 10 words
