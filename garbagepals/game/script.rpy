# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Here we define the backgrounds that are used.
image bg dumpster = "assets/dumpster.jpg"
image bg trashcan = "assets/trashcan.jpg"

# Declare characters used by this game.
define d = Character('Dumpster', color="#c8ffc8")
define t = Character('Trashcan', color="#c8ffc8")


# the game starts here.
label start:
    $ bearhappy = 0
    $ bearanger = 0
    $ raccoonhappy = 0
    $ raccoonanger = 0
    $ question = ''
    scene bg dumpster

    d "Hi! I'm Dumpster"

    scene bg trashcan

    t "Hi! I'm Trashcan"

    jump checkandrandom

    #return

label checkandrandom:
if bearhappy > 3:
    if raccoonhappy >3:
        jump happyend
    else:
        pass
elif bearanger >2:
    jump badendbear
elif raccoonanger >2:
    jump badendraccoon
else:
    $ question = renpy.random.randint(1, 13)
if question == 1:
    jump zero
elif question == 2:
    jump one
elif question == 3:
    jump two
elif question == 4:
    jump three
elif question == 5:
    jump four
elif question == 6:
    jump five
elif question == 7:
    jump six
elif question == 8:
    jump seven
elif question == 9:
    jump eight
elif question == 10:
    jump nine
elif question == 11:
    jump ten
elif question == 12:
    jump eleven
elif question == 13:
    jump twelve



label zero:
d "Am I garbage?"

menu:

    "Yes":
        $ bearhappy += 1
        jump checkandrandom
    "No":
        $ bearanger -= 1
        jump checkandrandom

label one:
    d "Am I garbage?"
    menu:
        "Yes":
            $ bearhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label two:

    t "Am I garbage?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label three:
    d "Do I have opposable thumbs?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label four:

    t "Do I have opposable thumbs?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label five:

    d "Does my fur look clean?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

    t "Does my fur look clean?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label six:

    d "Are humans awful?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label seven:

    t "Are humans awful?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label eight:

    d "Want to pet my nose?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label nine:

    t "Wanna pet my tail?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label ten:

    d "Do you like running?"
    menu:
        "Yes":
            $ bearhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label eleven:

    t "Do you like running?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label twelve:

    t "Do I ever get sweaty?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label thirteen:

    d "Am I endangered?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom


label happyend:
    d "I wanna smooch smooch smooch"
    t "I also wanna smooch smooch smooch"
    "You all smooch whatever the end"
    return

label badendbear:
    d "Roar I don't trust you you make me uncomfortable I'm gonna EAt YOU NOW"
    "bad end"
    return

label badendraccoon:
    t "Fack u raccons r the worst hiss '3'"
    "bad end"
    return
