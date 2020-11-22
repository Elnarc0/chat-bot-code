#!C:\Python27\python.exe
print "Content-Type: text/html; charset=utf-8\n\n";
import random
import cgi

form =cgi.FieldStorage()
userInput = form.getvalue('inputt')


ls =[["althrocin","eltocin","erycin","eryocin plus"],
    ["calpol","pararite","arden","dolo","febrex","medomol"],
    ["cheston cold","okacet cold","cetrifos","elgnil cold","rhinoryl cz"],
    ["dolokind plus","aceclorite plus","aceclo plus","acenac","accemol"],
    ["ibuprofen","brupal","ibugesic"]]

lss =["althrocin","eltocin","erycin","eryocin plus","calpol","pararite","arden","dolo","febrex","medomol","cheston cold","okacet cold","cetrifos","elgnil cold","rhinoryl cz","dolokind plus","aceclorite plus","aceclo plus","acenac","accemol","ibuprofen","brupal","ibugesic"]

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?','how are you?','how are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)


def tab( userInput ):
    for elem in ls:
        if userInput in elem:
            print elem 
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

while True:
    	if userInput in greetings:
            print(random_greeting)
            break
	elif userInput in question:
            print(random_response)
            break
	elif userInput in lss:
	    tab( userInput )
	    break
	else:
	    print("I did not understand what you said")
	    break
