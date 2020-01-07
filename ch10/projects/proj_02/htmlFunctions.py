# Functions adapted from ProgrammingHistorian (updated to Python3)
# http://niche.uwo.ca/programming-historian/index.php/Tag_clouds

# Take one long string of words and put them in an HTML box.
# If desired, width, background color & border can be changed in the function
# This function stuffs the "body" string into the HTML formatting string

def printHTMLfile(body,title):
    ''' create a standard html page with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    '''
    fd = open(title+'.html','w')
    theStr="""
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    <address></address>
    <!-- hhmts start --> Last modified: Wed Jul 25 19:39:41 EDT 2018 <!-- hhmts end -->
    </body> </html>
    """
    fd.write(theStr)
    fd.close()

def makeHTMLbox(body):
    ''' make an HTML box that has all the words in it
    '''
    boxStr = """<div style=\"
    width: 800px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center;
    margin: auto auto\">%s</div>
    """
    return boxStr % (body)

def makeHTMLword(word,cnt,high,low):
    ''' make a word with a font size to be placed in the box. Font size is 
    scaled between htmlBig and htmlLittle (to be user set). high and low  
    represent the high and low counts in the document. cnt is the cnt of the 
    word
    '''
    htmlBig = 96
    htmlLittle = 14
    ratio = (cnt-low)/float(high-low)
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    wordStr = '<span style=\"font-size:%spx;\">%s</span>'
    return wordStr % (str(fontsize), word)


# example usage

pairs = [('hi',5),('there',6),('mom',10),('fred',2),('bill',20)]
highCount=20
lowCount=2
body=''
for word,cnt in pairs:
    body = body + makeHTMLword(word,cnt,highCount,lowCount) + ' '
box = makeHTMLbox(body)
printHTMLfile(box,'testFile')
