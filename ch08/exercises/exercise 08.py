def mirror(pair):
    '''reverses first two elements;
        assumes "pair" is as a collection with at least two elements'''
    try:
        return pair[1], pair[0]
    except TypeError:
        print("Pair should be an iterable object either one of lists, tuples \
or str.")
    except IndexError:
        print("Pair should be a collection of 2 or more elements.")

mirror(10)      # generates error
mirror('2')     # generates error
mirror((6,))    # generates error
mirror([6])     # generates error
