# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import os.path
import base64
import email
import os
from bs4 import BeautifulSoup
import json

# ======================= Beginnging of Googles Code=============================
 
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def runGetMail(): # change this so that it runs in main
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    #  ========================= End of googles code ========================== 
    # Call the Gmail API
    
    result = service.users().messages().list(maxResults=1, userId='me').execute()
    messages = result.get('messages')

   
    # iterate through all the messages
    for msg in messages:
        # Get the message from its id
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        # Use try-except to avoid any Errors
        try:
            # Get value of 'payload' from dictionary 'txt'
            payload = txt['payload']
            headers = payload['headers']

            # Look for Subject and Sender Email in the headers
            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']

            # The Body of the message is in Encrypted format. So, we have to decode it.
            # Get the data and decode it with base 64 decoder.
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)

            # Now, the data obtained is in lxml. So, we will parse
            # it with BeautifulSoup library
            soup = BeautifulSoup(decoded_data, "lxml")
            body = soup.body()

            # Printing the subject, sender's email and message
            # to make sure that it is working
            #print("Subject: ", subject)
            #print("From: ", sender)
            #print("Message: ", body)
            #print('\n')

            #setting email sections to variables
            varSubject = subject
            varSender = sender
            varBody = body

            #converting html to type string to be recorded
            strVarSubject = str(varSubject)
            strVarSender = str(varSender)
            strVarBody = str(varBody)

            #removing perivous OTP file
            os.remove("EmailOTP/onetimepassword.html")
            # recording the email to a file
            otpFile = open("EmailOTP/onetimepassword.html", "w")
            otpFile.write(strVarSubject)
            otpFile.write(strVarSender)
            otpFile.write(strVarBody)
            otpFile.write('\n')
            otpFile.close()
            with open("EmailOTP/onetimepassword.html") as fp:
                soup = BeautifulSoup(fp, "html.parser")
                varOTP = soup.find(class_="otp")
                toOTPStr = str(varOTP)
                finalOTP = toOTPStr.join(i for i in varOTP if i.isdigit())
                fp.close()

            optResults = open("EmailOTP/otpResults.txt", "w")
            optResults.write(finalOTP)
            optResults.write("\n")
            optResults.close()
        except:
            pass

if __name__ == '__runGetMail__':
    runGetMail()
# [END gmail_quickstart]
