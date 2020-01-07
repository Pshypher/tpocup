# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:58:04 2018

@author: Pshypher
"""
from nba_stats import NBA_PLAYER_STATS_DICT
    
def calc_efficiency(line_str, the_dict):
    """Calculate player efficiency."""
    # asserts on the parameters
    assert isinstance(the_dict,dict),\
    'bad parameter, expected a dictionary got {}'.format(the_dict)
    
    line_str = line_str.strip()
    assert isinstance(line_str, str) and line_str != '',\
    'bad parameter, expected string, got {}'.format(line_str)
    
    fields_list = line_str.split(',')
    name = fields_list[1]
    
    # mapping fields_list in a line to theor particular variable.
    # league is a str, everything else an int
    gp,mins,pts,fgm,fga,fgp,tpm,tpa,tpp,ftm,fta,ftp,oreb,dreb,reb,asts,stl,\
    blk,to,efgp,tsp = \
    int(fields_list[2]),int(fields_list[3]),int(fields_list[4]),\
    int(fields_list[5]),int(fields_list[6]),float(fields_list[7]),\
    int(fields_list[8]),int(fields_list[9]),float(fields_list[10]),\
    int(fields_list[11]),\
    int(fields_list[12]),float(fields_list[13]),int(fields_list[14]),\
    int(fields_list[15]),int(fields_list[16]),int(fields_list[17]),\
    int(fields_list[18]),\
    int(fields_list[19]),int(fields_list[20]),float(fields_list[21]),\
    float(fields_list[22])
    
    # gp can't be 0
    assert gp != 0, '{} has no games played'.format(name)
    
    # calculate the player's efficiency
    efficiency = ((pts+reb+asts+stl+blk)-((fga-fgm) + (fta-ftm)+to))/gp
    
    the_dict[name] = {'gp':gp,'mins':mins,'pts':pts,'fgm':fgm,'fga':fga,
            'fgp':fgp,'tpm':tpm,'tpa':tpa,'tpp':tpp,'ftm':ftm,'fta':fta,
            'ftp':ftp,'oreb':oreb,'dreb':dreb,'reb':reb,'asts':asts,'stl':stl,
            'blk':blk,'to':to,'efgp':efgp,'tsp':tsp,
            'efficiency':efficiency}
    
    
def find_most_efficient(the_dict,how_many):
    '''
    >>> find_most_efficient({}, 10)
    []
    >>> find_most_efficient(NBA_PLAYER_STATS_DICT, 0)
    []
    >>> find_most_efficient([], 5)
    Traceback (most recent call last):
        ...
    AssertionError: bad parameter, expected a dictionary got []
    >>> find_most_efficient(NBA_PLAYER_STATS_DICT, 'three')
    Traceback (most recent call last):
        ...
    AssertionError: bad parameter, expected an integer got three
    >>> find_most_efficient(NBA_PLAYER_STATS_DICT, 3)
    [(20.91866913123845, 'John Wall'), (14.744186046511627, 'Jim Washington'), (11.669781931464174, 'Nate Williams')]
    '''
    # user must implement
    assert isinstance(the_dict,dict),\
    'bad parameter, expected a dictionary got {}'.format(the_dict)
    assert type(how_many) == int,\
    'bad parameter, expected an integer got {}'.format(how_many)
    
    players_list = sorted([(stats_dict['efficiency'],name_str)
    for name_str, stats_dict in the_dict.items()], reverse=True)
    
    return players_list[:how_many]

def print_results(lst):
    '''pretty print the results '''
    print('The top {} players in efficiency are'.format(len(lst)))
    print('*'*20)

    for efficiency_flt,name_str in lst:
        print(" {:>25s} : {:<.2f}".format(name_str,efficiency_flt))
    
# main program as a function
def main(file_name):
    '''
    >>> main('')
    File named  not found
    >>> main('x')
    Traceback (most recent call last):
        ...
    OSError: bad file format.
    >>> main('player_career.csv')
    The top 10 players in efficiency are
    ********************
                    Mike Bibby : 14921.00
                     Sam Lacey : 9443.50
                 Stacey Augmon : 8655.00
                 Calvin Murphy : 8323.00
                    Grant Long : 4192.00
                    Ron Harper : 1627.22
                 Nazr Mohammed : 1589.80
               Jermaine O'Neal : 1388.64
               Antonio McDyess : 1017.40
              Wilt Chamberlain : 963.67
    '''
    try:
        nba_file = open(file_name)
    except IOError:
        print('File named {} not found'.format(file_name))
    else:
        global nba_dict
        nba_dict = {}
        line_str = nba_file.readline()
        if 'PLAYER' not in line_str:
            raise IOError('bad file format.')
        for line_str in nba_file:
            calc_efficiency(line_str,nba_dict)
            
        results_list = find_most_efficient(nba_dict,10)
        print_results(results_list)
        nba_file.close()
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()