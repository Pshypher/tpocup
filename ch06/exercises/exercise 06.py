# Function takes in mass as input and returns its energy equivalent (E = m*c*c)
# the SI unit is used (meter-kilogram-second)

speed_flt = 3.0E8

def calc_energy(mass):
    energy_flt = mass*speed_flt*speed_flt
    return energy_flt