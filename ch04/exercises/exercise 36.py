# Program written to display the values of the melting and boiling point
# of Alkanes in a nice format

melt_boil_pt_alkanes = [("Methane", -162, -183),("Ethane", -89, -172),
                        ("Propane", -42, -188), ("Butane", -0.5, -135)]

# Header
print()
print("Melting and Boiling Points of Alkanes")
print("{:8s}  {:22s}  {:22s}".format("Name", "Melting Point (deg C)", "Boiling Point (deg C)"))
print("{:8s}  {:22s}  {:22s}".format('-'*4, '-'*21, '-'*21))

for alkane in melt_boil_pt_alkanes:
    print("{0[0]:8s}  {0[1]:>+21.1f}   {0[2]:>+21d}".format(alkane))
