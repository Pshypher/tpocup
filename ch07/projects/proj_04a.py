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


# Prompt user for a shift value. Caesar ciphers use a shift value of 3
shift_str = input("Enter a shift value: ")
shift_int = int(shift_str)
# Prompt the user for a plain text to encrypt
text = input("Enter text to encode: ")

cipher_text = encrypt(text, shift_int)
plain_text = decrypt(cipher_text, shift_int)

print()
print("Original text:",text)
print("Cipher text:",cipher_text)
print("Plain text:",plain_text)