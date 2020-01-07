# Function "safe_input(prompt_str, type)" designed to work similarly to the
# Python input function, except that it only accepts the specified type of

def safe_input(prompt_str="", type=str):
    input_str = input(prompt_str)
    
    while True:
        try:
            input_type = type(input_str)
            break
        except ValueError:
            print('Incorrect input({:s}) of specified type({:s}).'.format(
                input_str, str(type)))
            input_str = input(prompt_str)
        
    return input_type            