# Oil conversions and calculations
# Prompt the user for the volume of gasoline in gallons
# 140.43 billion gallons of gasoline consumed in the United States
volume_gasoline_str = input("Volume of gasoline in gallons [example 140.43e10]: ")    
volume_gasoline_gallons = float(volume_gasoline_str)

volume_gasoline_liters = volume_gasoline_gallons * 3.785412
print(volume_gasoline_gallons, "gallons ->", volume_gasoline_liters, "liters")

# Calculates the amount of barrels of oil required to make the volume of gasoline given
volume_oil = 1 * volume_gasoline_gallons / 19.5     
print("{:.4f} barrels of oil yields {} gallons of gasoline.".format(volume_oil, volume_gasoline_gallons))                                                                    

# Returns the volume of CO2 gas produced for n gallons of gasoline                                                   
CO2_produced = volume_gasoline_gallons * 20 / 1     
print("{} gallons of gasoline returns {} pounds of CO2".format(volume_gasoline_gallons,
                                                                       CO2_produced))
                                                   
gasoline_energy_output = 115000 * volume_gasoline_gallons / 1
# Calculates the gallons of ethanol required to
# produce the same amount of energy for gasoline
ethanol_gallons = gasoline_energy_output * 1 / 75700
print("The volume of Ethanol in gallons required to yield an equivalent \
energy output of {0} BTU for {1} gallons of gasoline is {2:.4f}".format(gasoline_energy_output,
                                                                               volume_gasoline_gallons,
                                                                               ethanol_gallons))

# Price in U.S. dollars of the given volume of gasoline
price_of_gasoline = 3.00 * volume_gasoline_gallons / 1
print("Cost of gasoline for {0} gallons is ${1:.2f}".format(volume_gasoline_gallons,
                                                                price_of_gasoline))
