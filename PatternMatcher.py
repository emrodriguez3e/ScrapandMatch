import webbrowser, urllib.request, ast, json, re, os

def setUrl():

    '''
    Should attempt to make the portion after getItems to be dynamic if possible.
    That way if the numbers change, it won't be an issue.
    '''
    url = 'https://secure.rec1.com/CA/cypress-recreation-community-services/catalog/getItems/b06dd2a58023baa31f9e4323d179f83a/'

    #set all class locations
    classCategories = {'artsCraft': '2761',
                       'specialInterest': '2759',
                       'youthSports': '3057',
                       'specialEvents': '2770',
                       'educationEnrichment': '2758',
                       'sports': '2762',
                       'teenClasses': '8184',
                       'healthFitness': '2758',
                       'dayCamps': '2771',
                       'music': '2760',
                       'specialtyCamps': '2991'
                       }

    '''
    Current sections at the moment.
    Had to go into web developer mode to find the numbers below under the network tab
    artsCraft = "2761"
    specialInterest = "2759"
    youthSports = "3057"
    dance = "2757"
    specialEvents = "2770"
    educationEnrichment = "2758"
    sports = "2762"
    teenClasses = "8184"
    healthFitness = "2758"
    dayCamps = "2771"
    music = "2760"
    specialtyCamps = "2991"
    '''

    #urlTest = url+artsCraft

    #create empty string that will be used to merge all class lists together
    myStr = ""

    #for each category, get the text version
    for values in classCategories.values():
        urlTest = url+values

        myStr += grabSite(urlTest)
        
    return textForm(myStr)


def grabSite(urlTest):
    #webbrowser.open(urlTest)
        
    fp = urllib.request.urlopen(urlTest)
    mystr = fp.read().decode('utf8') #contains all classes. For loop actually messes with the string
    fp.close()

    return mystr

def textForm(classList):
    
    classListOutput = str(classList) #convert text into string directly

    #regex 
    classListOutput = re.sub("{","{\n",classListOutput)
    classListOutput = re.sub("},{","},\n{",classListOutput)
    classListOutput = re.sub("\",\"","\",\n\"",classListOutput)
    classListOutput = re.sub("null,","null,\n",classListOutput)
    classListOutput = re.sub("true,","true,\n",classListOutput)
    classListOutput = re.sub("false,","false,\n",classListOutput)
    classListOutput = re.sub("</?[a-zA-z]*>|<\\\/[a-zA-Z]*>|&nbsp;","",classListOutput)
    classListOutput = re.sub("<[a-zA-z]* .*>","",classListOutput) 
    classListOutput = re.sub("}],","}],\n",classListOutput)
    classListOutput = re.sub("\\\/"," ",classListOutput)

    #hard replace
    classListOutput = classListOutput.replace("[],","[],\n")
    classListOutput = classListOutput.replace("}","\n}")
    classListOutput = classListOutput.replace("\\r","")
    classListOutput = classListOutput.replace("\\n","")
    
    return classListOutput

#Made for testing purposes I suppose. 
def stop():
    quit()

def outFile(classList):
    file_obj = open("output.txt", "w")
    file_obj.write(classList)
    file_obj.close()
    os.startfile("output.txt")

if __name__ == "__main__":
    classList = setUrl() #set the url string
    outFile(classList)

