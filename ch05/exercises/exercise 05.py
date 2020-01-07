# read a particular line from a file. User provides both the line
# number and the file name

file_str = input("Open what file:")
file_found = False

while not (file_found and line_exists):
    try:
        input_file = open(file_str)         # potential user error
        file_found = True
        
        find_line_str = input("Which line (integer):")
        legal_line_input = False
        while not legal_line_input:
            try:
                find_line_int = int(find_line_str)  # potential user error
                legal_line_input = True
            except ValueError:
                print("Line", find_line_str, "isn't a legal line number.")
                find_line_str = input("Which line (integer):")
            
        line_count_int = 1
        for line_str in input_file:
            if line_count_int == find_line_int:
                print("Line {} of file {} is {}".format(find_line_int, file_str,
                                                        line_str), end='')
                break
            line_count_int += 1
            line_exists = True
        else:
            # get here if line sought doesn't exist
            line_exists = False
            print("Line {} of file {} not found".format(find_line_int, file_str))
                
    except IOError:
        print("The file", file_str, "doesn't exist.")
        file_str = input("Open what file:")

input_file.close()
print("End of the program")
