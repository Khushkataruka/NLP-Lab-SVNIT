import pandas as pd
from LAB_1.tokenizer import sentence_tokenizer, word_tokenizer
from news_utils import sentence_probability   

# ================================
# CONFIG
# ================================
TXT_FILE = "LAB_4/hindi_news_sentences.txt"   # use your saved text file

# ================================
# Load sentences from txt file
# ================================
def load_sentences():
    with open(TXT_FILE, "r", encoding="utf-8") as f:
        sentences = [line.strip() for line in f if line.strip()]
    return sentences

# ================================
# Process sentences
# ================================
def process_sentences(sentences):
    results = []
    for sent in sentences:
        probs = {
            "unigram_prob": sentence_probability(sent, model="unigram"),
            "bigram_prob": sentence_probability(sent, model="bigram"),
            "trigram_prob": sentence_probability(sent, model="trigram"),
            "quadgram_prob": sentence_probability(sent, model="quadgram"),
        }
        results.append({
            "sentence": sent,
            **probs
        })
    return results

# ================================
# MAIN
# ================================
if __name__ == "__main__":
    print("Loading Hindi sentences from txt file...")
    sentences = load_sentences()
    print(f"Loaded {len(sentences)} sentences.")

    print("Calculating sentence probabilities...")
    results = process_sentences(sentences)

    df = pd.DataFrame(results)
    df.to_csv("LAB_4/news_sentence_probs.csv", index=False, encoding="utf-8-sig")

    print("✅ Done. Saved to LAB_4/news_sentence_probs.csv")
