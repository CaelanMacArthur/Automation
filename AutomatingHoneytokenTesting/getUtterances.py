from selenium import webdriver
from time import time
import json
import string
import os
import shutil

#invoke browser
driver = webdriver.Chrome(executable_path= r" Path to selenium driver") # TODO Remove your path and put "Put chrome driver path here"

def runGetUtterrances():

   #directory for screenshots
   dirDataScrap = "Screenshots/SeleniumScreenshots/DataScraping/"

   # times for files
   timeTaken = time()
   convertTimeTaken = str(timeTaken)

   getTheUrlUserWants = input("What url would you like to get utterances from? Recommended that you copy and paste in URL.\n")
   driver.save_screenshot('Utterances/screenshot.png')

   # Moving files around for Amazon Email Enter screenshots
   ogScreenshot = 'Utterances/screenshot.png'
   old_file_name = ogScreenshot
   new_file_name = convertTimeTaken + ".png"
   os.rename(old_file_name, new_file_name)
   shutil.move(new_file_name, dirDataScrap + new_file_name)

   convertToList = str(getTheUrlUserWants) # converting user input
   driver.get(convertToList) #getting user input from web
   varUtterances = driver.find_elements_by_class_name("a2s-utterance-text")
   utteranceList = [] # empty list for utterances
   utteranceList.clear() # remove perivous utterances

   # iterate through list and get text
   for utterance in range(len(varUtterances)):

      print("Just got the utterances!")
      print("\n")
      innerCheck = 0

      for data in varUtterances: # setting user input to list

         if innerCheck == 1: # check to make that program does not duplicate results
            break
         else:
            utteranceList.append(data.text)
            innerCheck += 1

   finalizedDictionary = [] #setting empty dictionary for cleaned data
   for theString in utteranceList:

      if (theString != ""): #parsing only letters exist
         finalizedDictionary.append(theString)

   """" Recording to utteranceData """
   dataUtterance = json.dumps(finalizedDictionary)
   theFile = open("Utterances/utterancesData.txt", "w")
   theFile.write(dataUtterance)
   theFile.write("\n")
   theFile.close()

   for varString in utteranceList:
      qoutesOne = '"'
      qoutesTwo = '"'
      if (varString != string.digits,string.punctuation,qoutesOne,qoutesTwo): #parsing only letters exist
         theFile = open("Utterances/utterancesData.txt", "w")
         #print("instead if statement")
         theFile.write(varString)
         theFile.write("\n")
         theFile.close()

   driver.quit() #closing browser

if __name__ == '__runGetUtterrances__': 
   runGetUtterrances()
