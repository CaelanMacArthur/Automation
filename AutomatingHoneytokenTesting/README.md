# Automation testing for Alexa HoneyTokens

## Problem 
<br>

The problem the software is trying to solve is to create a program that mostly automates the testing of Amazon Alexa using honeytokens. Full automation would require some additional development, but is not beyond the scope of the capability of the program. 

## Solution 
<br>

##Automated testing does the following: 

1. Scrapes utterances from the Alexa skills store.
2. Uses a voice synthesizer to talk to Alexa, and records Alexa’s responses 
3. Automates changing of emails for honeytokens. 
4. Automates getting the one-time password for prompted by Amazon web portal. 
5. Retrieves a two-factor authentication code sent by OAuth your accounts google voice number when third-party skills require it. 
6. File management for recording utterances files (.mp3 & .wav), file management for recording screenshots while data scraping, changing emails, getting text messages for Oath, and one-time passwords prompted by Amazon’s security portal.  

## User flow of Program  
<br>
1. The getUtterances class data scrapes the Alexa skill store with the URL provided by the user and passes them into Voice.py.  
<br>
2. Voice.py handles the recording/creating voice synthesizer to talk to Alexa and records Alexa responses. 
<br>
3. The changeEmail.py class changes the email and enters the one-time password in the Amazon web portal. 
<br> 
4. The getMail class gets the one-time password and passes it back to changeEmail.  
<br>
5. The wait.py class simply tells the program to wait a specified amount of time. It is done this wait because “ctime” and “from time import time” break “import time”.

## Setup / Dependencies 
<br>

##### Dependencies to install:  

1. [gTTS - Google text to speech](https://pypi.org/project/gTTS/) to create text to speech. Here are [gTTS docs](https://gtts.readthedocs.io/en/latest/) for reference. 
2. [Playsound](https://pypi.org/project/playsound/) to play audio. 
3. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) to record Alexa responses.  
4. [Pydub](https://anaconda.org/conda-forge/pydub) to help break up large files and combine them back together. This works well SpeechRecognition. SpeechRecognition loses audio translation sometimes without it.
5. Pydub needs [ffmpeg](https://anaconda.org/conda-forge/ffmpeg) to run. See [here](https://github.com/jiaaro/pydub/issues/348) for bug and fix. 
6. [Selenium Python bindings](https://selenium-python-test.readthedocs.io/en/latest/installation.html) 
7. For getting Gmail one time password pip install --upgrade [google-api-python-client](https://developers.google.com/gmail/api/quickstart/python) google-auth-httplib2 google-auth-oauthlib.  
8. [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) for parsing through HTML.  

## Required software 

1. Google [developer](https://console.developers.google.com/) console. 
2. Amazon Account  
3. Amazon Alexa  
4. Gmail account that is 54 characters (google supports up 254, but amazon limits characters). 
5. Gmail API
6. [Selenium](https://www.selenium.dev/downloads/) web driver chrome (if you prefer a different driver it should work fine. May have issues with safari) 

## Recommended software:

1. IDE PyCharm 
2. Windows 10 OS (may work on macOS and Linux)  
3. [Anaconda](https://www.anaconda.com/products/individual)

## Helpful Documentation and Guides  

1. [Selenium Python bindings docs](https://selenium-python.readthedocs.io/installation.html)
2. Gmail [API](https://developers.google.com/gmail/api) docs 
3. Python [quickstart](https://developers.google.com/gmail/api/quickstart/python) for Gmail 
4. Reference [documentation](https://developers.google.com/gmail/api/reference/rest/v1/Format) for Gmail  
5. Check [E-mail](https://www.youtube.com/watch?v=njDGaVnz9Z8) Messages with Python and Gmail API | #34 (Gmail API #1) 
6. Setting up [OAuth](https://support.google.com/googleapi/answer/6158849?hl=en) 2.0 - API Console Help 
7. Create [credentials](https://developers.google.com/workspace/guides/create-credentials) | Google Workspace for Developers (note you must have a project created already with the Gmail API)

Side note it might be helpful when using the Gmail API to set the default view for the Gmail view to load as HTML only. It is much easier for the getMail class to parse through HTML versus CSS and Javascript.  

## Possible Errors When Setting Up 

1. [Permissions](https://stackoverflow.com/questions/39818922/errno-13-permission-denied-file-mp3-python) Error
2. If you are trying to install on Ubuntu or other linux systems this error may come up "[Cannot](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error) install pyaudio Ubuntu, 20.04 LTS". 
3. ModuleNotFoundError: No module named 'gi' when using playground lib. This only happens on Linux, but not on windows. Possible [solution](https://askubuntu.com/questions/80448/what-would-cause-the-gi-module-to-be-missing-from-python)
4. line 858, in recognize_google if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError() speech_recognition.UnknownValueError. Solution is [here](https://github.com/Uberi/speech_recognition/issues/383). 

## Limitations / Workarounds 
<br>

##### Testing skills in different languages
<br>

To test in different languages, they need to have different language codes. Currently, it is English (“'en-us”), and to change to other languages during testing switch language codes. You can simply just get the language codes from [here](https://en.wikipedia.org/wiki/Language_localisation).To change languages in voice.py go to line 117 and change language='en position to the language code you wish to test.

##### Future Challenges and Roadblock for Automation Software 

###### Problem 

* Getting past Multi-factor authentication

###### Solution 

* Creating a google voice number and using [pygooglevoice](https://pypi.org/project/pygooglevoice/) library to sign in and get the OAuth authentication code. 

###### Problem
*  Selenium is getting stopped by reCaptcha.

###### Solution
* Common [solutions](https://stackoverflow.com/questions/58872451/how-can-i-bypass-the-google-captcha-with-selenium-and-python) for reCaptcha are listed in this StackOverflow forum. [Fakeuseragent](https://pypi.org/project/fake-useragent/) framework is a framework that imitates user behavior. There is a suggested [solution](https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium/49565254#49565254) for Fakeuseragent in this StackOverflow forum. For more complex reCaptcha here is another possible solution with the 
[dessant-buster](https://github.com/dessant/buster) and here is a [tutorial](https://medium.com/analytics-vidhya/how-to-easily-bypass-recaptchav2-with-selenium-7f7a9a44fa9e).   


## Future Plans

###### Future Development of the Automation Software 

1) Give the program the skills IDs we want to test and have the program parse through the original dataset. That should give the program the skill name.  
2) After we have the skills name it is given to selenium put that name into the search bar of the Alexa skills store. 
3) It finds a match then it can click on that webpage of the skill ID you wanted to test. 
Web scrape that page for those utterances and then stick them into the voice synthesizer. That way the only thing we would have to do is give the program the skill ids for it to parse through.
4) To get the OAuth authentication code you would have to use google voice number and [pygooglevoice](https://pypi.org/project/pygooglevoice/) library to sign in and get the one-time code.  

## Code Changes to Make During Implementation

In Voice.py on 130 "w" in the variable, jsonFile needs to be changed to "a" for append, otherwise, the JSON file will be overwritten. 
