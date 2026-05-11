# Simple Markov Chain Text Generator Algorithm

## v1.0
This project is a very simple analyser and generator which feeds a corpus of data in, creating a transition matrix (a dictionary consisting of each unique word in the corpus as keys with the following word of each instance as values) which is then used with a first-order markov chain to generate a length of text.

To generate text, save a text file in utf-8 encoding with the name `corpus.txt` (there are 2 example corpus texts, they can be renamed for use).
Then on line 61 you can change the value to decide the length of the text output.
Run `main.py` and the text will be printed.