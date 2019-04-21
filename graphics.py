import turtle
import time as t

screen = turtle.Screen()
screen.tracer(100, 100)

# self.write("    " + name, False, 'left', ("Arial", 15, 'bold'))


image1 = 'button1.gif'
image2 = 'button2.gif'



alchem1 = 'alchem1.gif'
alchem2 = 'alchem2.gif'
alchem3 = 'alchem3.gif'
alchem4 = 'alchem4.gif'
alchem5 = 'alchem5.gif'

mehcla1 = 'mehcla1.gif'
mehcla2 = 'mehcla2.gif'
mehcla3 = 'mehcla3.gif'
mehcla4 = 'mehcla4.gif'
mehcla5 = 'mehcla5.gif'



azurea1 = 'azurea1.gif'
azurea2 = 'azurea2.gif'
azurea3 = '.gif'
azurea4 = '.gif'
azurea5 = '.gif'

aeruza1 = 'aeruza1.gif'
aeruza2 = 'aeruza2.gif'
aeruza3 = '.gif'
aeruza4 = '.gif'
aeruza5 = '.gif'



incwar1 = '.gif'
incwar2 = '.gif'
incwar3 = '.gif'
incwar4 = '.gif'
incwar5 = '.gif'

rawcni1 = '.gif'
rawcni2 = '.gif'
rawcni3 = '.gif'
rawcni4 = '.gif'
rawcni5 = '.gif'



starkn1 = '.gif'
starkn2 = '.gif'
starkn3 = '.gif'
starkn4 = '.gif'
starkn5 = '.gif'

nkrats1 = '.gif'
nkrats2 = '.gif'
nkrats3 = '.gif'
nkrats4 = '.gif'
nkrats5 = '.gif'



bckgrd = 'stage.gif'


screen.addshape(image1)
screen.addshape(image2)

screen.addshape(alchem1)
screen.addshape(alchem2)
screen.addshape(alchem3)
screen.addshape(alchem4)
screen.addshape(alchem5)

screen.addshape(mehcla1)
screen.addshape(mehcla2)
screen.addshape(mehcla3)
screen.addshape(mehcla4)
screen.addshape(mehcla5)


screen.addshape(azurea1)
screen.addshape(azurea2)
##screen.addshape(azurea3)
##screen.addshape(azurea4)
##screen.addshape(azurea5)

screen.addshape(aeruza1)
screen.addshape(aeruza2)
##screen.addshape(aeruza3)
##screen.addshape(aeruza4)
##screen.addshape(aeruza5)

screen.bgpic(bckgrd)


button_coords = [-240, -80, 80, 240]

class Button(turtle.Turtle):
    def __init__(self, lable, x):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.speed(100)

        self.shape(image1)
        self.goto(x, -200)
        self.color(0.11, 0.11, 0.24)

        if len(lable.split(" ")) == 2:
            for y in lable.split(" "):
                self.write(y, False, 'center', ("Calabri", 15, "bold"))
                self.forward(-20)
        else:
            self.forward(-10)
            self.write(lable, False, 'center', ("Calabri", 15, "bold"))

        self.goto(x, -200)
        self.available = True
        self.lable = lable

    def unavailable(self):
        self.shape(image2)

    def available(self):
        self.shape(image1)

    def select(self):
        print("whoa", lable)



class GroupOf4Buttons(turtle.Turtle):
    def __init__(self, lables):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.speed(100)

        self.ch1 = Button(lables[0], button_coords[0])
        self.ch2 = Button(lables[1], button_coords[1])
        self.ch3 = Button(lables[2], button_coords[2])
        self.ch4 = Button(lables[3], button_coords[3])
        self.buttons = [self.ch1, self.ch2, self.ch3, self.ch4]

        self.shape('classic')
        self.color(0.89, 0.89, 0.76)
        self.goto(0, 50)

        self.select_opt = 0
        self.lables = lables
        self.goto(button_coords[self.select_opt], -240)
        self.shapesize(2)


    def select_button(self, change_opt):
        self.select_opt += change_opt
        
        if self.select_opt > 3:
            self.select_opt = 0
        elif self.select_opt < 0:
            self.select_opt = 3
        self.goto(button_coords[self.select_opt], -240)
        
        return self.select_opt


class bar_lable(turtle.Turtle):
    def __init__(self, host):
        self.host = host
        
    def change_value(self, value):
        pass



image_coords = {

    "alchem": {  # PLAYER ALCHEMIST
        
        alchem1: [-161, -13],  # image_displayed: [coordx, coordy], 
        alchem2: [-143, -20],
        alchem3: [-148, -10],
        alchem4: [-156, -14], 
        alchem5: [-198, -83]

        }, 
    
    "mehcla": {  # ENEMY ALCHEMIST
        
        mehcla1: [169, -14], 
        mehcla2: [127, -18],
        mehcla3: [150, -12],
        mehcla4: [154, -13], 
        mehcla5: [202, -85]

        },

    "azurea": {  # PLAYER ARCHER
        
        azurea1: [-161, -36], 
        azurea2: [-119, -34],
        azurea3: [-148, -10],
        azurea4: [], 
        azurea5: [-198, -90]

        }, 
    
    "aeruza": {  # ENEMY ARCHER
        
        aeruza1: [175, -34], 
        aeruza2: [116, -36],
        aeruza3: [150, -12],
        aeruza4: [], 
        aeruza5: [202, -85]

        },

    "incwar": {  # PLAYER WARRIOR
        
        incwar1: [-161, -13], 
        incwar2: [-143, -20],
        incwar3: [-148, -10],
        incwar4: [], 
        incwar5: [-198, -83]

        }, 
    
    "rawcni": {  # ENEMY WARRIOR
        
        rawcni1: [169, -14], 
        rawcni2: [127, -18],
        rawcni3: [150, -12],
        rawcni4: [], 
        rawcni5: [202, -85]

        },

    "starkn": {  # PLAYER KNIGHT
        
        starkn1: [-161, -13], 
        starkn2: [-143, -20],
        starkn3: [-148, -10],
        starkn4: [], 
        starkn5: [-198, -83]

        }, 
    
    "nkrats": {  # ENEMY KNIGHT
        
        nkrats1: [169, -14], 
        nkrats2: [127, -18],
        nkrats3: [150, -12],
        nkrats4: [], 
        nkrats5: [202, -85]

        }
    
    
    }




class visual(turtle.Turtle):

    def __init__(self, player_type):
        super().__init__()
        self.penup()
        self.st()
        self.playert = player_type

    def change_image(self, image):
        
        self.goto(image_coords[self.playert][image][0],
                  image_coords[self.playert][image][1])
        
        self.shape(image)
        screen.update()



class visualFigure(visual):

    def __init__(self, player_type):
        
        super().__init__(player_type)
        
        self.shapes = []
        for k in image_coords[self.playert]:
            self.shapes.append(k)
            
        self.goto(image_coords[self.playert][self.shapes[0]][0],
                  image_coords[self.playert][self.shapes[0]][1])
        
        self.shape(self.shapes[0])
        
        screen.update()


    def attacking(self):
        self.change_image(self.shapes[1])
        t.sleep(.75)
        self.change_image(self.shapes[0])


    def take_damage(self):
        self.change_image(self.shapes[2])
        for x in range(4):
            self.ht()
            screen.update()
            t.sleep(.125)
            self.st()
            screen.update()
            t.sleep(.25)
        self.change_image(self.shapes[0])

    def healing(self):
        self.change_image(self.shapes[3])
        t.sleep(.75)
        self.change_image(self.shapes[0])

    def lose(self):
        self.change_image(self.shapes[4])
        screen.update()


ti = visualFigure('azurea')
ti.attacking()



