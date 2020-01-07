###############################################################################
# Tasks
# 1 - Create a training set
# 2 - Train a 'dumb' rule-based classifier
# 3 - Create a test set
# 4 - Apply rule-based classifier to test set
# 5 - Report accuracy of classifier
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and sums
# DONE - Do not modify.
###############################################################################
AGE = "Age"
WORKCLASS = "Work-class"
EDUCATIONNUM = "Education-num"
MARITAL = "Marital-status"
OCCUPATION = "Occupation"
RELATIONSHIP = "Relationship"
RACE = "Race"
SEX = "Sex"
CAPITALGAIN = "Capital-gain"
CAPITALLOSS = "Capital-loss"
HOURS = "Hours-per-week"
CLASS = "Class"
PREDICTED = "Predicted Class"

###############################################################################
# 1. Create a training set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
# makeTrainingSet
# parameters: 
#     - filename: name of the data file containing the training data records
#
# returns: trainingSet: a list of training records (each record is a dict,
#                       that contains attribute values for that record.)
###############################################################################
def makeTrainingSet(filename):
    # DONE - Do not modify.
    trainingSet = []

    fin = open(filename,'r')

    # Read in file
    for line in fin:
        line = line.strip()
        line_list = line.split(',')

        # Create a dictionary for the line
        # ( assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys )
        record = {}
        record[AGE] = float(line_list[0])
        record[WORKCLASS] = line_list[1]
        record[EDUCATIONNUM] = float(line_list[4])
        record[MARITAL] = line_list[5]
        record[OCCUPATION] = line_list[6]
        record[RELATIONSHIP] = line_list[7]
        record[RACE] = line_list[8]
        record[SEX] = line_list[9]
        record[CAPITALGAIN] = float(line_list[10])
        record[CAPITALLOSS] = float(line_list[11])
        record[HOURS] = float(line_list[12])
        record[CLASS] = line_list[14]

        # Add the dictionary to a list
        trainingSet.append(record)        

    fin.close()
    return trainingSet


###############################################################################
# 2. Train 'Dumb' Classifier
# trainClassifier
# parameters:
#     - trainingSet: a list of training records (each record is a dict,
#                     that contains attribute values for that record.)
#
# returns: two dictionaries, one for >50K and the other for <=50K. In each
#          dictionary, if one attribute is categorical, its value should also
#          be a dictionary.
###############################################################################
def trainClassifier(trainingSet):
    pass

    # TODO
    
    # A. initialize two dictionaries for sums of attribute values
    #    and initialize record counts


    # B. process each record in the training set
    #    calculating sums and counts as we go


    # C. calculate averages for continuous attributes, and
    #    calcuate ratios of category for categorical attributes


#    return the two dictionaries


###############################################################################
# 3. Create a test set
# - Read in file
# - Create a dictionary for each line
# - Initialize each record's predicted class to 'unknown'
# - Add this dictionary to a list
#
# makeTestSet
# parameters: 
#     - filename: name of the data file containing the test data records
#
# returns: testSet: a list of test records (each record is a dict,
#                       that contains attribute values for that record
#                       and where the predicted class is set to 'unknown'. 
###############################################################################
def makeTestSet(filename):

    # DONE - Do not modify.
    testset = makeTrainingSet(filename)

    for record in testset:
        record[PREDICTED] = 'unknown'

    return testset


###############################################################################
# 4. Classify test set
#
# classifyTestRecords
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#      - dict1: a dictionary for >50K
#      - dict2: a dictionary for <=50K
#
# returns: testSet with the predicted class set to either >50K or <=50K
#
# for each record, if the majority of attributes are closer to dict1,
# then predict the record as >50K
###############################################################################
def classifyTestRecords(testSet, dict1, dict2):
    pass
    # TODO
    
    # For each record in testset

        # initialize >50K and <=50K votes to zero

        # for each attribute of the record
            # if attribute value is closer to dict1 then
            # add one to >50K vote. Otherwise, add one to <=50K vote

        # if >50K vote greater than <=50K vote then
        # predicted class of record is >50K (set predicted class value)
        # otherwise, the predicted class is <=50K
            
#    return testSet


###############################################################################
# 5. Report Accuracy
# reportAccuracy
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#                 and both the predicted and actual class values are set
#
# returns: None
#
# prints out the number correct / total and accuracy as a percentage
###############################################################################
def reportAccuracy(testSet):
    pass
    # TODO

    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class (PREDICTED) to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.

    
###############################################################################
# main - starts the program
###############################################################################
def main():
    # TODO
    print("Reading in training data...")
    trainingSet = []
    trainingFile = "annual-income-training.data"
    trainingSet = makeTrainingSet(trainingFile)
    print("Done reading training data.\n")

    print("Training classifier...")
    # add call to appropriate function
    print("Done training classifier.\n")

    print("Reading in test data...")
    testFile = "annual-income-test.data"
    testSet = makeTestSet(testFile)
    print("Done reading test data.\n")

    print("Classifying records...")
    # add call to appropriate function
    print("Done classifying.\n")

    # add call to appropriate function

    print("Program finished.")
    
main()
