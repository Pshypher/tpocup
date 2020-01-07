# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 08:46:11 2018

@author: Pshypher
"""
# session makes use of the GPSUnit class

import gps

# make an instance of a GPSUnit and display your current position
a_gps_unit = gps.GPSUnit()
print(a_gps_unit)

"""
# save current waypoint in GPSUnit, walk away some distance and 
a_gps_unit.set_waypoint("western-way")
# create new path
a_gps_unit.set_path("ABU")
# mark the subsequent waypoints
# waypoint PZ
pz_long,pz_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("pz",pz_long,pz_lat)
# waypoint MTD
mtd_junc_long,mtd_junc_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("mtd",mtd_junc_long,mtd_junc_lat)
# waypoint Kwangila
kwangila_long,kwangila_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("kwangila",kwangila_long,kwangila_lat)
# waypoint Emanto
emanto_long,emanto_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("emanto",emanto_long,emanto_lat)
# waypoint Zango
zango_long,zango_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("zango",zango_long,zango_lat)
# waypoint Samaru
samaru_long,samaru_lat = a_gps_unit.gps_get_long_lat()
a_gps_unit.set_waypoint("samaru",samaru_long,samaru_lat)

# add all waypoint to path ABU
a_gps_unit.add_to_path("ABU","western-way")
a_gps_unit.add_to_path("ABU","pz")
a_gps_unit.add_to_path("ABU","mtd")
a_gps_unit.add_to_path("ABU","kwangila")
a_gps_unit.add_to_path("ABU","emanto")
a_gps_unit.add_to_path("ABU","zango")
a_gps_unit.add_to_path("ABU","samaru")

print("Total distance western-way to ABU: {:.2f}km".format(
        a_gps_unit.get_path_length("ABU")))

# move randomly away from former location
current_long, current_lat = a_gps_unit.gps_get_long_lat()
current_position = gps.WayPoint(current_long,current_lat)
# get WayPoint object of former location
all_waypoints = a_gps_unit.get_all_waypoints()
former_position = all_waypoints["samaru"]
# get the distance and bearing between former waypoint and current position
print("Distance between Samaru and current position: {:.2f}km".format(
        current_position.calc_distance(former_position)))
print("Bearing between Samaru and current position: {:.2f} degrees".format(
        current_position.calc_bearing(former_position)))
"""

a_gps_unit.set_path("path-across-major-cities")
smith_county_long,smith_county_lat = -98.5833,39.83333
