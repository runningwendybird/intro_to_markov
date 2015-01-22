#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_list = []
    markov_keys = []
    markov_dict = {}


    for l in corpus:
        line = l.rstrip()
        words = line.split(" ")
        for word in words:
            markov_list.append(word)

    for i in range(0, len(markov_list)-2):
        if (markov_list[i], markov_list[i+1]) in markov_dict:
            markov_dict[(markov_list[i], markov_list[i+1])].append(markov_list[i+2])
        else:
            markov_dict[(markov_list[i], markov_list[i+1])] = [markov_list[i + 2]]

    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    current_key = random.choice(chains.keys())
    s = current_key[0] + " " + current_key[1]
    count = 0
    while current_key in chains and count < 150:
        #print current_key
        next_word = random.choice(chains[current_key])
        #print next_word
        s = s + " " + next_word
        current_key = (current_key[-1], next_word)
        count = count + 1
    return s

def main():
    args = sys.argv

 
    input_text = open(raw_input("Enter file to open: "))

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    input_text.close()
    print random_text 

if __name__ == "__main__":
    main()
