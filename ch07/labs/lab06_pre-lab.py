fp = open( "lab06_pre-lab_input.txt" )
total = 0
letters = ''
for line in fp:
    for ch in line:
        if ch.isdigit():
            total += int(ch)
        elif ch.isalpha():
            letters += ch
            
print( total )    # Line 1 -> 13
print( letters )  # Line 2 -> abcdxyz 
fp.close()