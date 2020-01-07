# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:28:05 2018

@author: Pshypher
"""

import copy, math, random
import matplotlib.pyplot as plt

def distance(point_a, point_b):
    """Calculates the distance between two points on a rectangular coordinate."""
    x_diff = point_a[0] - point_b[0]
    y_diff = point_a[1] - point_b[1]
    return math.sqrt(x_diff**2 + y_diff**2)

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
        self.predator_list = []
        self.prey_list = []
        
    def count(self, animal_type):
        """Counts the number of the category of specified animal
        on this Island at an instance in time."""
        animal_count = 0
        for y in range(len(self.current_grid_list)):
            for x in range(len(self.current_grid_list[y])):
                if isinstance(self.current_grid_list[y][x], animal_type):
                    animal_count += 1
        
        return animal_count
    
    def count_predator(self):
        """Count the number of predator on this Island."""
        predator_count = self.count(Predator)
        self.predator_list.append(predator_count)
        
    def count_prey(self):
        """Count the number of preys on this Island."""
        prey_count = self.count(Prey)
        self.prey_list.append(prey_count)       
                
    
    def current_grid(self, x, y):
        """Return animal at location (x,y) in the current grid."""
        if not(0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return  -1  # outside island boundary
        else: 
            return self.current_grid_list[x][y]
        
    def get_predator_population(self):
        """Returns a list of all the population count of 
        the Predator per clock tick on this Island"""
        return self.predator_list
    
    def get_prey_population(self):
        """Returns a list of all the population count of
        the Prey per clock tick on this Island."""
        return self.prey_list
        
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
        coordinates = [(x,y) for x in range(self.grid_size) for y in
                       range(self.grid_size)]
        # while loop continues until prey_count unoccupied positions are found
        while count < prey_count and coordinates:
            x,y = random.choice(coordinates)
            coordinates.remove((x,y))
            new_prey = Prey(island=self, x=x, y=y, s='m')
            count += 1
            self.register(new_prey)
        count = 0
        # same while loop but for predator_count
        while count < predator_count and coordinates:
            x,y = random.choice(coordinates)
            coordinates.remove((x,y))
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
        location = self.check_grid(int)
        if location:
            # print('Move, {}, from {},{} to {},{}'.format(
            #        type(self),self.x,self.y,location[0],location[1]))
            self.island.remove(self)
            self.x = location[0]        # new coordinates
            self.y = location[1]
            self.island.register(self)  # register new coordinates
                
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
                
    def get_empty_cells(self):
        """Returns a list of unoccupied cells."""
        empty_cells_lst = list()
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if not self.island.current_grid(x,y):
                empty_cells_lst.append((x,y))
                
        return empty_cells_lst
                
    def search_animal(self, animal_type):
        """Returns a list of coordinates occupied by an animal type, 2 hops
            away."""
        animals_list = list()
        offset = [(x,y) for x in range(-2,3) for y in range(-2,3) 
        if x!=0 or y!=0]
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if isinstance(self.island.current_grid(x,y),animal_type):
                animals_list.append((x,y))
                
        return animals_list
        
    def __str__(self):
        return self.name
    
class Prey(Animal):
    
    def __init__(self, island, x=0, y=0, s="m"):
        Animal.__init__(self, island, x, y, s)
        self.breed_clock = self.breed_time
        
    def clock_tick(self):
        """Prey updates only its local breed clock."""
        self.breed_clock -= 1
                
    def move(self):
        """Move Prey away from Predator."""
        predators = self.search_animal(Predator)
        empty_cells = self.get_empty_cells()
        maximum_distance = 0
        location = (self.x,self.y)
        
        for i,a_point in enumerate(empty_cells):
            total_distance = 0
            for other_point in predators:
                total_distance += distance(a_point,other_point)
            if total_distance > maximum_distance:
                maximum_distance = total_distance
                location = a_point
                
        if self.island.next_grid(location[0],location[1]) == 0:
            # print("Move, {} from {},{} to {},{}".format(
            #         type(self),self.x,self.y,location[0],location[1]))
            self.island.remove(self)
            self.x = location[0]
            self.y = location[1]
            self.island.register(self)
        else:
            Animal.move(self)
                
class Predator(Animal):
    
    def __init__(self, island, x=0, y=0, s="w"):
        Animal.__init__(self, island, x, y, s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        
    def clock_tick(self):
        """Predator updates both breeding and starving."""
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)
        
    def eat(self):
        """Predator looks for one of the eight locations with Prey. If found,
        moves to that location, updates the starve clock, removes the Prey."""
        location = self.check_grid(Prey)
        
        if location:
            prey = self.island.current_grid(location[0],location[1])
            self.island.remove(prey)
            self.island.remove(self)
            self.x = location[0]
            self.y = location[1]
            self.island.register(self)
            self.starve_clock = self.starve_time
            
    def move(self):
        """Move Predator towards Prey."""        
        preys = self.search_animal(Prey)
        empty_cells_lst = self.get_empty_cells()
        closest_distance = distance((0,0), (self.island.size(),
                                     self.island.size()))
        location = (self.x,self.y)
        
        for i,a_point in enumerate(empty_cells_lst):
            total_distance = 0
            for other_point in preys:
                total_distance += distance(a_point,other_point)
            if total_distance < closest_distance:
                closest_distance = total_distance
                location = a_point
                
        if self.island.next_grid(location[0],location[1]) == 0:
            self.island.remove(self)
            self.x = location[0]
            self.y = location[1]
            self.island.register(self)
        else:
            Animal.move(self)
        
def main(predator_breed_time=3, predator_starve_time=3,initial_predators=10, 
         prey_breed_time=5,initial_prey=50,size=10,ticks=80):
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
        isle.count_predator()
        isle.count_prey()
        isle.empty_grid()
        
    # Plot the population of predator & prey during each clock-tick
    plt.plot(isle.get_predator_population(), label='Predator')
    plt.plot(isle.get_prey_population(), label='Prey')
    plt.legend()
    plt.ylabel("Population")
    plt.xlabel("Clock tick")
    plt.show()