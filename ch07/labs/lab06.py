# lab06.py

# Unless stated otherwise, each variable is assumed to be a list data type.

import string

def find_mean_score(student_scores):
    """Finds the mean score of the score from four exams. Returns
        the mean scores of the student, a float data type."""
    total_int = sum(student_scores[1:])
    average_float = total_int/len(student_scores[1:])
    
    return average_float

file_obj = open("scores.txt", "r")  # open the file containing the score
                                    # for each student
                                    
# Create a list of tuples to hold each students name, four scores
# and mean score
student_scores = []
for line in file_obj:
    student_info = []
    if line not in string.whitespace:
        line = line.strip()
        student_info.append(line[:20].strip())
        student_info.extend(line[20:].strip().split())
        student_info = [int(elem) if elem.isdigit() else elem
                        for elem in student_info]
        avg_float = find_mean_score(student_info)
        student_info.append(avg_float)
        student_info_tuple = tuple(student_info)
        student_scores.append(student_info_tuple)
        
# Display the each students name, scores and mean score. Also the
# mean score of students for a particular exam is shown

# Sort the list of tuples according to the names of each student
student_scores.sort()
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name","Exam1","Exam2",
                                                      "Exam3","Exam4","Mean"))
exam_total_scores = [0,0,0,0]
for student_record in student_scores:
    name,exam1,exam2,exam3,exam4,mean = student_record
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(name,exam1,exam2,exam3,
                                                      exam4,mean))
    exam_total_scores[0] += exam1
    exam_total_scores[1] += exam2
    exam_total_scores[2] += exam3
    exam_total_scores[3] += exam4

exams_avg_tuple = tuple([exam_total/len(student_scores)
                         for exam_total in exam_total_scores])
    
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",
                                exams_avg_tuple[0],exams_avg_tuple[1],
                                exams_avg_tuple[2],exams_avg_tuple[3]))

    
    