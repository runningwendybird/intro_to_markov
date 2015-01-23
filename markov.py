#!/usr/bin/env python

import sys
import random
from protectedwords import protec

MAX_TWITTER_LENGTH = 140

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_list = []
    markov_keys = []
    markov_dict = {}

    for l in corpus:
        line = l.strip()
        words = line.split(" ")
        for word in words:
            word = word.lower()
            markov_list.append(word)

    for i in range(0, len(markov_list)-2):
        if (markov_list[i], markov_list[i+1]) in markov_dict:
            markov_dict[(markov_list[i], markov_list[i+1])].append(markov_list[i+2])
        else:
            markov_dict[(markov_list[i], markov_list[i+1])] = [markov_list[i + 2]]

    for keys in markov_dict.keys():
        if '\r' in keys[0] or '\r' in keys[1]:
            del markov_dict[keys]

    return markov_dict


    # markov_dict(i, i+1) = markov_dict.get(i, i+1, []) + i+2

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # """Create markov list.

    # jhkh kjgfh kjfdgh kjfdhgkj hdfkjghskjdfh ksdjh fkjdsh fkjsd hfkjsdh fksdjh file_to_open
    # dsfkjsdhfjkdshfkjsdhfjksd.
    # """

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

def condition_text(string):

    """This function will take the generated
    string and turn format it into a more readable
    tweetable string."""

    s = string[0:MAX_TWITTER_LENGTH]

    if "!" in s or "?" in s or "." in s:
        exclam = s.rfind("!")
        question = s.rfind("?")
        period = s.rfind(".")
        punc = max([exclam, question, period])
        s = s[0 : punc + 1]
    else:
        space = s.rfind(" ")
        s = s[0 : space] + "."

    #s = s[0].upper() + s[1:]
    conditioning = s.split(" ")
    #print conditioning
    for word in conditioning:
        word = word.strip()
    conditioning[0] = conditioning[0][0].upper() + conditioning[0][1:]

    if conditioning[0][0].isalpha() == False:
        conditioning[0] = conditioning[0][0] + conditioning[0][1].upper() + conditioning[0][2:]

    for i in range(1,len(conditioning)):
        current = i
        next_char = i + 1
        prev_char = i - 1

        check = conditioning[current][0].upper() + conditioning[current][1:]

        if check in protec:
            conditioning[current] = check

        if conditioning[prev_char][-1] == "." or conditioning[prev_char][-1] == "?" or conditioning[prev_char][-1] == "!":
            conditioning[current] = conditioning[current][0].upper() + conditioning[current][1:]

        if conditioning[current] == "i":
            conditioning[current] == "I"

        s = ' '.join(conditioning)

    return s




def main():
    args = sys.argv

    script, file_to_open = args


    #input_text = open(raw_input("Enter file to open: "))
    input_text = open(file_to_open)
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    input_text.close()
    #print random_text[0:140]
    tweet = condition_text(random_text)
    print tweet
    #print len(tweet)

if __name__ == "__main__":
    main()
