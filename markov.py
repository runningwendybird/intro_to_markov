#!/usr/bin/env python

import sys
import random
from protectedwords import WORDS_TO_CAPITALIZE
from tweetit import tweet_markov

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
    
    # Turning string into a list, so we can iterate through each word and make changes like 
    # capitalization that will improve the quality of the output. 

    words_to_fix = s.split(" ")
    
    # Iterating through the list and striping whitespace. 
    for word in words_to_fix:
        word = word.strip()
    
# Ensuring that the first word of the tweet is capitalized. Even if it starts with a quotation mark. 
    if words_to_fix[0][0].isalpha() == False:
        words_to_fix[0] = words_to_fix[0][0] + words_to_fix[0][1].upper() + words_to_fix[0][2:]
    else:
        words_to_fix[0] = words_to_fix[0][0].upper() + words_to_fix[0][1:]
    

# Loops through our current list of words and:
# 1 - Protected words: Checking for reserve words (nouns that should be capitalized) and ensuring they aren't put into lower case
# 2 - Title case: First letter of a sentence is capitalized
# 3 - "I"  pronoun: Ensuring that "I" or contractions that begin with "I" (I've, I'm, etc) are capitalized
    for i in range(1, len(words_to_fix)):

        prev_char, current, next_char = (i - 1, i + 0, i + 1)

        check = words_to_fix[current][0].upper() + words_to_fix[current][1:]

        if check in WORDS_TO_CAPITALIZE:
            words_to_fix[current] = check

        if words_to_fix[prev_char][-1] == "." or words_to_fix[prev_char][-1] == "?" or words_to_fix[prev_char][-1] == "!":
            words_to_fix[current] = check

        if words_to_fix[current] == "i":
            words_to_fix[current] == "I"
        if "i'" in words_to_fix[current]:
            words_to_fix[current] = check

# Now that we have checked the words, we are putting them back into a string. 
    s = ' '.join(words_to_fix)

    return s

def tweet_option(tweet_string):
    send_to_twitter = raw_input("Input 'y' to tweet this Markov Chain. ")
    if send_to_twitter.lower() == "y":
        tweet_markov(tweet_string)
    else:
        print "Alright, we won't post that one."


def main():
    args = sys.argv

    script, file_to_open = args


    #input_text = open(raw_input("Enter file to open: "))

    # FIXME: better var names for files/paths/context-text

    input_file = open(file_to_open)
    chain_dict = make_chains(input_file)
    random_text = make_text(chain_dict)
    input_file.close()
    #print random_text[0:140]
    tweet = condition_text(random_text)
    print tweet
    #print len(tweet)
    tweet_option(tweet)

if __name__ == "__main__":
    main()
