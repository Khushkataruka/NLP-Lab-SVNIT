import string
from automathon import NFA

def construct_word_nfa():
    """Constructs the Epsilon-NFA to recognize sequences of lowercase letters."""
    
    # Define the components of the NFA
    lowercase_letters = set(string.ascii_lowercase)
    
    # All characters that are not lowercase letters are considered invalid for the core automaton
    # Note: '_' and ' ' are handled separately by our custom processor
    invalid_chars = set(string.digits + string.ascii_uppercase + string.punctuation)
    
    q_states = {'q_start', 'q_ready', 'q_accept', 'q_dead'}
    sigma_alphabet = lowercase_letters.union(invalid_chars)
    sigma_alphabet.add('')
    q0_start = 'q_start'
    f_final = {'q_accept'}
    
    # Define transitions
    delta_transitions = {
        'q_start': {'': {'q_ready'}},
        'q_ready': {},
        'q_accept': {},
        'q_dead': {}
    }

    # From q_ready, any lowercase letter moves to the final state q_accept
    for char in lowercase_letters:
        delta_transitions['q_ready'][char] = {'q_accept'}
    
    # Any invalid character from q_ready moves to the dead state
    for char in invalid_chars:
        delta_transitions['q_ready'][char] = {'q_dead'}

    # From q_accept, any lowercase letter loops back to q_accept
    for char in lowercase_letters:
        delta_transitions['q_accept'][char] = {'q_accept'}
        
    # Any invalid character from q_accept moves to the dead state
    for char in invalid_chars:
        delta_transitions['q_accept'][char] = {'q_dead'}
        
    # The dead state loops on every character
    for char in sigma_alphabet:
        delta_transitions['q_dead'][char] = {'q_dead'}
        
    # Create and return the NFA object
    nfa = NFA(
        q=q_states,
        sigma=sigma_alphabet,
        delta=delta_transitions,
        initial_state=q0_start,
        f=f_final
    )
    return nfa

def process_string(input_str, nfa):
    """
    Processes a string according to the special rules (space, _)
    using the provided NFA as a validator.
    """
    # Rule: If '_' is encountered anywhere, the string is immediately invalid.
    if '_' in input_str:
        return "Not Accepted"

    # Extract the part of the string before the first space
    word_to_check = input_str.split(' ')[0]
    
    # Rule: Check if the extracted word exceeds th
        
    # Rule: Use the NFA to check if the word is a valid sequence of letters.
    # Also ensure the word is not empty (e.g., input was " dog" or just " ").
    if word_to_check and nfa.accept(word_to_check):
        return "Accepted"
    else:
        return "Not Accepted"
    
    