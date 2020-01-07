# Unless stated otherwise, variables are assumed to be lists

import random
import string

def encrypt(plain_text, shift_value):
    """Encrypts a plain_text by shifting each character in the string
        by some amount shift_value to the right and replacing the character
        in the original text with the character at the new index calculated.
        Returns the cipher text, a string of encrypted words"""
    word_list = plain_text.split()
    
    for i, word in enumerate(word_list):
        encrypted_word = ""
        
        for char in word:
            if not char.isalpha():
                continue
            encrypted_word += encode_char(char.upper(), shift_value)
            
        word_list[i] = encrypted_word
        
    return ' '.join(word_list)

def decrypt(encrypted_text, shift_value):
    """Decrypts a plain_text by shifting each character in the string
        by some amount shift_value  to the left and replacing the character 
        in the original text with the character at the new index calculated.
        Returns the plain text."""
    word_list = encrypted_text.split()
    
    for i, word in enumerate(word_list):
        plain_text = ""
        
        for char in word:
            if not char.isalpha():
                continue
            plain_text += decode_char(char.upper(), shift_value)
            
        word_list[i] = plain_text
        
    return ' '.join(word_list)

def encode_char(ch, shift):
    """Replaces the character ch with another character from the english
        uppercase ascii alphabets shifting it from its position by some shift 
        amount index to the right. Returns a single string character."""
    plainCharIndex = string.ascii_uppercase.find(ch)
    cipherCharIndex = (plainCharIndex + shift) % 26
    
    return string.ascii_uppercase[cipherCharIndex]

def decode_char(ch, shift):
    """Replaces the character ch with another character from the english
        uppercase ascii alphabets shifting it from its position by some shift 
        amount index to the left. Returns a single string character."""
    cipherCharIndex = string.ascii_uppercase.find(ch)
    plainCharIndex = (cipherCharIndex - shift) % 26
    
    return string.ascii_uppercase[plainCharIndex]


def count_alphabets(cipher_str):
    """Counts the number of times each letter appears in a cipher text.
        Returns a list of the alphabets and the frequency of alphabets
        in the cipher string."""
    alphabets_count = [0 for i in range(len(string.ascii_uppercase))]
    
    for char in cipher_str:
        if char.isalpha():
            char = char.upper()
            sub = string.ascii_uppercase.find(char)
            alphabets_count[sub]+=1
            
    alphabet_count_pairs = [(alphabets_count[i], string.ascii_uppercase[i])
                                for i in range(len(string.ascii_uppercase))]
    return alphabet_count_pairs
            

def getWordString():
    """Reads in the content of a file into a whole string of words.
        Returns the entire string of words."""
    dataFile = open("gettysburg.txt", "r")
    wordString = ''             # start with an empty string of words
    for line in dataFile:
        wordString += line      # add each line of words to the word string
    dataFile.close()
    return wordString


# Code breaking via frequency analysis
# A random shift integer 1-26 is employed in encoding each character
# of the plain text

# Program written to determine the shift of a cipher text,
# decode the cipher text and output the decoded message.

# Prompt user for cipher text
cipher_str = encrypt(getWordString(),
                     random.randint(1,len(string.ascii_uppercase)))

frequency, letter = max(count_alphabets(cipher_str))  # The most occuring letter
                                                      # in the cipher_str
# Guess the shift used in creating the cipher string from 1-26 
for shift_int in range(1,len(string.ascii_uppercase)+1):
    if decode_char(letter, shift_int)=='E':
        break
print()
print("Shift:",shift_int)
print()
print(decrypt(cipher_str, shift_int))                
