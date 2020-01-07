# Program designed to simulate a game of Heap of Beans amongst 2 players
# Unless stated otherwise, variables are assumed to be of type int

import random

def remove_bean_player_one(beans):
    """Removes a single bean from the heap by the first player, reduces the
        amount of beans in the heap by one and return the number of beans left
        in the heap."""
    print("A single bean is removed from the heap.")
    beans = beans - 1
    return beans

def remove_bean_player_two(beans):
    """Removes a single bean from the heap by the second player, reduces the
        amount of beans in the heap by one and return the number of beans left
        in the heap."""
    print("A single bean is removed from the heap.")
    beans = beans - 1
    return beans


beans = 16
player_turn = random.randint(0, 1)

while beans > 1:
    if not player_turn:
        beans = remove_bean_player_one(beans)
        player_turn = 1
    else:
        beans = remove_bean_player_two(beans)
        player_turn = 0
else:
    if player_turn:
        print("Player two looses the game.")
    else:
        print("Player one looses the game.")


