# Project-1
In the first python class of my CS degree, along with few classmates we developed this mini-project.
This project is developed using python and other libraries which I will be briefing about a little over here.

Understanding the project: 
Tkinter - This is a standard Python iterface to the Tk GUI Toolkit.We used this to create the simple GUI for the notepad.
And some other modules like os, wikipedia, datetime, random, and webbrowser. These can be understood easily by the requirement.
The main package required was pyttsx3 which is a Text to Speech Conversion library. So on the basis of the platform("Microsoft"), I intialised the driver to sapi5.

So basically when a user writes something on a notepad, he may want to surf over the net, to get some referrences for the document the user is working on. Here comes the part which was included in the notepad which may come in handy. There is a button called "Assistant" which when clicked, triggers the engine to recognize whatever query you speak onto the mic of the system like "Search Justin Bieber in wikipedia", "Play music", "Open Kindle", "Open Whatsapp", "Open Youtube", etc. And then it tries to recognise the keywords based on the inputs trained on. And executes the query by feeding it into the open function of the webbrowser module. And then this module will display a simple web based document in a new window of browser to the user without coming in way of his note-taking. 


(This was something I developed in a night, so I haven't added much of the support for the queries.) 


