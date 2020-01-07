# This program rewrites a string of names in the form "Chapman, Graham Arthur"
# to the string "Graham Arthur Chapman."

names_str = "Chapman, Graham Arthur"
lastname_str, names_str = names_str.split(', ')
firstname_str, middlename_str = names_str.split(' ')

print("{} {} {}.".format(firstname_str, middlename_str, lastname_str)) 
