#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True



def sentence():
    u_sentence =''
    while (is_sentence(u_sentence) == False):
        u_sentence = input('Enter valid sentence ')
    
    words = u_sentence.split()
    word = []
    frequency = []
    #word.append(u_sentence.split())
    for i in range(len(words)):
        if check(word, words[i]):
            frequency[i] += 1
        else: 
            word.append(words[i])
            frequency.append(1)
        
    print (words)
    print (frequency)
    
sentence()
    
    
