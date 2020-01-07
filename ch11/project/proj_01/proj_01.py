# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:43:24 2018

@author: Pshypher
"""

# program simulates a game of easthaven version of solitaire using both the 
# Deck and Card class from cards_test1.py
import cards
import copy

# naming protocol and data structures 
    # SUIT_COLOR is a dictionary
    # the tableau is a list of lists
    # each pile in the tableau is a list
    # the foundation is a dictionary
    # the stock is a Deck
    
SUIT_COLOR = {'b': ('\u2663','\u2660'), 'r': ('\u2666','\u2665')}

def set_up(tableau: list, stock: list):
    """Setup the game of easthaven. Returns a tuple of strings, 1. instructions
    on how easthaven solitaire is played, 2. help on list of commands used to
    play the game."""
    # shuffle deck of cards, place deck in stock and deal from stock 7 cards
    # each of the 7 cards is moved to each of the 7 columns in the tableau
    a_deck = cards.Deck()
    a_deck.shuffle()
    
    for index in range(21):
        a_card = a_deck.deal()
        if (index/7) < 2:
            a_card.flip_card()
        tableau[index%len(tableau)].append(a_card)
        
    while not a_deck.is_empty():
        stock.append(a_deck.deal())
        
    easthaven_rules = """Rules of Easthaven
Goal, move all the cards to the foundations
Foundation
        Built up by rank and by suit from Ace to King
Tableau
        Built down by rank and by alternating color
        The top card may be moved
        Complete or partial correctly ranked piles may be moved
        An empty spot may be filled with any card or correctly ranked pile
Stock
        Dealing from the deck moves 1 card to each Tableau spot.\n"""
        
    help_str = """Responses are:
        'f [row A]' to move the top card of row A to foundation
        'm [number of cards] [row A] [row B]' to move a certain number of cards
from row A to row B
        'd' to deal cards
        'q' to quit """
        
    return easthaven_rules, help_str

    
def foundation_filled(foundation: dict) -> bool:
    '''Checks if the piles for each suit(club,diamond,heart,spades) in the
    foundation are already filled up in order of card ranks(from "ace" up until
    "king"). Returns a boolean value'''
    # check if all 13 ranked cards are present in order from ace,2,3,...,king
    # for each suit in the foundation
    for suit in foundation:
        if len(foundation[suit]) < 13:
            filled_bool = False
            break
    else:
        filled_bool = True
        
    return filled_bool

def get_ranked_piles(pile_list: list) -> list:
    '''Gets all possible partial correctly ranked piles in a column including
    a complete ranked pile of the column. Returns a list of lists'''
    all_possible_ranked_piles = [[pile_list[-1]]]

    for j in range(len(pile_list)-2,-1,-1):
        if pile_list[j].is_face_up():  # card at index j in pile is correctly 
                                    # ranked and facing up?
            # add another partial correctly ranked pile to list of ranked piles
            all_possible_ranked_piles.append(
                    [pile_list[j]] + copy.copy(all_possible_ranked_piles[-1]))
        else:
            break
        
    return all_possible_ranked_piles

def is_move_possible(a_card: cards.Card, other_columns_list: list) -> bool:
    '''Checks if a_card can be placed at the top of any of the piles in the 
    other_columns_list. Returns a boolean value'''
    possible_move = False
    
    for column in other_columns_list:
        top_card = column[-1]
        for color,suits in SUIT_COLOR.items():
            if a_card.suit() in suits and top_card.suit() not in suits and \
            top_card.rank()-a_card.rank()==1:
                possible_move = True
                break
        if possible_move:
            break

    return possible_move
                
def no_card_move(tableau: list, stock: list) -> bool:
    '''Checks whether the stock is empty and moves within the tableau is no 
    longer possible. Returns a boolean value.'''
    # loop through each column selecting a card at the top of each pile, 
    # a partial correctly ranked pile or a complete pile and try to assert
    # that no valid move to a different column in tableau is possible
    no_moves_bool = True
    for i,column in enumerate(tableau):
        # get all possible ranked pile list from a column in tableau
        ranked_piles_list = get_ranked_piles(column)
        tableau.remove(column)  # exclude ith column
        for pile in ranked_piles_list:
            a_card = pile[0]
            if is_move_possible(a_card, tableau):
                tableau.insert(i, column)   # insert ith column back to tableau
                no_moves_bool = False
                break
        if not no_moves_bool:
            break
        tableau.insert(i, column)   # insert ith column back to tableau             
        
    return no_moves_bool and len(stock) == 0

def fetch_pile(tableau: list,row_int: int,num_cards: int) -> list:
    '''Prompts user for the position of a card in a column of the tableau and
    selects all the cards facing up from that position up until the top most
    card. Returns a tuple of a pair an integer and list of Cards.''' 
    base_card_position = num_cards*-1
    if tableau[row_int][base_card_position].is_face_up():
        card_pile = tableau[row_int][base_card_position:]
    else:
        card_pile = []
    
    return card_pile

def is_proper_rank(tableau: list,a_card: cards.Card,row_int: int) -> bool:
    '''Checks if a_card can be placed on top of the pile of card(s) in tableau
    column column_int.'''
    # card at the top of the column pile in tableau
    empty_row_bool = len(tableau[row_int])==0
    if not empty_row_bool:
        row_top_card = tableau[row_int][-1]
        for color,suits in SUIT_COLOR.items():    
            alternate_colors_bool = a_card.suit() in suits and \
            row_top_card.suit() not in suits
            if alternate_colors_bool:
                break
        
        decrease_by_one_bool = a_card.rank()-row_top_card.rank()==-1
    
    return alternate_colors_bool and decrease_by_one_bool or empty_row_bool

def move_within_tableau(tableau: list,num_cards: int,source_row: int,
                        target_row: int) -> None:
    '''Move card within tableau.'''   
    
    target_row = target_row - 1
    source_row = source_row -1
    
    # select a card or partial correctly ranked sequence of cards from column
    card_pile = fetch_pile(tableau, source_row, num_cards)
    
    try:
        # card at the bottom of the pile of the source row in tableau
        base_card_source_row = card_pile[0]
    except IndexError:
        print("invalid move")
        
    # is the move of the pile to the destination possible?
    if is_proper_rank(tableau,base_card_source_row,target_row) and card_pile:
        # remove pile from column
        tableau[source_row][num_cards*-1:] = []
        # place pile at a different column
        tableau[target_row].extend(card_pile)
    else:
        print("invalid move")

def move_to_foundation(tableau: list, foundation: dict, row_int: int) -> None:
    '''Move card from tableau to foundation.'''
    
    row_int = row_int - 1
    
    a_card = tableau[row_int].pop()  # remove card from tableau
    
    # place the card at the correct suit position in the foundation only if it 
    # is 1 greater than the exposed card in the suit position in the foundation
    suit_list = foundation[a_card.suit()]
    # card is an ace and the row for the suit is empty,move ace to the row
    # of the ace's suit in the foundation
    if a_card.rank()==1 and len(suit_list)==0:
        suit_list.append(a_card)    
                                    #  
    elif len(suit_list)>0 and a_card.rank()-suit_list[-1].rank()==1:
        suit_list.append(a_card)    # move card to foundation
    else:
        print("invalid move")
        tableau[row_int].append(a_card)  # move card back into tableau if 
                                        # both conditions above are False
    
def deal_from_stock(stock: list, tableau: list) -> None:
    '''Moves a card from the stock to the top of the pile in each column of 
    the tableau.'''
    for i in range(len(tableau)):  
        if len(stock) > 0:
            card_from_stock = stock.pop()
            tableau[i].append(card_from_stock)
        else:
            print("Can no longer deal card from stock, stock is empty.")
            
def flip_upper_card(row: list) -> None:
    """Flips the upper card at the top of pile if it isn't facing up."""
    upper_card = row[-1]
    if not upper_card.is_face_up():
        upper_card.flip_card()
        
def display(tableau: list, foundation: dict, stock: list):
    '''Displays cards in the tableau, and foundation.'''
          
    print("\nTableau:")
    # print(tableau)
    for i in range(len(tableau)):
        flip_upper_card(tableau[i])
        print("Row {:02d}: ".format(i+1), end=' ')
        cards_in_column_str = ''
        for card in tableau[i]:
            cards_in_column_str += str(card) + ' '
        cards_in_column_str = cards_in_column_str.rstrip()
        print(cards_in_column_str) 
    
    print('-'*10)
        
    print("Foundation:")
    for suit,cards_list in foundation.items():
        print("Row {}: ".format(suit), end=' ')
        suit_cards_str=''
        for card in cards_list:
            suit_cards_str += str(card) + ' '
            
        suit_cards_str = suit_cards_str if suit_cards_str else "Empty"
        print(suit_cards_str)
       
    print()
    print('-'*10)
    print("Stock:", len(stock), "cards left.")
    
def is_valid(cmd_str):
    """Checks the command entered. Returns a boolean value."""
    fields = cmd_str.split()
    if fields[0] == 'm' and len(fields) == 4:
        for char in fields[1:]:
            if not char.isdigit():
                valid_cmd_bool = False
                break
        else:
            valid_cmd_bool = True 
    elif fields[0] == 'f' and len(fields) == 2 and fields[-1].isdigit():
        valid_cmd_bool = True
    elif len(fields) == 1 and (fields[0] == 'd' or fields[0] == 'q' or \
    fields[0] == 'h'):
        valid_cmd_bool = True
    else:
        valid_cmd_bool = False
        
    return valid_cmd_bool
         
def play():
    stock = []
    tableau = [[] for i in range(7)]
    foundation = {'\u2663': [],'\u2666': [],'\u2665': [],'\u2660': []}
    
    easthaven_rules, help_str = set_up(tableau,stock)  # set up tableau and 
                                                # add cards to stock
    # while moves within the tableau are still possible and  the stock is not empty
    # or all the piles of each suit in the foundation ranked in order from 
    # ace,2,3-king isn't filled, repeatedly prompt the user for a command to
        # move within tableau
        # move to foundation
        # deal from stock
    
    prompt_str = '\n\nCommand:(type \'h\' for help) '
    print(easthaven_rules)
    print(help_str)
    
    while True:
        # is the foundation filled?
        filled_bool = foundation_filled(foundation)
        no_more_card_moves = no_card_move(tableau, stock)
        
        if filled_bool or no_more_card_moves:
            if filled_bool:
                print("You've won")
            else:
                print("You've lost!!!")
                print("No more moves can be made")
            break
        
        display(tableau, foundation, stock)
        # prompt user for a command
        cmd_str = input(prompt_str).lower()
            
        if is_valid(cmd_str):   # parse command
            fields = cmd_str.split() 
            if fields[0] == 'm':
                move_within_tableau(tableau,int(fields[1]),int(fields[2]),
                                    int(fields[3]))
            elif fields[0] == 'f':
                move_to_foundation(tableau,foundation,int(fields[1]))
            elif fields[0] == 'd':
                deal_from_stock(stock, tableau)
            elif fields[0] == 'h':
                print(help_str)
            else:
                print("Thanks for playing")
                break
        else:
            print("Unknown command: {}".format(cmd_str))
            
if __name__ == "__main__":
    play()