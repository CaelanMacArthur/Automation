#importing files
from getUtterances import runGetUtterrances
from Voice import runVoice
from changeEmail import runChangeMail

def main():
    runGetUtterrances()
    runVoice()
    runChangeMail()


    print("Running from main.py")

if __name__ == "__main__":
    main()

