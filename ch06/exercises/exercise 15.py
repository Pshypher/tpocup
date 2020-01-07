# Function that truncuates a message to 160 characters if it is greater than
# 160, and returns the message if it is less than 160.

def restrict_chars(msg_str):
    """Return the message if it is less than 160, or the first 160 characters
    if it is greater than 160."""
    
    CHAR_LIMIT = 160
    
    if len(msg_str) < CHAR_LIMIT:
        msg_str = msg_str
    else:
        msg_str = msg_str[:CHAR_LIMIT]
    
    return msg_str
    
# The second function returns the message if it contains 20 words or less

def restrict_words(msg_str):
    """Returns the message if it contains exactly 20 words or less."""
    
    WORD_LIMIT = 20
    
    words_int = msg_str.count(" ") + 1
    
    if words_int <= WORD_LIMIT:
        msg_str = msg_str
    else:
        msg_str = trunc_msg(msg_str, WORD_LIMIT)
    
    return msg_str

def trunc_msg(msg_str, limit_int):
    """Restrict the number of words to exactly {:d} words.""".format(limit_int)
    
    words_str = msg_str
    word_count = 0
    start_int = 0
    
    while word_count < limit_int and words_str != '': 
        space_char_ind = msg_str.find(" ", start_int)
        start_int = space_char_ind + 1
        word_count = word_count + 1
        if space_char_ind == -1:
            space_char_ind = len(msg_str)
        
    msg_str = msg_str[:space_char_ind]
    return msg_str
        
    
        