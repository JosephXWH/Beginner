import easygui
flavor = easygui.enterbox("What's your favourite flavor?",
                          default = 'vanilla')
easygui.msgbox("you have entered" + flavor)