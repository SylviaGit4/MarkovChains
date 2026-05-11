import string

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

transitions = {}

# stop at len -1 (last word has no successor)
for i in range(len(words) -1):
    current_word = words[i]
    next_word = words[i+1]

    # Check if key exists prior to appending.
    if current_word not in transitions:
        transitions[current_word] = []

    transitions[current_word].append(next_word)

print(transitions)