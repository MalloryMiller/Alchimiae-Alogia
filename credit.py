import turtle as t
from fractions import Fraction
import menu as m
import sound_management as sm



screen = t.Screen()
keys_settings_file = open('key_settings.txt', 'r')
list_keys = keys_settings_file.readlines()
leave_screen_key = list_keys[4].split('\n')[0]

def credits_page():
    sm.submenu_music()
    screen.clear()
    screen.reset()
    screen.bgcolor(0, 0, 0)
    screen.tracer(1000, 1000)
    
    class credit(t.Turtle):
        def __init__(self):
            super().__init__()
            self.pu()
            self.ht()
            self.goto(100, -260)
            self.color('white')
            self.write("\
    CREDITS\n\
\n\
Beta Testers:\n\
        Willow B.\n\
        Bella L.\n\
        David M.\n\
        Mary M.\n\
        Virginia P.\n\
        Andi W.\n\
\n\
Teacher:\n\
        Mr. H. Roberts\n\
\n\
Programmed with Python\n\
\n\
Art drawn with Sketchbook Express Pro\n\
\n\
Music mixed on EarSketch with Python\n\
\n\
\n\
\
", False, 'right', ('Calabri', 15, 'bold'))

    class instructions(t.Turtle):
        def __init__(self):
            super().__init__()
            self.color('white')
            self.ht()
            self.pu()
            self.goto(270, 250)
            self.write("Press " + leave_screen_key + " to go back to the menu.",
                       False, 'right', ('Calabri', 10, 'italic'))
            
    crdt = credit()
    inst = instructions()
    screen.onkey(m.menu_page, leave_screen_key)
    screen.update()


