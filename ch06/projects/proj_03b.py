# Program designed to simulate a game of Heap of Beans amongst 2 players
# Unless stated otherwise, variables are assumed to be of type int

import random

def remove_bean_player_one(beans, beans_picked):
    """Removes a single bean from the heap by the first player, reduces the
        amount of beans in the heap by one and return the number of beans left
        in the heap."""
    print("Player one removes " + str(beans_picked) + " from the heap.")
    beans = beans - beans_picked
    return beans

def remove_bean_player_two(beans, beans_picked):
    """Removes a single bean from the heap by the second player, reduces the
        amount of beans in the heap by one and return the number of beans left
        in the heap."""
    print("Player two removes " + str(beans_picked) + " from the heap.")
    beans = beans - beans_picked
    return beans

def pick_beans_from_heap(beans_remaining, player):
    beans_picked_str = input(
        "Player {:d} select beans from heap(1-3): ".format(player))
    beans_picked = int(beans_picked_str)
    
    while beans_picked < 1 or beans_picked > 3 \
          or beans_picked > beans_remaining:
        beans_picked_str = input(
            "Player {:d} select beans from heap(1-3): ".format(player))
        beans_picked = int(beans_picked_str)
    
    return beans_picked


beans_remaining = 16
player_turn = random.randint(0, 1)

while beans_remaining > 1:
    if not player_turn:
        beans_picked = pick_beans_from_heap(beans_remaining, player_turn+1)  
        beans_remaining = remove_bean_player_one(beans_remaining, beans_picked)
        player_turn = 1
    else:
        beans_picked = pick_beans_from_heap(beans_remaining, player_turn+1)
        beans_remaining = remove_bean_player_two(beans_remaining, beans_picked)
        player_turn = 0
else:
    if player_turn:
        print("Player two looses the game.")
    else:
        print("Player one looses the game.")