#
#My first program that prints Hello World
#JD Dollahite
#
from easygui import *
nick_name = 'blinktwice2'
msgbox('Hello loser')
msgbox("I'm hungry")
msgbox('And I just want to sleep')
msgbox("But I can't go back to bed until I talk to you, so let's get this over with.")
usr_name = str(enterbox("What's your name?"))
msgbox('How does it feel to have such a dumb sounding name ' + usr_name + '?')
msgbox("My name is " + nick_name + '. ' + "I bet you blinked when you read it")
ans1 = str(enterbox('Would you rather have one real get out of jail free card or a key that opens any door? Why?'))
msgbox('You make a good point when you say ' + ans1 + ', ' + 'but I would have to take the other side')
ans2 = str(enterbox('Would you rather have all traffic lights you approach be green or never have to stand in line again?'))
msgbox("I couldn't agree with you more " + usr_name + " and I think you're right in saying that " + ans2 + " is the best choice.")
ans3 = str(enterbox("One last question. Would you rather go back to age 5 with everything you know now or know now everything your future self will learn?"))
msgbox("Did you actually say you'd want to " + ans3 + '? ' + " You're a bigger idiot than I thought. I don't think we'll get along.")
msgbox("goodbye")
quit()
