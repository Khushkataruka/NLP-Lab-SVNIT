def analyze_noun(word):
    # Plural endings handled
    if word.endswith("es"):
        # Check for rule 1 (E insertion)
        if any(word[:-2].endswith(suffix) for suffix in ["s", "z", "x", "ch", "sh"]):
            root = word[:-2]
            return f"{word} = {root}+N+PL"
        elif word[-3]=='e' and len(word) > 3:
            return f"{word} = {word}+N+SL"
        else:
            return f"{word}=Invalid Word"
    elif word.endswith("ies"):
        # Rule 2 (Y replacement)
        root = word[:-3] + "y"
        return f"{word} = {root}+N+PL"
    elif word.endswith("ess"):
        return f"{word}={word[:-3]}+N+SG"
    elif word.endswith("s"):
        # Rule 3 (S addition) - avoid false positives like "is"
        root=word[:-1]
        if any(root.endswith(suffix) for suffix in ["s", "z", "x", "ch", "sh"]):
            return f"{word}-Invalid Word"
    
        if root.isalpha() and len(root) > 0:
            return f"{word} = {root}+N+PL"
        else:
            return f"{word}-Invalid Word"
    else:
        # Singular form
        return f"{word} = {word}+N+SG"


# File paths
nouns_file = "brown_nouns.txt"
results_file = "results.txt"
output_file = "fst_output.txt"

results = []

# Read both files in parallel
with open(nouns_file, "r", encoding="utf-8") as f_nouns:
    
        noun = f_nouns.strip()

        results.append(analyze_noun(noun))

# Save results
with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(results))

print(f"✅ FST processing complete! Output saved to {output_file}")
