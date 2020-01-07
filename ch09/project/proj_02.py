# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:54:56 2018

@author: Pshypher
"""
# Organize your itunes library using the metadata

# using copy-and-paste, copy your itunes metadata from text "list" view of 
# the itunes playlist into a text editor.
# open the file containing the metadata
# initialize an empty dictionary, read each line of the file, organizing each 
    # music around the name of the artist, the remaining metadata becomes 
    # a value of each record
    
# to add a song into the dictionary containing the metadata, 
# prompt for the artist name, time, track title, album and genre
# search for the name of the artist in the dictionary, excluding the name
# of the artist, append a tuple of the remaining metadata into the list of 
# tuples associated with the name of the artist, being the key
# if the artist is not in the dictionary, add the artist name as a key in the
# dictionary and the remaining metadata as values in the dictionary

# to delete a song, prompt user for the track title 
# iterate through the values of each key in the dictionary until the track 
# title is found, remove the tuple containing the metadata for that track from
# the list of tuples.

# to find the artist with the most songs in the itunes library metadata,
# count the number of elements in the collection mapped to the key (artist name)
# and return the name of the artist

# to find the longest song in the itunes collection, convert the entire 
# dictionary to a list of tuples, including the name of the artist as the 1st
# element of the tuple, convert the time in minutes for the duration of each 
# record to seconds; sort the list based on the field containing the time.
# the first tuple in the collection is the metadata for the record with the
# longest time duration in seconds
from operator import itemgetter

def open_file():
    '''Returns the file pointer of the file containing the metadata of the
    itunes library.'''
    while True:
        try:
            file_name = input("Enter name of file contanining tab seperated \
values of itunes metadata: ")
            file_pointer = open(file_name, 'r')
            break
        except IOError:
            print("*** unable to open file ***")
            
    return file_pointer

def read_file(file_pointer, metadata_dict):
    '''Reads each line of the itunes metadata, organizing each record around
    the name of the artist, the artist becomes the key in the dictionary while
    the remaining metadata for each record are fields in a tuple mapped to the
    key. Each record by an artist is added to a collection of tuples.'''
    for line_str in file_pointer:
        line_str = line_str.strip()
        if line_str:    # split non-empty lines on the tab character
            track,time,artist,album,genre = line_str.split('\t')[:5]
            # add only records that have labels for artist names, albums and 
            # genres
            if artist and album and genre: 
                if artist in metadata_dict:
                    metadata_dict[artist].append((track,time,album,genre))
                else:
                    metadata_dict[artist] = [(track,time,album,genre)]
                    
def display_records_by_artist(name_str: str, metadata_dict: dict) -> None:
    '''Displays all the songs recorded by an artist.'''
    if name_str in metadata_dict:
        songs_list = metadata_dict[name_str]
        print('\n',name_str,sep='')
        print('-'*len(name_str))
        out_str = ''
        for record in songs_list:
            out_str += '  '
            for data in record:
                out_str += data + ', '
            else:
                out_str = out_str.rstrip(', ') + '\n'
        print(out_str,end='')
    else:
        print("\n{:<s} not found in metadata.".format(name_str))
        
def print_songs_on_album(album_str: str, metadata_dict: dict) -> None:
    '''Displays the songs recorded on the album specified.'''
    records_list = []
    for key, val in metadata_dict.items():
        for record in val:
            # album name is the 3rd field in each record tuple
            track_title, duration_str, album_title, genre_str = record
            artist_str = key
            if album_str == album_title:
                records_list.append(
                        (track_title,duration_str,artist_str,genre_str))
    
    if records_list:
        print('\n',album_str.strip(),sep='')
        print('-'*len(album_str))
        out_str = ''
        for record in records_list:
            out_str += '  '
            for data in record:
                out_str += data.strip() + ', '
            else:
                out_str = out_str.rstrip(', ') + '\n'        
        print(out_str,end='') 
    else:
        print("\n{:<s} not in the itunes library or metadata.".format(
                album_str))
        
def display_songs_in_genre(genre_spec_str: str, metadata_dict: dict) -> None:
    '''Displays a list of all the songs in the specified genre.'''
    records_list = []
    for key, val in metadata_dict.items():
        for record in val:
            track_title,duration_str,album_str,genre_str=record
            if genre_spec_str == genre_str:
                records_list.append((track_title,duration_str,album_str,key))
                
    if records_list:
        print('\n',genre_spec_str,sep='')
        print('-'*len(genre_spec_str))
        out_str = ''
        for record in records_list:
            out_str += '  '
            for data in record:
                out_str += data + ', '
            else:
                out_str = out_str.rstrip(', ') + '\n'
        print(out_str, end='')
    else:
        print("Specified genre {} not in the itunes library metadata".format(
                genre_spec_str))
        
def parse_num_secs(secs_str: str) -> str:
    '''Parses the number of seconds passed in to minutes and seconds, seperated
    by a comma.Returns a string in the format min:seconds.'''
    secs_int = int(secs_str)
    minutes = secs_int // 60
    secs_left = secs_int % 60
    return str(minutes) + ':' + str(secs_left)
        
def add_track(record_metadata_tuple: tuple, metadata_dict: dict) -> None:
    '''Adds the metadata of a particular record to the dictionary.'''
    artist_str = record_metadata_tuple[0]
    if artist_str in metadata_dict:
        metadata_dict[artist_str].append(record_metadata_tuple[1:])
    else:
        metadata_dict[artist_str] = record_metadata_tuple[1:]
        
def delete_song(track_title: str, metadata_dict: dict) -> None:
    '''Removes the values of a record from the dictionary.'''
    track_found = False
    
    for key,val in metadata_dict.items():
        for i,record in enumerate(val):
            # track_title in record and song title specified are similar?
            if track_title == record[0]:
                del val[i]  # remove record
                track_found = True
                break
        if track_found:
            break
        
def get_popular_artist(metadata_dict: dict) -> str:
    '''Finds the name of the artist with the highest number of records in 
    itunes collection. Returns a string'''
    max_num_of_songs_int = 0
    for artist,records in metadata_dict.items():
        if len(records) > max_num_of_songs_int:
            max_num_of_songs_int = len(records)
            most_popular_artist = artist
            
    return most_popular_artist

def calc_time_in_seconds(time_str: str) -> int:
    '''Calculates and returns the total time in seconds from the time_str 
    argument specified in the min:seconds format.'''
    time_list = time_str.split(':')
    mins_int,secs_int = int(time_list[0]),int(time_list[1])
    total_num_secs = mins_int * 60 + secs_int
    return total_num_secs

def get_longest_record(metadata_dict: dict) -> tuple:
    '''Returns a tuple of the record with the longest duration of play.'''
    
    itunes_library_metadata_list = []
    for artist,records in metadata_dict.items():
        for song in records:
            track_title,time_str,album_str,genre = song
            duration_secs = calc_time_in_seconds(time_str)
            itunes_library_metadata_list.append((artist,track_title,
                                                 duration_secs,album_str,genre))
            
    # sort all records in descending order using the 3rd field for the duration
    # of each song
    itunes_library_metadata_list.sort(reverse=True,key=itemgetter(2))
    
    artist,track_title,duration_secs,album_str,genre = \
    itunes_library_metadata_list[0]
    
    time_str = parse_num_secs(str(duration_secs))
    return artist,track_title,time_str,album_str,genre

def main():
    # open file containing itunes metadata
    file_pointer = open_file()
    metadata_dict = {}  # empty dictionary to map artist name to each track 
                        # recorded
    read_file(file_pointer, metadata_dict)
    
    while True:
        name_str = input("Enter name of artist: ")
        display_records_by_artist(name_str, metadata_dict)
        album_str = input("Enter album name: ")
        print_songs_on_album(album_str, metadata_dict)
        genre_str = input("Enter genre of songs to be fetched from metadata: ")
        display_songs_in_genre(genre_str, metadata_dict)
        add_track_char = input("Do you wish to add a song (y/n)? ")
        # add a song to the metadata dictionary
        if add_track_char.lower() == 'y':
            track_title = input("Enter name of song: ")
            secs_str = input("Enter duration of song in seconds: ")
            artist_str = input("Enter name of artist: ")
            album_str = input("Enter album track belongs to: ")
            genre_str = input("Genre of track: ")
            time_str = parse_num_secs(secs_str)
            add_track((artist_str,track_title,time_str,album_str,genre_str),
                      metadata_dict)
        
        del_track_char = input("Do you want to delete a song (y/n)? ")
        # delete a song record from the dictionary
        if del_track_char.lower() == 'y':
            track_title = input("Name of song you wish to delete: ")
            delete_song(track_title, metadata_dict)
        
        # artist with the most songs in itunes collection
        popular_artist = get_popular_artist(metadata_dict)
        print("\nMost popular artist:",popular_artist)
        # metadata of the longest song in the itunes collection
        longest_record_metadata_tuple = get_longest_record(metadata_dict)
        print("\nDuration of longest record in collection")
        print('-'*40)
        for data in longest_record_metadata_tuple:
            print('  ',data,sep='',end=' ')
        print()
         
if __name__ == "__main__":
    main()
        
    
    
