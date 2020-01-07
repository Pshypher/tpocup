# Calculates the depth of the great lakes in the United States over a
# surface area of the 48 contiguous states.
volume_int = 22810    # Volume of 22% of the world's fresh surface water
surface_area_int = 8080464.3    # Surface area in square km

# V = SA * H
# where V is the volume, SA the surface area and
# H is the height, depth or thickness of the solid
depth = volume_int / surface_area_int

print("The depth of the great lakes in the United States is {0:>.5f}km, \
over a total surface area of {1:^} square-km.".format(depth, surface_area_int))
