from easychat import App
import wikipedia

# This creates an object to hold your GUI in a variable called app
app = App("Jarvis") # Give it a Name
reply = app.input("Hello friend, what's your name?")
reply = reply.lower()
reply = reply.title()
reply = app.input("Hello, " + reply + ", how can I help you?")

while reply != 'bye':
    if 'think' in reply:
        reply = app.input("You're a very thoughtful person!")
    elif 'when' in reply:
        reply = app.input("What is time, really?")
    elif 'why' in reply:
        reply = app.input("Because that's just how it is, friend.")
    elif 'good' in reply:
        reply = app.input("There is no good while there is no liberty")
    elif 'dant' in reply:
        reply = app.input("Dant? Don't you mean Warden?")
    elif 'liberty' in reply:
        reply = app.input("Give me liberty or give me COMRATS!")
    elif 'where' in reply:
        x = reply[9: -1]
        summary = wikipedia.summary(x, auto_suggest = False, sentences=2)
        reply = app.input(summary)
    elif 'what' in reply:
        x = reply[8:-1]
        summary = wikipedia.summary(x, auto_suggest = False, sentences=2)
        reply = app.input(summary)
    elif 'who' in reply:
        x = reply[7: -1]
        summary = wikipedia.summary(x, auto_suggest = False, sentences=2)
        reply = app.input(summary)
    elif 'how old' in reply: #Works with John Kerry, not with people whose birth dates are listed in other formats
        x = reply[11:-1]
        summary = wikipedia.summary(x, auto_suggest = False, sentences=2)
        birth = summary.find('born')
        end_parenth = summary.find(')')
        #print(end_parenth)
        #print(birth)
        date = summary[(birth + 5):(end_parenth)]
        year = int(summary[end_parenth - 4: end_parenth])
        #print(year)
        age_yrs = 2021 - year
        age_yrs = str(age_yrs)
        x = x.title()
        reply = app.input(x + ' is ' + age_yrs + ' years old, give or take a year:)')
    else:
        reply = app.input("Tell me more.")
