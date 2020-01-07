# Function displays a textual progress bar based on the number of seconds elapsed
# in intervals of floor(num_secs/10) seconds
# Unless stated otherwise, variables are of type int

import time
import math

def textual_progress_bar(num_secs):
    """Prints an X on the console after floor(num_secs/10) seconds have elapsed."""
    progress_bar_width = 10
    progress = 0
    secs_elapsed = progress
    progress_str = "X"

    print("At {:d} secs: {:s}".format(secs_elapsed, progress_str*progress))
    
    while progress < math.floor(num_secs/10):
        time.sleep(math.floor(num_secs/10))
        progress += 1
        secs_elapsed += math.floor(num_secs/10)  
        print("At {:d} secs: {:s}".format(secs_elapsed, progress_str*progress))
        

