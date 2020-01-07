# Program written to find the max, min and average values of columns.
# also an additional column (BMI) based on the other columns is created

MINIMUM = 1E6
MAXIMUM = -1E6

input_file = open("data.txt", 'r')
line_count = 0

total_height_flt = 0
total_weight_flt = 0
total_bmi_flt = 0

minimum_height_flt = MINIMUM
minimum_weight_flt = MINIMUM
minimum_bmi_flt = MINIMUM

maximum_height_flt = MAXIMUM
maximum_weight_flt = MAXIMUM
maximum_bmi_flt = MAXIMUM

for line in input_file:
    
    line_count += 1
    
    if line_count == 1:
        print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)",
                                                          "Weight(kg)", "BMI"))
        continue
    
    height_flt = float(line[12:24])
    weight_flt = float(line[24:])
    bmi_flt = weight_flt / height_flt ** 2
    
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(line[:12], height_flt,
                                                         weight_flt, bmi_flt))
    
    if height_flt < minimum_height_flt:
        minimum_height_flt = height_flt
    if height_flt > maximum_height_flt:
        maximum_height_flt = height_flt
    if weight_flt < minimum_weight_flt:
        minimum_weight_flt = weight_flt
    if weight_flt > maximum_weight_flt:
        maximum_weight_flt = weight_flt
    if bmi_flt < minimum_bmi_flt:
        minimum_bmi_flt = bmi_flt
    if bmi_flt > maximum_bmi_flt:
        maximum_bmi_flt = bmi_flt
        
    total_height_flt = total_height_flt + height_flt
    total_weight_flt = total_weight_flt + weight_flt
    total_bmi_flt = total_bmi_flt + bmi_flt
    
    
count = line_count - 1
average_height_flt = total_height_flt / count
average_weight_flt = total_weight_flt / count
average_bmi_flt = total_bmi_flt / count

avg_line = "{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", average_height_flt,
                                            average_weight_flt, average_bmi_flt)
max_line = "{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", maximum_height_flt,
                                            maximum_weight_flt, maximum_bmi_flt)
min_line = "{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", minimum_height_flt,
                                            minimum_weight_flt, minimum_bmi_flt)
print()
print(avg_line)
print(max_line)
print(min_line)
    
input_file.close()