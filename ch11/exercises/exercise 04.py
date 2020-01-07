# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:48:22 2018

@author: Pshypher
"""

import random
import time

class Track(object):
    
    def __init__(self,name,duration,artist,album_name=None,year=None):
        """Initializes an instance of a Track."""
        self.__track_name = name
        # duration in hours:min:sec format
        self.__duration = self.get_duration_in_seconds(duration)
        self.__artist = artist
        self.__album_str = album_name
        self.__year = year
        self.__track_playing = False
        self.__paused = False
        
    def get_duration_in_seconds(self,duration):
        fields_time = duration.split(':')
        if len(fields_time) == 3:
            hrs,mins,secs = [int(value) for value in fields_time]
        else:
            hrs,mins,secs = [0] + [int(value) for value in fields_time]
            
        return hrs*3600 + mins*60 + secs
        
    def get_album(self):
        """Returns the name of album track belongs to."""
        return self.__album_str
    
    def play(self):
        """Plays a track. Returns the number of seconds left to play a track"""
        self.__track_playing = True
        self.__paused = False
        print("Track is playing")
    
    def pause(self, seconds_remaining):
        """Pauses track."""
        self.__track_playing = False
        self.__paused = True
        self.__duration = seconds_remaining
        print("Track is paused")
    
    def stop(self):
        """Halts the song."""
        self.__track_playing = False
        self.__paused = False
        print("Track was stopped")
        

class Album(object):
    
    def __init__(self,album_title,album_artist,track_list=[],
                 genre=None,year=None):
        """Initializes an instance of the Album object."""
        self.__tracks = track_list  # Container for a list of tracks 
                                    # in a music album
        self.__album_title = album_title
        self.__album_artist = album_artist
        self.genre = genre
        self.year = year
        
    def add_to_album(self,track: Track):
        """Adds a track to the album track list."""
        if track.get_album() == self.__album_title:
            self.__tracks.append(track)
        else:
            print("*** Track {} doesn't belong to album. ***".format(track))