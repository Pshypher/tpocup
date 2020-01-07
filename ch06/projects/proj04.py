# Affine Cipher Encryption Algorithm:
# Calculate M, the number of characters in the alphabet (Hint: use len())
# Calculate A using get_smallest_co_prime(M)
# For the character to be encrypted find its index in the alphabet: x in the
    # formula is the index
# Apply the formula to get the index of the cipher character:
    # E(x) = (Ax+N) mod M
# Using the index get the cipher character from the alphabet
# Return the character

# Affine Cipher Decryption Algorithm:
# Calculate M, the number of characters in the alphabet (Hint: use len())
# Calculate A using get_smallest_co_prime(M)
# Calculate A` using the function multiplicative_inverse(A, M)
# For the character to be decrypted find its index in the alphabet:
    # x in the formula is the index
# Apply the formula to get the index of the plaintext character:
    # D(x) = A`(x-N) mod M
# Using the index get the plaintext character from the alphabet
# Return the character

# Caeser cipher encryption and decryption algorithms 
# are similar to the Affine cipher algorithms
    # E(x) = (x+N) mod M
    # D(x) = (x-N) mod M

# Unless stated otherwise, variables are of the type int

import math,string
PUNCTUATION = string.punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
        Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Checks that both numbers are co-primes
        num: A number between (1, M) exclusive (int)
        M: The size of a sef of alphabet (int)
        Returns: True if both numbers are co-primes otherwise False (bool)'''
    
    return math.gcd(num, M) == 1
        
def get_smallest_co_prime(M):
    '''Gets the smallest co-prime of the number M 
        M: The size of a set of alphabets (int)
        Returns: the smallest coprime of M that is greater than 1 (int)'''
    
    a = 2
    while a < M:    # Loop through numbers 2 up to but excluding M
        if check_co_prime(a, M):
            return a
        a = a + 1
        
def caesar_cipher_encryption(ch,N,alphabet):
    '''Encrypts a character using the caesar cipher algorithm
        ch: character to encrypt (string)
        N: index size about which ch is rotated (int)
        alphabet: set of alphabets (string)
        Return: the cipher text character using caesar cipher (string)'''
    
    x = alphabet.find(ch)   # index of plain text character in the alphabet
                            # str, no offset from 0
    M = len(alphabet)
    cipher_text_sub = (x+N)%M
    cipher_text = alphabet[cipher_text_sub]
    return cipher_text

def caesar_cipher_decryption(ch,N,alphabet):
    '''Decrypts a character using the caesar cipher algorithm
        ch: character to decrypt (string)
        N: index size about which ch is rotated (int)
        alphabet: set of alphabets (string)
        Return: the plain text character using caesar cipher (string)'''
    
    x = alphabet.find(ch)
    M = len(alphabet)
    plain_text_sub = (x-N)%M
    plain_text = alphabet[plain_text_sub]
    return plain_text
        
def affine_cipher_encryption(ch,N,alphabet):
    '''Encrypts a character using the affine cipher algorithm
        ch: character to encrypt (string)
        N: index size about which ch is rotated (int)
        alphabet: set of alphabets (string)
        Return: the cipher text character using affine cipher (string)'''
    
    x = alphabet.find(ch)
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    cipher_text_sub = (A*x+N)%M
    cipher_text = alphabet[cipher_text_sub]
    return cipher_text

def affine_cipher_decryption(ch,N,alphabet):
    
    '''Decrypts a character using the affine cipher algorithm
        ch: character to decrypt (string)
        N: index size about which ch is rotated (int)
        alphabet: set of alphabets (string)
        Return: the plain text character using affine cipher (string)'''
    
    x = alphabet.find(ch)
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    A_inverse = multiplicative_inverse(A, M)
    plain_text_sub = A_inverse*(x-N)%M
    plain_text = alphabet[plain_text_sub]
    return plain_text
    
def main():    
    '''Prompts for a command_str (d,e,q), prompts for a string, decrypts or
        encrypts the string depending on the command_str using the encryption
        and decryption functions of the affine and caesar cipher algorithms'''
    
    is_integer = False
    while not is_integer:
        try:
            N = int(input("Input a rotation (int): "))
            is_integer = True
        except ValueError:
            print("Error; rotation must be an integer.")
          
    command_str = input("Input a command_str (e)ncrypt, (d)ecrypt, (q)uit: ")
    while command_str != 'q':
        if command_str == 'e':
            cipher_str = ""
            plain_text_str = input("Input a string to encrypt: ")
            for char in plain_text_str.lower():
                if char in ALPHA_NUM:
                    cipher_str += affine_cipher_encryption(char, N, ALPHA_NUM)
                elif char in PUNCTUATION:
                    cipher_str += caesar_cipher_encryption(char, N, PUNCTUATION)
                else:
                    print("Error with character:\nCannot encrypt this string.")
                    break
            else:
                print("Plain text: " + plain_text_str) 
                print("Cipher text: " + cipher_str)
        elif command_str == 'd':
            plain_text_str = ""
            cipher_str = input("Input a string to decrypt: ")
            for char in cipher_str.lower():
                if char in ALPHA_NUM:
                    plain_text_str += affine_cipher_decryption(char, N, ALPHA_NUM)
                elif char in PUNCTUATION:
                    plain_text_str += caesar_cipher_decryption(char, N, PUNCTUATION)
                else:
                    print("Error with character:\nCannot decrypt this string.")
                    break
            else:
                print("Cipher text: " + cipher_str)
                print("Plain text: " + plain_text_str)
        else:
            print("command_str not recognized.")
                
        command_str = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            
if __name__ == "__main__":
    main()