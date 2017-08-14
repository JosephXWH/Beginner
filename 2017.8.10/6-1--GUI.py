import easygui
flavor = easygui.buttonbox("What's your favourite ice cream flavor?",
                 choices = ['vanilla','chocolate','strawberry'])

easygui.msgbox ("You picked" + flavor)


