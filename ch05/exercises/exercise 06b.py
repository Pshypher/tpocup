import os

infile_obj = open("thisFile.txt", "r")
os.chdir("subdir/")
outfile_obj = open("thatFile.txt", "w")
os.chdir('../')

for line in infile_obj:
    os.chdir("subdir/")
    print(line, end='', file=outfile_obj)
    os.chdir("../")
    
infile_obj.close()
outfile_obj.close()
