# Program design to solve the paper folding puzzle
# prompt the user for the total folds
# initial thickness of the paper is 1/200
# number of folds = 0
# while the number of folds is less than the limit of the total folds entered
# by the user
#   fold the paper by half and increase the thickness by 1/200
#   increment the number of folds by 1
# display the thickness of the folded paper

# unless stated otherwise, variables are assumed to be of type int

PAPER_THICKNESS = 1/200

total_folds_str = input("Enter the total number of folds: ")
total_folds = int(total_folds_str)

number_of_folds = 0
thickness = PAPER_THICKNESS

while number_of_folds < total_folds:
    thickness = thickness + PAPER_THICKNESS
    number_of_folds = number_of_folds + 1
    
print("Paper thickness after ", total_folds, "folds is", thickness)
    

