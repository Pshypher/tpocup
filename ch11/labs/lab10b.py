
import cards

# Constants
HANDS_SIZE = 5
PAIR = 2

def setup():
    """Creates a deck of cards, shuffles the deck and deals both players equal
    amount of cards."""
    # Create the deck of cards
    the_deck = cards.Deck()
    the_deck.shuffle()
    
    players_dict = dict(player1=[], player2=[])
    
    for i in range(HANDS_SIZE):
        players_dict["player1"].append(the_deck.deal())
        players_dict["player2"].append(the_deck.deal())
        
    return players_dict

def break_tie(player1_card: cards.Card,player2_card: cards.Card,
              players_dict: dict):
    """Using the rules of the game "Battle", the winner of the game is selected
    from a tie. Returns a tuple"""
    cards_removed = [player1_card, player2_card]
    # Repeatedly turn over two other cards in each players hand if both player
    # card ranks are equal and both players still has cards left in hand
    while player1_card.rank()==player2_card.rank():
        player1_card_pair = []
        player2_card_pair = []
        empty_hand_bool = True
        for i in range(PAIR):
            # No card in either or both player's hand?
            if not players_dict["player1"] or not players_dict["player2"]:
                break
            else:                
                player1_card_pair.append(players_dict["player1"].pop(0))
                player2_card_pair.append(players_dict["player2"].pop(0))
        else:
            player1_card = player1_card_pair[-1]
            player2_card = player2_card_pair[-1]
            empty_hand_bool = False
            
        cards_removed.extend(player1_card_pair + player2_card_pair)
        if empty_hand_bool:
            break
    # Unequally ranked cards in each player's hand was encountered before 
    if player1_card.rank() > player2_card.rank() or players_dict["player1"] \
    and not players_dict["player2"]:
        players_dict["player1"].extend(cards_removed)
        winner_str = '1'
    elif player2_card.rank() > player1_card.rank() or not \
    players_dict["player1"] and players_dict["player2"]:
        players_dict["player2"].extend(cards_removed)
        winner_str = '2'
    else:
        winner_str = '0'
        
    return winner_str  
    
def compare_rank(player1_card, player2_card,players_dict):
    """Compares the rank of both cards."""
    if player1_card.rank()==player2_card.rank():
        # Turn over two more cards and compare the second card of each pair
        winner_str = break_tie(player1_card,player2_card,players_dict)
    elif player1_card.rank()>player2_card.rank() and player2_card.rank()!=1:
        winner_str = '1'
    elif player1_card.rank()>player2_card.rank() and player2_card.rank()==1:
        winner_str = '2'
    elif player1_card.rank()<player2_card.rank() and player1_card.rank()!=1:
        winner_str = '2'
    else:
        winner_str = '1'
        
    return winner_str
        
def battle(players_dict: dict):
    """Compares the rank of the first cards in both players hand, adds both 
    cards to the bottom of the stack of either player whose card has a higher
    rank than the other and displays the player that wins each round."""
    player1_card = players_dict["player1"].pop(0)
    player2_card = players_dict["player2"].pop(0)
    winner_str = compare_rank(player1_card,player2_card,players_dict)
    player_str = "player" + winner_str
    if player_str in players_dict:
        print("Battle was 1: {}, 2: {}. Player {} wins battle.".format(
                player1_card,player2_card,winner_str))
        players_dict[player_str].extend([player1_card,player2_card])
        
    else:
        print("Battle was 1: {}, 2: {}. Battle was a draw.".format(
                player1_card,player2_card))
    
def play():
    # Setup game and display hands dealt to both players
    players_dict = setup()
    print("Starting Hands")
    print("Hand 1:",players_dict["player1"])
    print("Hand 2:",players_dict["player2"])
    print()
    
    continue_battle = 'y'
    # Continue while both player have non empty deck and neither player quits
    while continue_battle != 'n':
        battle(players_dict)
        print("hand1:",players_dict["player1"])
        print("hand2:",players_dict["player2"])
        # Check if either player's hand is empty
        if [] in players_dict.values():
            break
        continue_battle = input("Keep Going: (Nn) to stop: ").lower()
    
    print()
    if len(players_dict["player1"]) > len(players_dict["player2"]):
        print("Player 1 wins!!!")
    else:
        print("Player 2 wins!!!")