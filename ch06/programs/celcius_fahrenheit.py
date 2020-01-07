# Conversion program

def celcius_to_fahrenheit(celcius_float):
    """Convert Celcius to Fahrenheit."""
    return celcius_float * 1.8 + 32


# main part of the program
print("Convert Celcius to Fahrenheit.")
celcius_float = float(input("Enter a Celcius temp: "))
# call the conversion function
fahrenheit_float = celcius_to_fahrenheit(celcius_float)
# print the returned value
print(celcius_float, " converts to ", fahrenheit_float, " Fahrenheit")