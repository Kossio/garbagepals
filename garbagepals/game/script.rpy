# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Here we define the backgrounds that are used.
image bg dumpster = "assets/dumpster.jpg"
image bg trashcan = "assets/trashcan.jpg"
image bg trash = "assets/trash.jpg"
image overlay youdied = "assets/youdied.png"

# And this is the character art we use.
image dumpster default = "assets/bear.png"
image trashcan default = "assets/raccoon.png"

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
    $ question = renpy.random.randint(1, 15)
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
elif question == 14:
    jump thirteen
elif question == 15:
    jump fourteen



label zero:
scene bg trash
show dumpster default
d "Am I garbage?"

menu:

    "Yes":
        $ bearhappy += 1
        jump checkandrandom
    "No":
        $ bearanger += 1
        jump checkandrandom

label one:
    scene bg trash
    show dumpster default
    d "Am I garbage?"
    menu:
        "Yes":
            $ bearhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label two:
    scene bg trash
    show trashcan default
    t "Am I garbage?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label three:
    scene bg trash
    show dumpster default
    d "Do I have opposable thumbs?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label four:
    scene bg trash
    show trashcan default
    t "Do I have opposable thumbs?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label five:
    scene bg trash
    show dumpster default
    d "Does my fur look clean?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label fourteen:
    scene bg trash
    show trashcan default
    t "Does my fur look clean?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label six:
    scene bg trash
    show dumpster default
    d "Are humans awful?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label seven:
    scene bg trash
    show trashcan default
    t "Are humans awful?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label eight:
    scene bg trash
    show dumpster default
    d "Want to pet my nose?"
    menu:
        "Yes":
            $ bearanger += 1
            jump checkandrandom
        "No":
            $ bearhappy += 1
            jump checkandrandom

label nine:
    scene bg trash
    show trashcan default
    t "Wanna pet my tail?"
    menu:
        "Yes":
            $ raccoonanger += 1
            jump checkandrandom
        "No":
            $ raccoonhappy += 1
            jump checkandrandom

label ten:
    scene bg trash
    show dumpster default
    d "Do you like running?"
    menu:
        "Yes":
            $ bearhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label eleven:
    scene bg trash
    show trashcan default
    t "Do you like running?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ bearanger += 1
            jump checkandrandom

label twelve:
    scene bg trash
    show trashcan default
    t "Do I ever get sweaty?"
    menu:
        "Yes":
            $ raccoonhappy += 1
            jump checkandrandom
        "No":
            $ raccoonanger += 1
            jump checkandrandom

label thirteen:
    scene bg trash
    show dumpster default
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
    show overlay youdied
    "bad end"
    return

label badendraccoon:
    t "Fack u raccons r the worst hiss '3'"
    show overlay youdied
    "bad end"
    return
