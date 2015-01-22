#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_list = []
    markov_keys = []
    markov_dict = {}
    # f = open(corpus)
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
        #print markov_dict

    # for i in range(0,len(markov_list)-2):
    #     markov_keys.append((markov_list[i], markov_list[i+1]))

    # for t in range(0,len(markov_keys)-1):
    #     if markov_keys[t] not in markov_dict:
    #         markov_dict[markov_keys[t]] = [markov_keys[t+1][1]]
    #     else:
    #         markov_dict[markov_keys[t]].append(markov_keys[t+1][1])

    # markov_dict[markov_keys[-1]] = [markov_list[-1]]
    #print markov_dict
    # for word in markov_list:
    #     markov_dict[()]
    # if ('them,', 'Sam') in markov_dict:
    #     return True
    # else:
    #     return False
    #print len(markov_dict)
    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    current_key = random.choice(chains.keys())
    s = current_key[0] + " " + current_key[1]
    while current_key in chains:
        #print current_key
        next_word = random.choice(chains[current_key])
        #print next_word
        s = s + " " + next_word
        current_key = (current_key[-1], next_word)

    return s

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = open('suess.txt')

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    input_text.close()
    print random_text 

if __name__ == "__main__":
    main()
