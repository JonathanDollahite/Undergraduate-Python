from easychat import App

# This creates an object to hold your GUI in a variable called app
app = App("Jarvis") # Give it a Name
reply = app.input("Hello friend, what's your name?")
reply = reply.lower()
reply = reply.title()
reply = app.input("Hello, " + reply + ", how are you?")

while reply != 'bye':
    if 'think' in reply:
        reply = app.input("You're a very thoughtful person!")
    elif 'when' in reply:
        reply = app.input("What is time, really?")
    elif 'why' in reply:
        reply = app.input("Because that's just how it is, friend.")
    elif 'where' in reply:
        reply = app.input("It could be anywhere")
    elif 'what' in reply:
        reply = app.input("That's what.")
    elif 'good' in reply:
        reply = app.input("There is no good while there is no liberty")
    elif 'dant' in reply:
        reply = app.input("Dant? Don't you mean Warden?")
    elif 'liberty' in reply:
        reply = app.input("Give me liberty or give me COMRATS!")
    else:
        reply = app.input("Tell me more.")
