# Prints out an estimate of the population in n years in the United States

# Prompt user for the number of years
years_str = input("Number of years: ")
years_int = int(years_str)
current_population = 307357870

# Calculates the number of births, deaths and immigrants since n seconds elapsed
secs_since_n_years = years_int * 365 * 24 * 60 * 60
births_since_n_years = 1 * secs_since_n_years / 7
deaths_since_n_years = 1 * secs_since_n_years / 13
immigrants_since_n = 1 * secs_since_n_years / 35

# Population is estimated from the total number of births, death and immigration
# since n seconds elapsed
population_estimate = current_population + births_since_n_years - deaths_since_n_years + immigrants_since_n
print("The population in the United States since {} seconds elapsed is {:.0f}".format(secs_since_n_years,
                                                                                      population_estimate))
