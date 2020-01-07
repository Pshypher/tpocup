# Function "prompt_open(mode)" designed to prompt for a file name and
# repeatedly attempt to read the file specified until a correctly specified file
# has been entered. The mode argument is one of 'r' or 'w'

def prompt_open(mode):
    file_name = input("Enter name of file: ")
    
    while True:
        try:
            input_file = open(file_name, mode)
            break
        except IOError:
            print("File name \"{:s}\" not found".format(file_name))
            file_name = input("Enter name of file: ")
            
    return input_file