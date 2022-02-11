import webbrowser
import urllib.request
import ast
import json
import re
import os


def setUrl():
    
    url = 'https://secure.rec1.com/CA/cypress-recreation-community-services/catalog/getItems/b06dd2a58023baa31f9e4323d179f83a/'

    artsCraft = "2761"
    specialInterest = "2759"
    youthSports = "3057"
    dance = "2757"
    specialEvents = "2770"
    deucationEnrichment = "2758"
    sports = "2762"
    teenClasses = "8184"
    healthFitness = "2758"
    dayCamps = "2771"
    music = "2760"
    specialtyCamps = "2991"


    urlTest = url+artsCraft

    return grabSite(urlTest)

'''
arts&craft - 2761
specialInterest - 2759
youthSportsCa - 3057
dance-2757
specialEvents - 2770
educationEncrichment - 2758
sports - 2762
teenClasses - 8184
healthFitness - 2763
dayCamps - 2771
music - 2760
specialityCamps - 2991
'''



def grabSite(urlTest):
    #webbrowser.open(urlTest)
    fp = urllib.request.urlopen(urlTest)
    mystr = fp.read().decode('utf8') #contains all classes. For loop actually messes with the string
    fp.close()

    return textForm(mystr)


'''
mystr seems to be a list within a list. Might be able to format this much better.
Can perform a regex operation of a contains function.
'''


def textForm(classList):
    
    classListOutput = str(classList)

    classListOutput = classListOutput.replace("',", "',\n")
    classListOutput = classListOutput.replace("None,", "None,\n")
    classListOutput = classListOutput.replace("True,", "True,\n")
    classListOutput = classListOutput.replace("},", "\n},\n")
    classListOutput = classListOutput.replace("[]", "[]\n")
    classListOutput = classListOutput.replace("]", "]\n")
    classListOutput = classListOutput.replace("[{'", "[{\n'")
    classListOutput = classListOutput.replace("{'\n{'\n", "\n")
    classListOutput = classListOutput.replace("\\n", "{'\n")
    classListOutput = classListOutput.replace("\\r", "{'\r")
    classListOutput = classListOutput.replace("&amp;", "&")
    classListOutput = classListOutput.replace("{'\n","")
    classListOutput = classListOutput.replace(".\n{'\n","")
    classListOutput = classListOutput.replace("","")
    classListOutput = classListOutput.replace("\'id","{\'id")
    classListOutput = classListOutput.replace("\'name","{\'name")

    
    classListOutput = re.sub("</?[a-zA-Z]*>|<[a-zA-Z]* [a-zA-Z]*=\"[a-zA-Z]*: #[a-zA-Z]*\d*;\">|\n\n", "", classListOutput)
    classListOutput = re.sub("\n{'\n","{'\n",classListOutput)
    classListOutput = re.sub("\'","",classListOutput)
    classListOutput = re.sub("<.*>","",classListOutput)
    classListOutput = re.sub("&[a-zA-Z]*;","",classListOutput)
    classListOutput = classListOutput.replace("{\'","\'")
    classListOutput = classListOutput.replace("StudentsMUSTbe","Students MUST be")
    
    return classListOutput

def stop():
    quit()


#Convert string to dict (can't convert at the moment)
#myDict = ast.literal_eval(mystr)

#Convert string to list
#myList = mystr.split(',')

#Conver string to dict using json.loads
#myJson = json.loads(mystr)



#this produces another depth that I might have to change into another dictionary. 
#for k,v in myJson.items():
 #   if k == 'sections':
        #vStr = ''.join([str(elem) for elem in v])

        #need to convert dict v[0] to a string version first
  #      classList = v[0]
        
#print(type(classList))


#classListOutput = textForm(mystr)
#Think the line below will wrap everything in curly

  
def outFile(x):
    file_obj = open("output.txt", "w")
    file_obj.write(x)
    file_obj.close()
    os.startfile("output.txt")


if __name__ == "__main__":
    x = setUrl() #set the url string
    outFile(x)





