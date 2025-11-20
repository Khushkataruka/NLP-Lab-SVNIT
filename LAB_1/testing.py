from tokenizer import word_tokenizer

text="भारत। संस्कृत। यह. एक, अद्भुत देश है।"
sentences = word_tokenizer(text)
print(sentences)
# Output: ['भारत', 'संस्कृत', 'यह', 'एक', 'अद्भुत', 'देश', 'है']