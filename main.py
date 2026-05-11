import string
import random

def tokenise_file():
    # Opens file, specifying utf-8
    with open("corpus.txt", encoding="utf-8-sig") as f:
        text = f.read()

    # Convert to lowercase & split on whitespace to get word list.
    text = text.lower()
    text = text.split()

    words = [
        w.strip(string.punctuation)
        for w in text
        if w.strip(string.punctuation)
    ]
    return words

words = tokenise_file()

## BELOW IS THE SECTION RELATED TO THE FIRST ORDER MARKOV CHAIN ##

def create_transition_matrix(words):
    transitions = {}

    # stop at len -1 (last word has no successor)
    for i in range(len(words) -1):
        current_word = words[i]
        next_word = words[i+1]

        # Check if key exists prior to appending.
        if current_word not in transitions:
            transitions[current_word] = []

        transitions[current_word].append(next_word)

    return transitions

transition_matrix = create_transition_matrix(words)

## Testing for the transition matrix
# for word, followers in transition_matrix.items():
#    print(f"'{word} -> {followers}")
# print(len(transition_matrix), "unique keys")

def generate_markov_chain(transition_matrix, num_words):
    current_word = random.choice(list(transition_matrix.keys()))
    output = [current_word]

    for _ in range(num_words -1):
        if current_word not in transition_matrix:
            # dead end restart
            current_word = random.choice(list(transition_matrix.keys()))
        else:
            current_word = random.choice(transition_matrix[current_word])
        output.append(current_word)
    
    return " ".join(output)

length_of_text = 100 # CHANGE TO CHANGE LENGTH OF OUTPUT

generated_text = generate_markov_chain(transition_matrix, length_of_text)
#print(generated_text) # Comment out if you want to use the bigram chain.


## BELOW IS THE SECTION RELATED TO THE SECOND ORDER MARKOV CHAIN ##

def build_ngram_transition(words, order):
    transitions = {}

    for i in range(len(words) - order):
        # state is a tuple of 'order' words
        state = tuple(words[i : i + order])
        next_word = words[i + order]

        if state not in transitions:
            transitions[state] = []
        transitions[state].append(next_word)

    return transitions

def generate_ngram_chain(transitions, order, num_words):
    state = random.choice(list(transitions.keys()))
    output = list(state)

    for _ in range(num_words - order):
        if state not in transitions:
            state = random.choice(list(transitions.keys()))
            output.extend(list(state))
        else:
            next_w = random.choice(transitions[state])
            output.append(next_w)
            # slide window forward
            state = tuple(output[-order:])
        
    return " ".join(output)

    
order = 2 # Modify this number for higher or lower orders (see explanation of markov chain in README to understand). 
num_words = 100 # Modify this number to change the amount of words generated in the text
transitions = build_ngram_transition(words, order)

generated_ngram = generate_ngram_chain(transitions, order, num_words)
print(generated_ngram) # Comment out if you want to use the first order chain.
