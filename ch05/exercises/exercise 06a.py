infile_obj = open("thisFile.txt", "r")
outfile_obj = open("thatFile.txt", "w")

for line in infile_obj:
    print(line, end='', file=outfile_obj)
    
infile_obj.close()
outfile_obj.close()