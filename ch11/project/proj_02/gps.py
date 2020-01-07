# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:34:51 2018

@author: Pshypher
"""
import random
import math

class WayPoint(object):
    
    DISTANCE_PER_DEGREE_LATITUDE=110.57     # distance in km per degree lat.
    DISTANCE_PER_DEGREE_LONGITUDE=111.32    # distance in km per degree long.
    
    def __init__(self, longitude=0, latitude=0):
        """Constructor for a new waypoint object."""
        self.__longitude = longitude
        self.__longitude_dir = 'W' if longitude < 0 else 'E'
        self.__latitude = latitude
        self.__latitude_dir = 'S' if latitude < 0 else 'N'
        
    def get_longitude(self):
        """Returns the longitude of WayPoint object."""
        return self.__longitude
    
    def set_longitude(self, longitude):
        """Sets a new longitude."""
        self.__longitude = longitude
        self.__longitude_dir = 'W' if longitude < 0 else 'E'
        
    def set_latitude(self,latitude):
        """Sets a new latitude."""
        self.__latitude = latitude
        self.__latitude_dir = 'S' if latitude < 0 else 'N'        
        
    def get_latitude(self):
        """Returns the latitude of WayPoint object."""
        return self.__latitude
        
    def calc_distance(self, other):
        """Calculates the distance between two WayPoints. Returns a floating 
        point number."""
        longitude_diff = (self.__longitude - other.__longitude) * \
        WayPoint.DISTANCE_PER_DEGREE_LONGITUDE
        latitude_diff = (self.__latitude - other.__latitude) * \
        WayPoint.DISTANCE_PER_DEGREE_LATITUDE
        
        return math.sqrt(longitude_diff * longitude_diff + 
                         latitude_diff * latitude_diff)
        
    def calc_bearing(self, other):
        """Calculates the bearing(direction) between two WayPoint objects.
        Returns a floating point number."""
        # calculate the horizontal distance(longitude) between waypoints
        dist_btw_longitudes = (self.__longitude - other.__longitude) * \
        WayPoint.DISTANCE_PER_DEGREE_LONGITUDE
        # calculate the vertical distance(latitude) between waypoints
        dist_btw_latitudes = (self.__latitude - other.__latitude) * \
        WayPoint.DISTANCE_PER_DEGREE_LATITUDE
        
        angle_radians = math.atan2(dist_btw_latitudes, dist_btw_longitudes)
        
        if (self.__latitude_dir=='N' or self.__latitude_dir=='S') and \
        self.__longitude_dir=='W':
            angle_degrees = math.degrees(angle_radians + math.pi)
        elif self.__latitude_dir=='S' and self.__longitude_dir=='E':
            angle_degrees = math.degrees(2*math.pi + angle_radians)
        else:
            angle_degrees = math.degrees(angle_radians)
            
        return angle_degrees
    
    def __str__(self):
        return "({:.2f}{},{:.2f}{})".format(abs(self.__latitude),
                 self.__latitude_dir,abs(self.__longitude),self.__longitude_dir)
                
class GPSUnit(object):
      
    def __init__(self):
        """Constructor for a new gps unit."""
        self.__way_points = {}
        self.__paths = {}
        self.__longitude,self.__latitude = self.gps_get_long_lat()
        
    def gps_get_long_lat(self):
        """Generates the current longitude and latitude. Returns a pair of 
        floating point values."""
        longitude_sign = random.choice([-1,1])
        longitude_flt = (random.random()*181)%181 * longitude_sign
        latitude_sign = random.choice([-1,1])
        latitude_flt = (random.random()*91)%91 * latitude_sign
        
        return longitude_flt, latitude_flt
    
    def set_waypoint(self,name_str: str):
        """Saves a WayPoint with longitude,latitude pair or the current default
        longitude,latitude position if no argument is passed in, each waypoint
        is labelled name_str in the GPS."""
        self.__way_points[name_str] = WayPoint(self.__longitude,
                         self.__latitude)
        
    def get_waypoint(self,waypoint_name):
        """Returns the waypoint labelled wapoint_name in the GPSUnit."""
        return self.__way_points[waypoint_name]
    
    def set_path(self,name_str):
        """Creates and sets a path to chart a course consisting of several 
        named waypoints."""
        self.__paths[name_str] = list()
        
    def add_to_path(self,path_name: str,waypoint_str: str):
        """Adds a waypoint to a path."""
        self.__paths[path_name].append(self.__way_points[waypoint_str])
        
    def get_path(self,path_name):
        """Returns the path called path_name in the GPSUnit."""
        return self.__paths[path_name]
        
    def get_path_length(self,path_name: str):
        """Gets the length of a certain named path, path_name. Returns a 
        floating point number."""
        total_dist_flt = 0
        for i in range(len(self.__paths[path_name])-1):
            total_dist_flt += self.__paths[path_name][i].calc_distance(
                    self.__paths[path_name][i+1])
        
        return total_dist_flt
            
    def get_distance(self,waypoint: WayPoint):
        """Calculates the distance between the current position and a named
        waypoint."""
        current_position = WayPoint(self.__longitude,self.__latitude)
        distance_flt = current_position.calc_distance(waypoint)
        
        return distance_flt
    
    def get_bearing(self,waypoint: WayPoint):
        """Calculates the bearing between the current position and another 
        named waypoint."""
        current_position = WayPoint(self.__longitude,self.__latitude)
        bearing_flt = current_position.calc_bearing(waypoint)
        
        return bearing_flt
        
    def __str__(self):
        """"Displays the current longitude and latitude."""
        return "({:.2f},{:.2f})".format(self.__longitude,self.__latitude)