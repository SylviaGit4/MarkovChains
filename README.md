# Simple Markov Chain Text Generator Algorithm

## v1.0
This project is a very simple analyser and generator which feeds a corpus of data in, creating a transition matrix (a dictionary consisting of each unique word in the corpus as keys with the following word of each instance as values) which is then used with a first order markov chain to generate a length of text.

To generate text, save a text file in utf-8 encoding with the name `corpus.txt` or save it into the existing file with the same name (there are 2 example corpus texts, they can be renamed for use, by default the `seraphim_corpus.txt` file is copied into `corpus.txt`).

Then on `line 61` you can change the value to decide the length of the text output.

Run `main.py` and the text will be printed.


## v1.1
Below the first order markov chain, there is code for a bigram markov chain. It feeds from the same text but you will need to comment out the print statement on line 64.
By default it is a second order, you can change the order on line 

To generate text, save a text file in utf-8 encoding with the name `corpus.txt` or save it into the existing file with the same name (there are 2 example corpus texts, they can be renamed for use, by default the `seraphim_corpus.txt` file is copied into `corpus.txt`).

Then on `line 100` and `line 101` you can change the value to decide the order and length of the text output.

Run `main.py` and the text will be printed.
