import requests
import re
import pandas as pd

api_key = "8e774079b4594ba68e5e88fcd52ffa80"
url = "https://newsapi.org/v2/everything?"

# -----------------------------------------
# Utility: Clean and split text into sentences
# -----------------------------------------
def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"\[.*?\]", "", text)       # remove [... chars]
    text = re.sub(r"\s+", " ", text).strip()  # normalize spaces
    return text

def sentence_split(text):
    # Split on । (Hindi danda) or .
    return [s.strip() for s in re.split(r"[।.]", text) if len(s.strip()) > 5]

# -----------------------------------------
# Fetch News
# -----------------------------------------
def fetch_hindi_news(max_sentences=100):
    sentences = []
    page = 1

    while len(sentences) < max_sentences:
        params = {
            "q": "भारत",
            "language": "hi",
            "apiKey": api_key,
            "pageSize": 100,   # max allowed
            "page": page
        }
        response = requests.get(url, params=params)
        data = response.json()

        if "articles" not in data or not data["articles"]:
            break

        for article in data["articles"]:
            raw_text = " ".join([
                clean_text(article.get("title", "")),
                clean_text(article.get("description", "")),
                clean_text(article.get("content", ""))
            ])

            sents = sentence_split(raw_text)
            sentences.extend(sents)

            if len(sentences) >= max_sentences:
                return sentences[:max_sentences]

        page += 1

    return sentences[:max_sentences]

# -----------------------------------------
# MAIN
# -----------------------------------------
if __name__ == "__main__":
    hindi_sentences = fetch_hindi_news(100)
    print(f"✅ Collected {len(hindi_sentences)} Hindi sentences.\n")

    # Print to console
    for i, sent in enumerate(hindi_sentences, 1):
        print(f"{i}. {sent}")

    # Save to CSV
    df = pd.DataFrame(hindi_sentences, columns=["sentence"])
    df.to_csv("LAB_4/hindi_news_sentences.csv", index=False, encoding="utf-8-sig")
    print("📂 Saved to LAB_4/hindi_news_sentences.csv")

    # Save to TXT
    with open("LAB_4/hindi_news_sentences.txt", "w", encoding="utf-8") as f:
        for sent in hindi_sentences:
            f.write(sent + "\n")
    print("📂 Saved to LAB_4/hindi_news_sentences.txt")
