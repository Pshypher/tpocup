# Returns the body mass index of a person
# BMI is weight/height^2
# weight is measured in kilograms and height is in meters.

weight1_str = input("Enter a person's weight in kilograms: ")
weight1_float = float(weight1_str)
height1_str = input("Enter a person's height in meters: ")
height1_float = float(height1_str)
bmi_metric = weight1_float / height1_float ** 2
print("BMI of individual weighing", weight1_float, "kilogram and", height1_float,
      "metres tall is", bmi_metric, "kg/m^2")

if bmi_metric < 18.5:
    print("Underweight")
elif bmi_metric < 25.0:
    print("Normal")
elif bmi_metric < 30.0:
    print("Overweight")
else:
    print("Obese")

