
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        
        
        
        if species and species in self.species_set:
            
            species = species.lower()
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        if self.name_str:
            result_str = "species of {:s}, named {:s}".format(
                    self.species_str,self.name_str)
        else:
            result_str = "species of: {:s}, unnamed".format(self.species_str)
        
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):
    
    def __init__( self, name="", chases="Cats" ):
        
        Pet.__init__( self, "Dog", name )
        self.chases_str = chases

    def __str__( self ):
        
        result_str = Pet.__str__(self)
        result_str += ", chases {:s}".format(self.chases_str.lower())
        
        return result_str
        
##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    def __init__( self, name="", hates="Dogs" ):
        
        Pet.__init__( self, "Cat", name )
        self.hates_str = hates
        
    def __str__(self):
        
        result_str = Pet.__str__(self)
        result_str += ", hates {:s}".format(self.hates_str.lower())
        
        return result_str
