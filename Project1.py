import datetime
import random
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from ttkthemes import themed_tk as tk
from tkinter import ttk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
print(voices)
b = ['Good Morning!', 'Guten Morgan!', 'Bonjour!']
b = random.choice(b)
c = ['Good Afternoon!', 'Guten Tag!', 'Bonne après-midi!']
c = random.choice(c)
d = ['Good Evening!', 'Guten Abend! ', 'Bonsoir!']
d = random.choice(d)


class operations:
 def oper(self):
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greetings():
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour <= 12:
            speak(b)
        elif hour >= 12 and hour < 18:
            speak(c)
        else:
            speak(d)

        speak("Hello !!,I Am Your Notepad Assistant , How May I Help You ?")

    def fetchcommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.............")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognising.......")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n ")

        except Exception as e:
            print("Repeat it Again Please...")
            return 'None'
        return query

    if __name__ == '__main__':
        greetings()
        if 1:
            query = fetchcommand().lower()
            if "wikipedia" in query:
                speak("Searching Wikipedia For You!")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia!")
                print(results)
                speak(results)
            elif "open facebook" in query:
                webbrowser.open("facebook.com")
            elif "open whatsapp" in query:
                webbrowser.open("web.whatsapp.com")
            elif "open instagram" in query:
                webbrowser.open("instagram.com")
            elif "open snaptube" in query:
                webbrowser.open("snaptube.com")
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open translator" in query:
                webbrowser.open("googletranslator.com")
            elif "open goodreads" in query:
                webbrowser.open("goodreads.com")
            elif "open google" in query:
                webbrowser.open("google.com")
            elif "open kindle" in query:
                webbrowser.open("kindle.com")
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open dictionary" in query:
                webbrowser.open("dictionary.com")
            elif "play music" in query:
                music_dir = "C://Users//karth//Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif "time" in query:
                nowtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The Time is!!{nowtime}")
            else:
                speak("Sorry Didn't Get You!")

class Notepad(operations):
    __root = tk.ThemedTk()
    __root.get_themes()
    __root.set_theme('plastik')
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisAssistantMenu = Menu(__thisMenuBar, tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Visual Insanity")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)

        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
        self.__thisMenuBar.add_command(label="Assitant",
                                       command=self.__oper)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __oper(self):
        self.oper()

    def __showAbout(self):
        showinfo("Notepad", "TEAM KAN")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            self.__file = None
        else:

            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:

            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        self.__root.mainloop()


notepad = Notepad(width=600, height=400)
notepad.run()
