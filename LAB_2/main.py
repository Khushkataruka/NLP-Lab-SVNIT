from automata import construct_word_nfa,process_string


def main():
    nfa = construct_word_nfa()
    if nfa.is_valid()==False:
        print("NFA IS NOT VALID")

    with open("brown_nouns.txt", "r", encoding="utf-8") as file:
        for line in file:
            word= line.strip()
            print(word)
            if(word):
                res=process_string(word,nfa=nfa)
                print(res+ "\n")

main()