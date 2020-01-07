# Program displays the index of both o's in the input "Who's on first?"

input_str = "Who's on first?"
first_o = input_str.find('o')
second_o = input_str.find('o', first_o+1)
print("1st o: {}\n2nd o: {}".format(first_o, second_o)) 
