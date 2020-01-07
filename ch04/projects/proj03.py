# Program uses the Google currency converter to convert an amount of a currency
# specified by the user to another currency type also specified by the user.The
# conversion rates are determined online in real-time

# Prompt the user for the original currency
# Prompt the user for the target currency
# Prompt the user for the amount which must be an int.
# Setup the URL and send the request
# Convert the returned value to a string, and then process it to find the
# converted value.
# Display the result to the user.
# Prompt the user if they want to repeat.

# Unless specified otherwise, variables are of the string type

import urllib.request

PRE_URL = \
"https://finance.google.com/finance/converter?a={2:s}&from={0:s}&to={1:s}"
SPAN_TAG_CLASS_BLD = "<span class=bld>"
CLOSE_SPAN_TAG = "</span>"

repeat = "yes"

while repeat == "yes":
    original_currency = input("What is the original currency? ")
    original_currency = original_currency.upper()
    target_currency = input("What currency do you want to convert to? ")
    target_currency = target_currency.upper()
    orig_amount = input("How much do you want to convert (int)? ")
    
    while not orig_amount.isdigit():
        print("The value you input must be an integer. Please try again.\n")
        orig_amount = input ("How much do you want to convert (int)? ")
        
    url = PRE_URL.format(original_currency, target_currency, orig_amount)
    response = urllib.request.urlopen(url)
    result = str(response.read())   # read response and convert
                                    # it to a string
    
    # Parse result of response string and extract the value
    # of the target currency
    open_span_int = result.find(SPAN_TAG_CLASS_BLD)
    close_span_int = result.find(CLOSE_SPAN_TAG, open_span_int)
    length_span_tag = len(SPAN_TAG_CLASS_BLD)
    span_content = result[(open_span_int+length_span_tag):close_span_int]
    target_amount_flt = float(span_content[:-3])
    
    # Display the result of the conversion
    print("{0:s} {1:s} is {2:.2f} {3:s}".format(orig_amount, original_currency,
                                                target_amount_flt, target_currency))
    
    repeat = input("Do you want to convert another currency? ")
    repeat = repeat.lower()
    print()
    
