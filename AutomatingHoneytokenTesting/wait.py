import time

def runWait():
    print("Waiting for amazon mail server")
    time.sleep(30)  # wait for amazon mail server
    print("Done waiting!")

def runWaitUser():
    print("Waiting for user so they can see the screen")
    time.sleep(10)  # wait for user to see
    print("Done waiting!")

def runWaitBrowser():
    print("Waiting for page to load.")
    time.sleep(4)  # wait for browser
    print("Page should be loaded.")

def runWaitAlexa():
    print("Waiting for alexa.")
    time.sleep(10)  # wait for alexa to speak

if __name__ == '__runWait__': 
    runWait()

if __name__ == '__runWaitUser__': 
    runWaitUser()

if __name__ == '__runWaitBrowser__': 
    runWaitBrowser()

if __name__ == '__runWaitAlexa__': 
    runWaitAlexa()
