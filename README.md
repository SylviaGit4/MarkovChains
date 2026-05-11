# Simple Markov Chain Text Generator Algorithm

## Markov Chains
WARNING: This is not a detailed explanation of Markov Chains. This is my own interpetation of how to explain them.
Markov Chains, at least in the application of generating realistic (and occasionally coherent) text, work through the creation of a transition matrix from a given corpus (aka piece of data). 
The data is first tokenised to get a list of all words within the piece, before being placed into the matrix (in this case a dictionary in python). 
When placed into the matrix, each unique word is created as a key and then (in the case of a first order chain) each word following the individual instances of the key is recorded as a list.

Once the matrix is made the text can be generated from it, a starting word is chosen first and then randomly from the associated list of following words the next is chosen.
This process is repeated for the desired length of text to be generated, and usually results in semi-coherent text depending on the size of the corpus.
The process of generating the text itself is entirely based on probability as the transformnation matrix consists of a list of each individual instance of the following word, meaning that the word which appears most commonly following a particular word will appear more often after that word (e.g if the word "rain" followed the word "heavy" 5 times in the corpus, with only 1 instance of the word "light" following the word "heavy", it would be a 5/6 chance for the word "rain" to generate after the word "heavy".)

The process for second order chains (and 3rd and 4th and so on) is similar, but rather than just looking at the single word ahead of the current it looks two (or 3, 4, etc) ahead, allowing for the generated text to be more coherent and mirror the style of the corpus with greater accuracy, however at the cost of requiring a larger corpus to avoid generating text that is verbatim to the original.


## v1.0
This project is a very simple analyser and generator which feeds a corpus of data in, creating a transition matrix (a dictionary consisting of each unique word in the corpus as keys with the following word of each instance as values) which is then used with a first order markov chain to generate a length of text.

To generate text, save a text file in utf-8 encoding with the name `corpus.txt` or save it into the existing file with the same name (there is an example corpus text which can be renamed for use, by default the `savannah_example_corpus.txt` file is copied into `corpus.txt`).

Then on `line 61` you can change the value to decide the length of the text output.

Run `main.py` and the text will be printed.


## v1.1
Below the first order markov chain, there is code for a bigram markov chain. It feeds from the same text but you will need to comment out the print statement on line 64.
By default it is a second order, you can change the order on line `line 100`.

To generate text, save a text file in utf-8 encoding with the name `corpus.txt` or save it into the existing file with the same name (there is an example corpus text which can be renamed for use, by default the `savannah_example_corpus.txt` file is copied into `corpus.txt`).

Then on `line 100` and `line 101` you can change the value to decide the order and length of the text output.

Run `main.py` and the text will be printed.
