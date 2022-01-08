import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print('~By Hαƈƙҽɾ σϝ ƚԋҽ Yҽαɾ~')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hello .")
            talk("welcome to the Sinhala Greek show!!!")
            talk("I am Chanux ORB")
            talk("To get a list of commands I can do, say HELP")
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def runChanuxOrb():
    command1 = take_command()
    print(command1)
    if command1 == 'help':
        print('play <song name>              = Plays a song you say on youtube.')
        print('time                          = Get the current time')
        print('who the heck is <person name> = Display person infromation found on Wikipedia')
        print('will you marry me             = Just try and see')
        print('joke                          = command itself says what it does')
        print('who made you                  = mamane ithim meka heduwe')
        print('How old are you               = age')
    elif 'play' in command1:
        song = command1.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command1:
        person = command1.replace('who the heck is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'are you single' in command1 or 'are you married' in command1 or 'will you marry me' in command1 or 'i love you' in command1:
        talk('I am about to marry SL Greek School')
    elif 'joke' in command1:
        talk(pyjokes.get_joke())
    elif 'who made you' in command1:
        talk('My creator is Hacker of the year who is not a hacker.He used Python to build me.')
    elif 'how old are you' in command1:
        talk('I am 456 years old.I still have a young voice.')
    else:
        talk('Please say the command again.')


while True:
    runChanuxOrb()