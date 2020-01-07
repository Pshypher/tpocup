# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:14:59 2018

@author: Pshypher
"""

import copy, random

class Island(object):
    """Island 
    n X n grid where zero value indicates an unoccupied cell."""
    
    def __init__(self, n, prey_count=0, predator_count=0):
        """Initialize grid to all 0's, then fill with animals"""
        # print n,prey_count,predator_count
        self.grid_size = n
        # use of multiple grids
        self.current_grid_list = []
        for i in range(n):
            row = [0] * n  # row is a list of n zeros
            self.current_grid_list.append(row)
        self.next_grid_list = copy.deepcopy(self.current_grid_list)
        self.init_animals(prey_count, predator_count)
    
    def current_grid(self, x, y):
        """Return animal at location (x,y) in the current grid."""
        if not(0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return  -1  # outside island boundary
        else: 
            return self.current_grid_list[x][y]
        
    def next_grid(self, x, y):
        """Return animal at location (x,y) in the next grid."""
        if not(0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return  -1  # outside island boundary
        else:
            return self.next_grid_list[x][y]
        
    def empty_grid(self):
        """Fresh empty grid made for the next clock tick."""
        self.next_grid_list = []
        for i in range(self.grid_size):
            row = [0] * self.grid_size  # row is a list of grid_size zeros
            self.next_grid_list.append(row)
            
    def init_animals(self, prey_count, predator_count):
        """Put some initial animals on the island"""
        count = 0
        # while loop continues until prey_count unoccupied positions are found
        while count < prey_count:
            x = random.randint(0,self.grid_size-1)
            y = random.randint(0,self.grid_size-1)
            if not self.next_grid(x,y):
                new_prey = Prey(island=self, x=x, y=y, s='m')
                count += 1
                self.register(new_prey)
        count = 0
        # same while loop but for predator_count
        while count < predator_count:
            x = random.randint(0, self.grid_size-1)
            y = random.randint(0, self.grid_size-1)
            if not self.next_grid(x,y):
                new_predator = Predator(island=self, x=x, y=y, s='w')
                count += 1
                self.register(new_predator)
                
        self.update_grid()
        self.empty_grid()
                
    def register(self,animal):
        """Register animal with island, i.e., put it at the 
        animal's coordinates"""
        x = animal.x
        y = animal.y
        self.next_grid_list[x][y] = animal
                    
    def remove(self,animal):
        x,y = animal.position()
        self.current_grid_list[x][y] = 0
        self.next_grid_list[x][y] = 0

    def size(self):
        """Return size of the island: one dimension."""
        return self.grid_size
    
    def update_grid(self):
        """The current grid is updated, the actions of each Predator and Prey
        instance recorded in the subsequent grid is moved to the current grid."""
        self.current_grid_list = []
        for row in self.next_grid_list:
            self.current_grid_list.append(row[:])
            
    def __str__(self):
        """String representation for printing.
        (0,0) will be in the lower-left corner."""
        s = ""
        for j in range(self.grid_size-1,-1,-1):     # print row size-1 first
            for i in range(self.grid_size):         # each row starts at 0
                if not self.current_grid_list[i][j]:
                    # print a '.' for an empty space
                    s += "{:<4s}".format('.' + "  ")
                else:
                    s += "{:<4s}".format(str(self.current_grid_list[i][j]) + "  ")
            s+="\n"
        return s
    
class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        """Initialize the animals and their positions"""
        self.island = island
        self.name = s
        self.x = x
        self.y = y
        
    def position(self):
        """Return coordinates of the current position."""
        return self.x, self.y
    
    def check_grid(self,type_looking_for=int):
        """Look in the 8 directions from the animal's location
        and return the first location that presently has an object
        of the specified type. Return 0 if no such location exists."""
        # neighbor offsets
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        result = 0
        while offset:
            offset_x, offset_y = offset.pop(random.randint(0, len(offset)-1))
            x = self.x + offset_x  # neighbouring coordinates
            y = self.y + offset_y
            if not 0 <= x < self.island.size() or \
            not 0 <= y < self.island.size():
                continue
            if type(self.island.next_grid(x,y)) == int and \
            type(self.island.current_grid(x,y)) == type_looking_for:
                result = (x,y)
                break
        
        return result                    
    
    def move(self):
        """Move to an open, neighbouring position."""
        if isinstance(self, Predator) and self.starve_clock > 0 or \
            isinstance(self, Prey):    
            location = self.check_grid(int)
            if location:
                print('Move, {}, from {},{} to {},{}'.format(
                        type(self),self.x,self.y,location[0],location[1]))
                self.island.remove(self)
                self.x = location[0]        # new coordinates
                self.y = location[1]
                self.island.register(self)  # register new coordinates
            else:
                self.island.register(self)
            
    def breed(self):
        """Breed a new Animal. If there is room in one of the 8 locations,
        place the offspring there. Otherwise, you have to wait."""
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                self.breed_clock = self.breed_time
                the_class = self.__class__
                new_animal = the_class(self.island,x=location[0],y=location[1])
                self.island.register(new_animal)
        
    def __str__(self):
        return self.name
    
class Prey(Animal):
    
    def __init__(self, island, x=0, y=0, s="m"):
        Animal.__init__(self, island, x, y, s)
        self.breed_clock = self.breed_time
        
    def clock_tick(self):
        """Prey updates only its local breed clock."""
        self.breed_clock -= 1
        
class Predator(Animal):
    
    def __init__(self, island, x=0, y=0, s="w"):
        Animal.__init__(self, island, x, y, s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        
    def clock_tick(self):
        """Predator updates both breeding and starving."""
        self.breed_clock -= 1
        self.starve_clock -= 1
        # if self.starve_clock <= 0:
        #    self.island.remove(self)
        
    def eat(self):
        """Predator looks for one of the eight locations with Prey. If found,
        moves to that location, updates the starve clock, removes the Prey."""
        location = self.check_grid(Prey)
        
        if location:
            prey = self.island.current_grid(location[0],location[1])
            self.island.remove(prey)
            # self.island.remove(self)
            self.x = location[0]
            self.y = location[1]
            self.island.register(self)
            self.starve_clock = self.starve_time
        
def main(predator_breed_time=6, predator_starve_time=3,initial_predators=10, 
         prey_breed_time=3, initial_prey=50, size=10,ticks=300):
    """main simulation; sets defaults, runs event loop, plots at the end
    """
    # initialization values
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time
    
    # make an island
    isle = Island(size,initial_prey,initial_predators)
    
    # event loop.
    # For all the ticks, for every x,y location.
    # If there is animal there, try eat, move, breed and clock_tick
    for i in range(ticks):
        print(isle)
        for x in range(size):
            for y in range(size):
                animal = isle.current_grid(x,y)
                if animal:
                    if isinstance(animal, Predator):
                        animal.eat()
                    animal.move()
                    animal.breed()
                    animal.clock_tick()
        isle.update_grid()
        isle.empty_grid()