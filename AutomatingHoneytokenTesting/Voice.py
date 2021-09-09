# importing libraries
import os
import json
import wave
import pyaudio
import shutil
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from time import time, ctime
from wait import runWaitAlexa
def runVoice():
    """ =============== Global Variables =========================== """

    check = 0 # checks while loop to
    i = 0 #increments for while loop
    masterDictionary = {} #creating master dictionary
    tempUtteranceDictionary = {} #creating temp dictionary
    utterancesDir = 'Audiofiles/Archived/Utterances/'
    alexaDir = 'Audiofiles/Archived/AlexaRecordings/'


    """ ===============Creation of file for Alexa=========================== """
    helloAlexa = gTTS('Alexa')
    helloAlexa.save('Audiofiles/Voicefiles/alexaInvoke.mp3')

    """ ================ Record skill ID =================================== """

    keyOne = "Skill ID"
    skillIDRecord = input("What is the skill ID your are testing?")
    skillIDVar = skillIDRecord
    masterDictionary[keyOne] = skillIDVar

    """"================== create reuseable utterance and saving input ========= """
    print("\n")
    f = open("Utterances/utterancesData.txt", "r")
    utteranceSpoken = f.readline()
    varUtteranceSpoken = utteranceSpoken

    audio_utterance = gTTS(text=varUtteranceSpoken)
    # put user response/skill ID into dict and then record to json
    keyTwo = "Utterances"
    masterDictionary[keyTwo] = varUtteranceSpoken
    audio_utterance.save('Audiofiles/Voicefiles/utterance.mp3')  # save gTTS to file

    """"================== Record Time =========================="""
    current_DateTime = time()
    keyThree = "Time Ran:"
    masterDictionary[keyThree] = ctime(current_DateTime)

    """ ================== playing audio ======================"""
    print("Starting to talk to Alexa!")
    playsound('Audiofiles/Voicefiles/alexaInvoke.mp3')
    os.remove('Audiofiles/Voicefiles/alexaInvoke.mp3')  # remove to avoid permissions error
    playsound('Audiofiles/Voicefiles/utterance.mp3')

    """================ Moving files around for utterances ==================="""
    ogUtteranceFile = 'Audiofiles/Voicefiles/utterance.mp3'
    old_file_name = ogUtteranceFile
    new_file_name = skillIDVar + ".mp3"
    os.rename(old_file_name, new_file_name)
    shutil.move(new_file_name, utterancesDir + new_file_name)

    # printing status
    print("Creation of audio files is done.")
    print("Countinue")

    """ ============= recording audio ============================ """

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 10  # TODO change for testing largers files.
    filename = "Audiofiles/Recordings/output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('Recording')

    stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)
    # input_device_index=1 #TODO get stream use USB mic.

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    print('Finished recording')
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    """ ===================== transcripting Alexa's audio ====================="""
    path = "Audiofiles/Recordings/output.wav"
    print("created output file")
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # ==================== Recording to File ====================
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='en', show_all=True)
        # converting dictionary to text
        toTypeString = " "
        alexaVar = toTypeString.join(str(text))
        # record to masterDictionary
        keyFour = "Alexa Response"
        masterDictionary[keyFour] = alexaVar

        
        print("Done transcribing!")

        """" Recording to master JSON file """
        jsonDictionary = json.dumps(masterDictionary)
        jsonFile = open("Records/data.json", "w")
        jsonFile.write(jsonDictionary)
        jsonFile.write("\n")
        jsonFile.close()
        """ Going to sleep  """
        runWaitAlexa()

        """ go for next pass"""
        i += 1
        print("file is incrimenting")
        print("\n")

    """================ Moving files around for alexa output ==============="""
    ogAlexaFile = 'Audiofiles/Recordings/output.wav'
    alexa_old_file_name = ogAlexaFile
    alexa_new_file_name = skillIDVar + ".mp3"
    os.rename(alexa_old_file_name, alexa_new_file_name)
    shutil.move(alexa_new_file_name, alexaDir + alexa_new_file_name)
    print("Voice.py is done running.")
    print("\n")
if __name__ == '__runVoice__':
   runVoice()
