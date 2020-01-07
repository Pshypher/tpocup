# Returns the body mass index of a person
# BMI is weight/height^2
# weight is measured in kilograms and height is in meters.

weight1_str = input("Enter a person's weight in kilograms: ")
weight1_int = int(weight1_str)
height1_str = input("Enter a person's height in meters: ")
height1_int = int(height1_str)
bmi_metric = weight1_int / height1_int**2
print("BMI of individual weighing", weight1_int, "kilogram and", height1_int,
      "metres tall is", bmi_metric, "kg/m^2")

# weight is measured in pounds and height is in inches.
# Returns the Body Mass Index in kg/m^2

weight2_str = input("Enter a person's weight in pounds: ")
weight2_int = int(weight2_str)
height2_str = input("Enter a person's height in inches: ")
height2_int = int(height2_str)
bmi_lbs = weight2_int / height2_int
lbs_bmi_to_metric_bmi = bmi_lbs * 0.453592 / pow(0.0254,2)
print("BMI of individual weighing", weight2_int, "pounds and", height2_int,
      "inches tall is", lbs_bmi_to_metric_bmi, "kg/m^2")

