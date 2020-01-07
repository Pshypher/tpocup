# Program to convert the knuts to sickles and galleons (the currency
# of the Harry Potter novels).
# prompt user for amount of the currency in knuts
# convert the amount to sickles and galleons
# display only non-zero values that are results of the conversion

KNUTS_PER_SICKLE = 29
SICKLES_PER_GALLEON = 17

# prompt user for amount in knuts
knuts_str = input("Currency in knuts: ")
knuts_flt = float(knuts_str)

# convert from knuts to sickles
sickles_flt = knuts_flt / KNUTS_PER_SICKLE

# convert from knuts to galleons
galleons_flt = sickles_flt / SICKLES_PER_GALLEON

# display non-zero values of the conversion
if sickles_flt >= 1:
    print("Sickles: ", sickles_flt)
if galleons_flt >= 1:
    print("Galleons: ", galleons_flt)