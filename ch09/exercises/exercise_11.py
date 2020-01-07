# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:55:01 2018

@author: Pshypher
"""
import string


def build_cipher_dictionary(shift_int):
    '''Maps plain text letters to the corresponding encryption characters. '''
    cipher_alphabets = ''
    for char in string.ascii_lowercase:
        # calculate the position by which each plain character should be
        # shifted by 
        shift_char_index = (string.ascii_lowercase.find(char) + shift_int) % len(
                string.ascii_lowercase)
        cipher_alphabets = cipher_alphabets + string.ascii_lowercase[
                shift_char_index]
        
    cipher_dict = dict(zip(cipher_alphabets,string.ascii_lowercase))
    return cipher_dict

    
def caeser_cipher_encryption(text_str, cipher_dict):
    '''Encrypts plain text characters using caesar cipher. Space characters
    are not encrypted.Returns a string'''
    
    # create a dictionary that maps cipher characters to plain text values
    alphabets_list = list(cipher_dict.values())
    cipher_alphabets_list = list(cipher_dict.keys())
    cipher_to_plain_dict = dict(zip(alphabets_list,cipher_alphabets_list))
    cipher_text = ''    # initialize cipher text to an empty string 
    # convert each plain text character
    for char in text_str:
        char = char.lower()
        if char in string.ascii_lowercase:
            cipher_text = cipher_text + cipher_to_plain_dict[char]
        else:
            cipher_text = cipher_text + char
    
    return cipher_text

def caeser_cipher_decryption(cipher_text, cipher_dict):
    '''Decrypts a cipher text to plain text. Returns a string.'''
    
    plain_text = ''     # initialize plain text to an empty string
    for char in cipher_text:
        if char in string.ascii_lowercase:
            plain_text = plain_text + cipher_dict[char]
        else:
            plain_text = plain_text + char
        
    return plain_text
        

def main():
    command_str = input("(e)ncrypt, (d)ecrypt: ")
    text_str = input("Text to be encrypted or decrypted: ")
    shift_str = input("Enter integer shift: ")
    shift_int = int(shift_str)
    cipher_dict = build_cipher_dictionary(shift_int)
    print(cipher_dict)
    
    if command_str == 'e':    
        print("Plain text:", text_str)
        print("Cipher text:", caeser_cipher_encryption(text_str, cipher_dict))
    else:
        print("Cipher text:",text_str)
        print("Plain text:",caeser_cipher_decryption(text_str, cipher_dict))
    
if __name__ == '__main__':
    main()
