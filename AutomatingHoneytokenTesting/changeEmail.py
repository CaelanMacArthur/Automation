import shutil
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import time
from getMail import runGetMail
from wait import runWait
from wait import runWaitUser

def runChangeMail():

    #invoke browser
    driver = webdriver.Chrome(executable_path= r"path of selenium drive")

    #directories
    amazonDirHome = "Screenshots/SeleniumScreenshots/Amazon/Home/"
    amazonDirSignIn = "Screenshots/SeleniumScreenshots/Amazon/SignIn/"
    amazonDirEmail = "Screenshots/SeleniumScreenshots/Amazon/Email/"
    amazonDirPassword = "Screenshots/SeleniumScreenshots/Amazon/Password/"

    #times for files
    amazonTime = time()
    convertAmazonTime = str(amazonTime)

    """" ================== Amazon Selection =====================================  """

    driver.get("https://www.amazon.com/") # get amazon
    driver.save_screenshot('Screenshots/resultsAmazonHome.png')
    print(driver.current_url)
    # Moving files around for Amazon Homepage screenshots

    ogAmazonHomeFile = 'Screenshots/resultsAmazonHome.png'
    old_file_name = ogAmazonHomeFile
    new_file_name = convertAmazonTime + ".png"
    os.rename(old_file_name, new_file_name)
    shutil.move(new_file_name, amazonDirHome + new_file_name)

    # Getting login page and beginning to log in
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    driver.save_screenshot('Screenshots/resultsAmazonLogin.png')

    # Moving files around for Amazon Login Screenshots

    ogAmazonLoginFile = 'Screenshots/resultsAmazonLogin.png'
    old_file_name = ogAmazonLoginFile
    new_file_name = convertAmazonTime + ".png"
    os.rename(old_file_name, new_file_name)
    shutil.move(new_file_name, amazonDirEmail + new_file_name)

    print(driver.current_url)

    # Entering email address
    emailLogin = driver.find_element_by_id('ap_email')
    emailLogin.send_keys("test gmail") #entering email address in felid (TODO remember to delete email address after you are done)
    emailLogin.send_keys(Keys.RETURN) # hit return after you enter search text
    driver.save_screenshot('Screenshots/resultsAmazonEmail.png')

    # Moving files around for Amazon Email Enter screenshots
    ogAmazonEmailFile = 'Screenshots/resultsAmazonEmail.png'
    old_file_name = ogAmazonEmailFile
    new_file_name = convertAmazonTime + ".png"
    os.rename(old_file_name, new_file_name)
    shutil.move(new_file_name, amazonDirEmail + new_file_name)

    print(driver.current_url)

    # password section  for Amazon
    passwordLogin = driver.find_element_by_id('ap_password')
    passwordLogin.send_keys("password") #entering password in felid
    passwordLogin.send_keys(Keys.RETURN)
    driver.save_screenshot('Screenshots/resultsAmazonPassword.png')

    # Moving files around for Amazon Email Enter screenshots
    ogAmazonPasswordFile = 'Screenshots/resultsAmazonPassword.png'
    old_file_name = ogAmazonPasswordFile
    new_file_name = convertAmazonTime + ".png"
    os.rename(old_file_name, new_file_name)
    shutil.move(new_file_name, amazonDirPassword + new_file_name)

    print(driver.current_url)

    # getting to change email page
    driver.get("https://www.amazon.com/ap/cnep?ie=UTF8&orig_return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-account&openid.assoc_handle=usflex&pageId=usflex&openid.assoc_handle=usflex&openid.claimed_id=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AHT7HRJZAPZTQMCZKF3T43KJWS4Q&openid.identity=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AHT7HRJZAPZTQMCZKF3T43KJWS4Q&openid.mode=id_res&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.op_endpoint=https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin&openid.response_nonce=2021-08-03T20%3A22%3A29Z1527593693029365742&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fap%2Fcnep%3Fie%3DUTF8%26orig_return_to%3Dhttps%253A%252F%252Fwww.amazon.com%252Fyour-account%26openid.assoc_handle%3Dusflex%26pageId%3Dusflex&openid.signed=assoc_handle%2Cclaimed_id%2Cidentity%2Cmode%2Cns%2Cop_endpoint%2Cresponse_nonce%2Creturn_to%2Cns.pape%2Cpape.auth_policies%2Cpape.auth_time%2Csigned&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.auth_policies=http%3A%2F%2Fschemas.openid.net%2Fpape%2Fpolicies%2F2007%2F06%2Fnone&openid.pape.auth_time=2021-08-03T20%3A22%3A29Z&openid.sig=P3R1K2pOEAkOlY6SY0fH3HEg1bQy4yBC%2FPN%2BLEb3dPc%3D&serial=&")
    getToChangeEmailPage = driver.find_element_by_id("auth-cnep-edit-email-button")
    getToChangeEmailPage.click()

    #At the email page and now entering the email.
    changeEmail = driver.find_element_by_name("cvf_email")
    changeEmail.send_keys("") 
    changeEmail.send_keys(Keys.RETURN)
    runWait()

    #Getting one time password from gmail
    runGetMail() # calling getMail to OTP from Gmail
    with open('EmailOTP/otpResults.txt', 'r') as file:
        data = file.read().replace('\n', '')
        dataStr = str(data)
    enterOTP = driver.find_element_by_name('code')
    enterOTP.send_keys(dataStr)
    enterOTP.send_keys(Keys.RETURN)

    finalStep = driver.find_element_by_id('ap_password')
    finalStep.send_keys("enter in password")  # entering password in felid 
    runWaitUser()
    finalStep.send_keys(Keys.RETURN)

    # Add in screenshot features and moving those screenshots around.
    driver.quit() #close all windows/browser

if __name__ == '__runChangeMail__': # for now run this here in order to get it to start working properly
    runChangeMail()
