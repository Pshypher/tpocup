# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 07:53:00 2018

@author: Pshypher
"""
import string
QUIT = ''

def open_file():
    '''Open a file and returns a file pointer object if file exists in the 
    current working directory.'''
    found = False
    while not found:
        try:
            file_name = input("Enter a file: ")
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("\n*** unable to open file ***")
            
    return file_pointer


def create_keys(movies_list: list, movies_actor_dict: dict) -> None:
    '''Using the collection of actors and movie titles, it creates the keys 
    in the dictionary which are a tuple of (movie_title, production_year).'''
    for detail in movies_list:
        try:
            if str(detail[1]).isdigit():    # element is a tuple?
                if detail in movies_actor_dict:
                    continue
                movies_actor_dict[detail] = set()
        except IndexError:
            continue


def map_values_to_keys(movies_list: list, movies_actor_dict: dict) -> None:
    '''Actors are placed in a collection (a set) mapped to the movie(key) in
    which they were a part of.''' 
    for i in range(len(movies_list)):
        if type(movies_list[i]) == str:    # element is the name of an actor?
            actor = movies_list[i]
        # add each actor that played a role in a movie to the movie
        for j in range(i,len(movies_list)):
            if type(movies_list[j]) == str: # stop when you hit the end of the
                break                   # list of movies an actor appeared in
            movies_actor_dict[movies_list[j]].add(actor)
                
    
def build_map(movies_list: list, movies_actor_dict: dict) -> None:
    '''Each movie indexes a collection of actors, the mapping is created from 
    the first argument, the list of movies and actors, actors are distinguished
    from movies in that they are not suceeded by a production year (2003).'''
    
    for i,detail in enumerate(movies_list):
        # seperate fields with movies titles joined with names of actors
        if ')' in detail and detail[-1] in string.ascii_letters:
            movie_str, year_str = detail[:detail.find('(')-1], detail[
                    detail.find('(')+1:detail.find(')')]
            actor_str = detail[detail.find(')')+1:].strip()
            movies_list[i:i+1] = [(movie_str.strip(),int(year_str)),actor_str]
        elif ')' in detail:
            # seperate movie title and production year 
            movie_str, year_str = detail[:detail.find('(')-1], detail[
                    detail.find('(')+1:detail.find(')')]
            movies_list[i] = (movie_str.strip(), int(year_str))
        
    create_keys(movies_list, movies_actor_dict)
    map_values_to_keys(movies_list, movies_actor_dict)


def read_file(file_pointer, movies_actor_dict: dict) -> None:
    '''Reads each line from a file and builds a dictionary pairing movie titles
    with all the actors that participated in the movie.'''
    
    movies_list = []
    
    for line_str in file_pointer:
        next_entry = line_str.strip().split(',')
        if movies_list:
            start_int = 0
            # the last item in the list is an empty string
            if not movies_list[-1]:
                movies_list[-1] = next_entry[0] # replace empty string 
                start_int = 1
            elif movies_list[-1][-1] in '&' + string.ascii_letters:
                # join the last item in the list to the first line if it ends  
                # with an alphabet or an ampersand '&'
                movies_list[-1] = movies_list[-1] + ' ' + next_entry[0]
                start_int = 1
            movies_list.extend(next_entry[start_int:])
        else:
            movies_list.extend(next_entry)
            
    # map the tuple of movie, year to a collection of actors in the movie
    # using the movies_list
    build_map(movies_list, movies_actor_dict)
    

def get_others_actor_starred_alongside(command_str, movies_actor_dict):
    '''Fetches all the actors that have starred in previous roles in old films 
    alongside the actor whose name is given in command_str.'''
    remark_str = "Actors that have appeared in films alongside {}.".format(
            command_str)
    actor_set = set()
    for key, val in movies_actor_dict.items():
        if command_str in val:
            actor_set = actor_set | val
            
    return remark_str, actor_set
    
    
def get_set_of_actors_in_both_movies(command_list, movies_actor_dict):
    '''Performs a set operation on both movie titles and returns a tuple  
    consisting of a string and the set of actors gotten from such set operation.'''
    
    for key,val in movies_actor_dict.items():
        if key[0] == command_list[0]:
            movie_actors_set = val
        elif key[0] == command_list[2]:
            other_movie_actors_set = val
            
    if command_list[1] == '&':
        remark_str = "Intersection"
        actors_set = movie_actors_set & other_movie_actors_set
    elif command_list[1] == '|':
        remark_str = "Union"
        actors_set = movie_actors_set | other_movie_actors_set                                                 
    else:
        remark_str = "Symmetric difference"
        actors_set = movie_actors_set ^ other_movie_actors_set
    
    return remark_str, actors_set
    
 
def parse_command(command_str, movies_actor_dict):
    '''Parses the command and does one of the following operation according to
    what is passed in, union, intersection, symmetric difference of actors in
    both movies if two movie titles are given, otherwise it displays a list of
    all the actors an actor has worked with if an actor's name is given.'''
    command_list = []
    # use the keys (movie_title, year) in the dictionary to take out a movie
    # title from the string command
    for key in movies_actor_dict:
        if key[0] in command_str:
            command_str = command_str[:command_str.find(key[0])] + \
            command_str[command_str.find(key[0])+len(key[0]):]
            command_str = command_str.strip()
            command_list.append(key[0])
            break
    # find the set operator
    if command_str[0] in ('&','|','-'):
        command_list.append(command_str[0])
        command_str = command_str[1:].strip()
    elif command_str[-1] in ('&','|','-'):
        command_list.append(command_str[-1])
        command_str = command_str[:-1].strip()
    # find the other movie title in the dictionary mapping movie titles to a 
    # set of actors
    movies_list = [key[0] for key in movies_actor_dict]
    if command_str in movies_list:
        command_list.append(command_str)
    # process both movie_title strings using the set operator all in the
    #  passed into the list 
    print(command_list)
    if len(command_list) == 3:
        remark_str, actors_set = get_set_of_actors_in_both_movies(command_list,
                                                  movies_actor_dict)
    else: # otherwise assume the command is the name of an actor
         remark_str, actors_set = get_others_actor_starred_alongside(
                 command_str, movies_actor_dict)
    return remark_str, actors_set
    
def main():
    file_pointer = open_file()
    
    movies_actor_dict = {}
    read_file(file_pointer, movies_actor_dict)
    
    command_str = input("Name of actor or 2 movie titles seperated by either \
one of(&,|,-) or enter to quit: ")
    # repeatedly prompt the user until a sentinel value is entered
    while command_str != QUIT:
        result_tuple = parse_command(command_str, movies_actor_dict)
        if result_tuple[1]:
            remark_str, actors_set = result_tuple
            print("\n{:20s}".format(remark_str))
            print('-'*50)
            for actor in actors_set:
                if actor != command_str:
                    print(actor)
        elif not result_tuple[1]:
            remark_str = "Null Set"
            print(remark_str)
        
        command_str = input("Name of actor or 2 movie titles seperated by either \
one of(&,|,-) or enter to quit: ")
            
if __name__=="__main__":
    main()