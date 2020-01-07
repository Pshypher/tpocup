

import NMM #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
       Takes in a player and the current state of the board and counts how many
       of the mills are held by the player. Returns an int
    """
    count = 0
    for row in board.MILLS:
        for x in row:
            if board.points[x] != player:
                break
        else:
            count += 1
        
    return count
            
def place_piece_and_remove_opponents(board, player, destination):
    """
        Place a piece for player, if a mill is created, removes an opponent's
        piece
    """
    # count the mills formed by player before placing a piece
    previous_mill_count = count_mills(board, player)
    # place a piece
    if board.points[destination] != " " :
        raise RuntimeError("Cannot place a piece in an occupied spot.")
    elif destination not in board.points:
        raise RuntimeError("Point not in board.")
    else:
        board.assign_piece(player,destination)
    # count the number of mills formed after placing a piece
    current_mill_count = count_mills(board, player)
    # remove other player's piece from board if a new mill is formed
    if current_mill_count > previous_mill_count:
        other_player = get_other_player(player)
        remove_piece(board, other_player)
        
def point_check(board, point, piece):
    """
        Checks that point is on the board and the piece on the board is similar
        to the piece parameter. Returns a boolean.
    """
    if board.points(point) != piece:
        return False
    else:
        return True
    
def is_adjacent(board, origin, destination):
    """
        Checks that two points origin and destination are adjacent points.
        Returns a boolean.
    """
    if destination in board.ADJACENCY[origin]:
        return True
    else:
        return False
        
      
def move_piece(board, player, origin, destination):
    """
       Moves a piece from the origin to the destination on the board. 
    """
    if not (origin in board.points and destination in board.points):
        raise RuntimeError("Point not on board.")
    elif point_check(board, origin, player) and point_check(
            board, destination, " "):
        if is_adjacent(origin, destination):
            board.clear_place(origin)
            place_piece_and_remove_opponents(board, player, destination)
        else:
            raise RuntimeError("{:s} and {:s} are non-adjacent points".format(
                origin, destination))
    else:
        raise RuntimeError("Different piece on board")
            
    
def points_not_in_mills(board, player):
    """
        Finds all points belonging to a player that are not in mills. Returns
        a set
    """
    
    points_in_mills_set = set()
    
    for pt in board.points:
        if board.points[pt] == player:
            for row in board.MILLS:
                for x in row:
                    if board.points[x] != player:
                        break
                else:
                    points_in_mills_set.update(set(row))
                    
    points_outside_mill_set = placed(board, player) - points_in_mills_set 
        
    return points_outside_mill_set

def placed(board, player):
    """
        Gets all the points where the player's pieces have been placed. Returns
        a set
    """
    player_points = set()
    for pt in board.points:
        if board.points[pt] == player:
            player_points.add(pt)
            
    return player_points
    
def remove_piece(board, player):
    """
        Removes a piece belonging to player from the board.
    """
    points_outside_mills = points_not_in_mills(board, player) & placed(
            board, player)
    
    point = input('Enter point on board to remove {:s} from: '.format(player))    
    while point not in points_outside_mills:
        print("Cannot remove {:s} piece from {:s}".format(player, point))
        point = input('Enter point on board to remove {:s} from: '.format(player))
    else:
        board.clear_place(point)

def is_winner(board, player):
    """
        Used to decide if the game of Nine Men's Morris has been won. Returns
        a boolean
    """
    other_player = get_other_player(player)
    return len(placed(board, other_player)) == 3
   
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"
    
def main():
    #Loop so that we can start over on reset
    while True:
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent
        
        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:
                place_piece_and_remove_opponents(board, player, command)
                player = get_other_player(player)
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
        
        #Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                move_piece(board, player, command[0], command[1])
                if is_winner(board, player):
                    print(BANNER)
                    break
                player = get_other_player(player)
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))         
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

       
if __name__ == "__main__":
    main()