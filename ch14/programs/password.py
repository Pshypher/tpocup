# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:11:09 2018

@author: Pshypher
"""

from password_manager import *

def main():
    pm = PassManager({'bill':'$4Donuts', 'rich':'123ABC!'})
    
    max_tries = 3   # three tries allowed
    cnt = max_tries
    valid_bool = False
    while cnt > 0 and not valid_bool:
        user_str = input('User name:')
        try:
            valid_bool = pm.validate(user_str)  # validate prompts for password
        except NameException:
            print('Bad name!')
        except UserException:
            if input('No such name, add as new user (Y or y)? ') in 'Yy':
                try:
                    pm.add_user(user_str)
                    # only get here if no exceptions raised in add_user
                    valid_bool = True
                except NameException:
                    print('Bad name!')
                except UserException:
                    print('User already exists!')
                except PasswordException:
                    print('Bad password!')
        finally:
            cnt -= 1
    if not valid_bool:
        print('Session timed out.')
    else:
        print('Welcome user',user_str)
        
        