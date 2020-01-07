# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 07:22:19 2018

@author: Pshypher
"""

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

DISCRETEATTRIBUTES = [WORKCLASS,MARITAL,OCCUPATION,RELATIONSHIP,RACE,SEX]

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
        if '?' in line:
            continue
        
        line = line.strip()
        line_list = line.split(',')

        # Create a dictionary for the line
        # (assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys)
        record = {}
        record[AGE] = float(line_list[0])
        record[WORKCLASS] = line_list[1].strip()
        record[EDUCATIONNUM] = float(line_list[4])
        record[MARITAL] = line_list[5].strip()
        record[OCCUPATION] = line_list[6].strip()
        record[RELATIONSHIP] = line_list[7].strip()
        record[RACE] = line_list[8].strip()
        record[SEX] = line_list[9].strip()
        record[CAPITALGAIN] = float(line_list[10])
        record[CAPITALLOSS] = float(line_list[11])
        record[HOURS] = float(line_list[12])
        record[CLASS] = line_list[14].strip()

        # Add the dictionary to a list
        trainingSet.append(record)        

    fin.close()
    return trainingSet


###############################################################################
# sumAttributes
# parameters:
#    - classdict: a dictionary that sums up each attribute of all the records
#                   for both models above 50k and those below 50k for 
#                   discrete attributes, a dictionary is used to map a category 
#                   to its count.
#    - record: a record of attributes to be summed up with the corresponding
#                   attributes of the model
# returns: None, classdict being a mutable data structure is modified
###############################################################################
def sumAttributes(classDict, record):
    for key, val in record.items():
        if key in DISCRETEATTRIBUTES:   # attribute is categorical?
            if val in classDict[key]:
                classDict[key][val] += 1    # increase count of category by 1
            else:
                classDict[key][val] = 1
        else:
            classDict[key] += val
            
###############################################################################
# calcAverage
# parameters:
#   - classdict: a dictionary, the average value and ratios are calculated for 
#                  each continous and categorical attribute respectively in the
#                  dictionary. 
#   - classcount: the total number for each category (<=50K,>50K) in the 
#                   training set.
# returns: None, dictionary classdict is modified in place
###############################################################################
def calcAverage(classDict, classCount):
    for key, val in classDict.items():
        if key in DISCRETEATTRIBUTES:   # is a categorical attribute?
            for category,categoryCount in classDict[key].items():
                # find the ratio of each category per class(<=50K,>50K)
                classDict[key][category] = categoryCount/classCount
        else:
            classDict[key] = val/classCount 


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
    
    # TODO
    
    # A. initialize two dictionaries for sums of attribute values
    #    and initialize record counts
    above50Kclass = {AGE: 0,
                     WORKCLASS: {},
                     EDUCATIONNUM: 0,
                     MARITAL: {},
                     OCCUPATION: {},
                     RELATIONSHIP: {},
                     RACE: {},
                     SEX: {},
                     CAPITALGAIN: 0,
                     CAPITALLOSS: 0,
                     HOURS: 0}
    below50Kclass = {AGE: 0,
                     WORKCLASS: {},
                     EDUCATIONNUM: 0,
                     MARITAL: {},
                     OCCUPATION: {},
                     RELATIONSHIP: {},
                     RACE: {},
                     SEX: {},
                     CAPITALGAIN: 0,
                     CAPITALLOSS: 0,
                     HOURS: 0}
    above50Kcount = 0
    below50Kcount = 0
    

    # B. process each record in the training set
    #    calculating sums and counts as we go
    for record in trainingSet:
        if record[CLASS] == "<=50K":
            del record[CLASS]   # remove the key "Class" from the dict record
            sumAttributes(below50Kclass, record)
            below50Kcount += 1
        else:
            del record[CLASS]
            sumAttributes(above50Kclass, record)
            above50Kcount += 1
            

    # C. calculate averages for continuous attributes, and
    #    calculate ratios of category for categorical attributes
    calcAverage(above50Kclass, above50Kcount)
    calcAverage(below50Kclass, below50Kcount)
        

#    return the two dictionaries
    return above50Kclass,below50Kclass


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
    # TODO
    
    # For each record in testset
    for record in testSet:
    # initialize >50K and <=50K votes to zero
        above50Kvotes = 0
        below50Kvotes = 0

        # for each attribute of the record
        for attr,value in record.items():
            # for categorical attributes
            if attr in DISCRETEATTRIBUTES:
                # dictionary get method used for instances where the key for
                # each categorical attributes are absent 0 is used instead
                if dict1[attr].get(value,0) > dict2[attr].get(value,0):
                    above50Kvotes += 1
                else:
                    below50Kvotes += 1
                continue
            # if attribute value is closer to dict1 then
            # add one to >50K vote. Otherwise, add one to <=50K vote
            if attr != CLASS and attr != PREDICTED:
                if abs(dict1[attr] - value) < abs(dict2[attr] - value):
                    above50Kvotes += 1
                else:
                    below50Kvotes += 1

        # if >50K vote greater than <=50K vote then
        # predicted class of record is >50K (set predicted class value)
        # otherwise, the predicted class is <=50K
        if above50Kvotes > below50Kvotes:
            record[PREDICTED] = '>50K'
        else:
            record[PREDICTED] = '<=50K'
            
#   return testSet
    return testSet


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

    # TODO

    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class (PREDICTED) to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.
    correct = 0
    total = 0
    
    for record in testSet:
        if record[CLASS] == record[PREDICTED]:
            correct += 1
        total += 1
    
    accuracy = correct/total
    
    print("correct:",correct)
    print("total: ",total)
    print("accuracy (as a percentage): {:.2%}".format(accuracy))
    

    
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
    above50Kclass,below50Kclass = trainClassifier(trainingSet)
    print("Done training classifier.\n")

    print("Reading in test data...")
    testFile = "annual-income-test.data"
    testSet = makeTestSet(testFile)
    print("Done reading test data.\n")

    print("Classifying records...")
    testSet = classifyTestRecords(testSet,above50Kclass,below50Kclass)
    print("Done classifying.\n")

    reportAccuracy(testSet)

    print("Program finished.")
    
main()
