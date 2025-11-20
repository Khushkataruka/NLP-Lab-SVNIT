#include <bits/stdc++.h>

using namespace std;

struct TrieNode
{
    unordered_map<char, TrieNode *> children;
    int count; // frequency count
    bool is_end;
    TrieNode() : count(0), is_end(false) {}
};

class Trie
{
public:
    TrieNode *root;
    Trie()
    {
        root = new TrieNode();
    }

    void insert(const string &word)
    {
        TrieNode *node = root;
        for (char c : word)
        {
            if (!node->children[c])
            {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->count++;
        }
        node->is_end = true;
    }

    pair<string, string> find_split(const string &word)
    {
        TrieNode *node = root;
        int best_index = 0;
        double best_score = -1.0;

        for (int i = 0; i < (int)word.size(); i++)
        {
            char c = word[i];
            if (!node->children[c])
                break;
            node = node->children[c];

            int branching = (int)node->children.size();
            double prob = (node->count > 0) ? (double)branching / node->count : 0.0;

            if (prob > best_score)
            {
                best_score = prob;
                best_index = i + 1;
            }
        }

        string stem = word.substr(0, best_index);
        string suffix = word.substr(best_index);
        return {stem, suffix};
    }
};

bool isPluralSuffix(const string &suffix)
{
    return (suffix == "s" || suffix == "es");
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Load nouns
    vector<string> words;
    ifstream infile("../LAB_2/brown_nouns.txt");
    if (!infile.is_open())
    {
        cerr << "Error: Could not open brown_nouns.txt\n";
        return 1;
    }

    string w;
    while (infile >> w)
    {
        words.push_back(w);
    }

    if (words.empty())
    {
        cerr << "Error: No words found in brown_nouns.txt\n";
        return 1;
    }

    cout << "Loaded " << words.size() << " words\n\n";

    // Build prefix and suffix tries
    Trie prefixTrie, suffixTrie;
    for (auto &word : words)
    {
        prefixTrie.insert(word);

        string rev = word;
        reverse(rev.begin(), rev.end());
        suffixTrie.insert(rev);
    }

    int prefixCorrect = 0, suffixCorrect = 0, pluralWords = 0;

    cout << "Prefix Trie Splits (with probability measure):\n";
    for (auto &word : words)
    {
        string stem = prefixTrie.find_split(word).first;
        string suffix = prefixTrie.find_split(word).second;
        cout << word << " = " << stem << "+" << suffix << "\n";
        if (isPluralSuffix(suffix))
            prefixCorrect++;
        if (word.size() > 1 && (word.back() == 's'))
            pluralWords++;
    }

    cout << "\nSuffix Trie Splits (with probability measure):\n";
    for (auto &word : words)
    {
        string rev = word;
        reverse(rev.begin(), rev.end());

        string stem = suffixTrie.find_split(rev).first;
        string suffix = suffixTrie.find_split(rev).second;
        reverse(stem.begin(), stem.end());
        reverse(suffix.begin(), suffix.end());

        cout << word << " = " << stem << "+" << suffix << "\n";
        if (isPluralSuffix(suffix))
            suffixCorrect++;
    }

    cout << "\n--- Evaluation ---\n";
    cout << "Total plural words (ending with 's'/'es'): " << pluralWords << "\n";
    cout << "Prefix Trie correct splits: " << prefixCorrect << "\n";
    cout << "Suffix Trie correct splits: " << suffixCorrect << "\n";

    double prefixAcc = (pluralWords > 0) ? (100.0 * prefixCorrect / pluralWords) : 0.0;
    double suffixAcc = (pluralWords > 0) ? (100.0 * suffixCorrect / pluralWords) : 0.0;

    cout << "Prefix Trie Accuracy: " << prefixAcc << "%\n";
    cout << "Suffix Trie Accuracy: " << suffixAcc << "%\n";

    if (suffixAcc > prefixAcc)
        cout << "Conclusion: Suffix Trie is better for detecting plural forms.\n";
    else
        cout << "Conclusion: Prefix Trie is better.\n";

    return 0;
}