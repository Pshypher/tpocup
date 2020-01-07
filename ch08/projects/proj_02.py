from operator import itemgetter

# Unless stated otherwise, each variable is assumed to be a list 

def get_data_list(file_name, column_header, sep_char=','):
    '''Reads a file <file_name> and splits each line in the file
        on a <sep_char>, puts the data into a list that is returned.'''
    data_file = open(file_name, 'r')
    data_list = []      # start with an empty list
    for line_str in data_file:
        if column_header in line_str:   # skip line if it is the header
            continue                    # of a column
        # strip end-of-line, split on sep_char, and append items to list
        data_list.append(line_str.strip().split(sep_char))
    return data_list
        
def get_players_stats(data_list):
    '''Returns a list of relevant stats for each nba player, each item in the
        returned list is a tuple of values containing the efficiency of a
        player, games played, minutes, points scored, penalties, rebounds,
        free throws and the name of a player.'''
    stats = []
    
    for player in data_list:
        player_name = player[1]
        efficiency_flt = calc_efficiency(player)
        gp = int(player[5])
        mins = int(player[7])
        pts = float(player[-1])
        pf = int(player[-2])
        reb = int(player[-7])
        free_throws = int(player[18])
        stats.append((player_name, efficiency_flt, gp, mins, pts, pf, reb,
                      free_throws))
         
    return stats

def calc_efficiency(player_stat: list) -> float:
    '''Calculates the efficiency of a certain player using the relevant
        fields in the player_stat list.'''
    # All variables are assumed to be the float data type
    reb,asts,stl,blk,turn_over = [float(var) for var in player_stat[-7:-2]]
    pts = float(player_stat[-1])
    fgm,fga = [float(var) for var in player_stat[8:10]]
    ftm,fta = [float(var) for var in player_stat[18:20]]
    gp = int(player_stat[5])
    
    efficiency = (pts + reb + asts + stl + blk - fga + fgm - fta + ftm - \
                 turn_over) / gp
    
    return efficiency

def get_most_efficient_players(player_stats):
    '''Returns the fifty most efficient nba players in the entire season.'''
    player_stats.sort(key=itemgetter(1), reverse=True)
    return player_stats[:50]

def get_player_most_games(player_stats):
    '''Returns the player who played most games.'''
    player_stats.sort(key=itemgetter(2), reverse=True)
    return player_stats[0]

def get_player_most_minutes(player_stats):
    '''Returns the player who played the most minutes.'''
    player_stats.sort(key=itemgetter(3), reverse=True)
    return player_stats[0]

def get_player_most_points(player_stats):
    '''Returns the player who scored the most points.'''
    player_stats.sort(key=itemgetter(4), reverse=True)
    return player_stats[0]

def get_player_most_penalties(player_stats):
    '''Returns the player who got the most personal fouls.'''
    player_stats.sort(key=itemgetter(5), reverse=True)
    return player_stats[0]

def get_player_most_rebounds(player_stats):
    '''Returns the player who got the most rebounds.'''
    player_stats.sort(key=itemgetter(6), reverse=True)
    return player_stats[0]

def get_player_most_free_throws(player_stats):
    '''Returns the player who made the most free throws.'''
    player_stats.sort(key=itemgetter(7), reverse=True)
    return player_stats[0]

def display_stats(player_stats: list) -> None:
    '''Displays the relevant statistics such as 50 of the most efficient nba players,
        the player who played the most minutes,the player who played the most games,
        who scored the most points, who got the most rebound, etc.'''
    efficient_players = get_most_efficient_players(player_stats)
    played_most_games = get_player_most_games(player_stats)
    most_minutes = get_player_most_minutes(player_stats)
    scored_most_points = get_player_most_points(player_stats)
    most_personal_fouls = get_player_most_penalties(player_stats)
    most_rebounds = get_player_most_rebounds(player_stats)
    most_free_throws_made = get_player_most_free_throws(player_stats)
    
    # display the top fifty efficient players
    print()
    print("{:<22s} {:>10s}".format("Player Name", "Efficiency"))
    print('-'*34)
    for player in efficient_players:
        print("{:<22s} {:>10.2f}".format(player[0], player[1]))
        
    print('\n')
    
    print("{} played the most with a total of {} games.".format(
        played_most_games[0],played_most_games[2]))
    print("{} had more minutes of game time,{} mins than any other nba \
player.".format(most_minutes[0], most_minutes[3]))
    print("{} scored most point a total of {} pts.".format(
        scored_most_points[0], scored_most_points[4]))
    print("{} committed most fouls a total of {} fouls committed".format(
        most_personal_fouls[0], most_personal_fouls[5]))
    print("{} had the most rebounds a total of {} rebounds".format(
        most_rebounds[0], most_rebounds[6]))
    print("{} made most free throws {} free throws made".format(
        most_free_throws_made[0], most_free_throws_made[7]))
    

def main():
    data_list = get_data_list("player_regular_season_career.txt", "Player", '/')
    # Get relevant player statistic from the fields gotten from the
    # player_regular_season_career.txt file
    player_stats = get_players_stats(data_list)
    display_stats(player_stats)