# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:15:30 2018

@author: Pshypher
"""
# Program uses morse code dictionary to translate between morse code,
# characters and digits

def translate_morse_code(morse_code_char):
    '''Translates a morse code character to alphabets and digits.'''
    for key, val in morse_code_dict.items():
        if val == morse_code_char:
            return key
        
def translate_ascii_char(ascii_char):
    '''Translates an ascii character to a string morse code characters.'''
    try:
        ascii_char = ascii_char.upper()
        morse_code_char = morse_code_dict[ascii_char]
    except AttributeError:
        morse_code_char = morse_code_dict[ascii_char]
        
    return morse_code_char

def characters_to_morse_code(phrase):
    morse_code_str = ''
    for char in phrase:
        if char.isalpha():
            # single space char is used to seperate letters, double space chars 
            # between words
            morse_code_str += translate_ascii_char(char) + ' '
        else:
            morse_code_str += ' '
            
    morse_code_str = morse_code_str.strip()
    return morse_code_str

def morse_code_to_characters(morse_code_str):
    '''Converts a sequence of morse code characters to a sequence of alphabets 
    and digits.'''
    clause = ''
    words_list = morse_code_str.split('  ')
    for word in words_list:
        characters_list = word.split()
        for char in characters_list:
            clause += translate_morse_code(char)
        clause += ' '
            
    return clause.strip()

morse_code_dict = {'A': ".-", 'B': "-...",'C': "-.-.",'D': "-..",'E': '.',
                   'F': "..-.",'G': "--.",'H': "....",'I': "..",'J': ".---",
                   'K': "-.-",'L': ".-..",'M': "--",'N': "-.",'O': "---",
                   'P': ".--.",'Q': "--.-",'R': ".-.",'S': "...",'T': '-',
                   'U': "..-",'V': "...-",'W':".--",'X': "-..-",'Y': "-.--",
                   'Z': "--..",1: ".----",2: "..---",3: "...--",4: "....-",
                   5: ".....",6: "-....",7: "--...",8: "---..",9: "----.",
                   0: "-----"}
translate_ascii_text = input("Do you wish to translate text to morse code(y/n): ")
if translate_ascii_text == 'y':
    phrase = input("Enter text you wish to convert: ")
    print(characters_to_morse_code(phrase))
decode_morse_code = input("Do you wish to convert morse code msg to text\
                             (y/n): ")
if decode_morse_code == 'y':
    morse_code_str = input("Enter sequence of morse code chars: ")
    print(morse_code_to_characters(morse_code_str))
