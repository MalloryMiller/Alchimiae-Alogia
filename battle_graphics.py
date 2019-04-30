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
azurea3 = 'azurea3.gif'
azurea4 = 'azurea4.gif'
azurea5 = 'azurea5.gif'

aeruza1 = 'aeruza1.gif'
aeruza2 = 'aeruza2.gif'
aeruza3 = 'aeruza3.gif'
aeruza4 = 'aeruza4.gif'
aeruza5 = 'aeruza5.gif'



incwar1 = 'incwar.gif'
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
screen.addshape(azurea3)
screen.addshape(azurea4)
screen.addshape(azurea5)

screen.addshape(aeruza1)
screen.addshape(aeruza2)
screen.addshape(aeruza3)
screen.addshape(aeruza4)
screen.addshape(aeruza5)


##screen.addshape(incwar1)
##screen.addshape(incwar2)
##screen.addshape(incwar3)
##screen.addshape(incwar4)
##screen.addshape(incwar5)
##
##screen.addshape(rawcni1)
##screen.addshape(rawcni2)
##screen.addshape(rawcni3)
##screen.addshape(rawcni4)
##screen.addshape(rawcni5)
##
##
##screen.addshape(starkn1)
##screen.addshape(starkn2)
##screen.addshape(starkn3)
##screen.addshape(starkn4)
##screen.addshape(starkn5)
##
##screen.addshape(nkrats1)
##screen.addshape(nkrats2)
##screen.addshape(nkrats3)
##screen.addshape(nkrats4)
##screen.addshape(nkrats5)




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
        azurea3: [-205, -54],
        azurea4: [-185, -91], 
        azurea5: [-179, -89]

        }, 
    
    "aeruza": {  # ENEMY ARCHER
        
        aeruza1: [175, -34], 
        aeruza2: [116, -36],
        aeruza3: [201, -54],
        aeruza4: [181, -92], 
        aeruza5: [176, -86]

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


    

class vis_bar(turtle.Turtle):

    def __init__(self, host, side, direction = None):
        super().__init__()
        self.host = host
        self.ht()
        
        self.max_val = host.host_value
        self.num = host.host_value
        self.direction = direction

        if direction == 'up':
            self.setheading(90)
            
            self.penup()
            if side == 'left':
                self.start_bar = [-300, -60]
                self.goto(self.start_bar[0], self.start_bar[1])
            else:
                self.start_bar = [300, -60]
                self.goto(self.start_bar[0], self.start_bar[1])
            self.pendown()

            self.color(0, 0, .3)  # darker blue
        
        
        else:
            self.penup()
            if side == 'left':
                self.start_bar = [-320, 240]
                self.goto(self.start_bar[0], self.start_bar[1])
            else:
                self.start_bar = [320, 240]
                self.goto(self.start_bar[0], self.start_bar[1])
                self.setheading(180)
            self.pendown()
        

            self.color('dark green')

        if direction == 'up':
            
            self.pensize(30)
            self.fd(self.max_val * 8)
            self.fd(self.max_val * -8)
            self.pensize(20)

            b = .5
            for y in range(int(self.max_val)):
                self.color(0, 0, b)
                b += 0.02
                self.fd(8)

        else:
            
            self.pensize(15)
            self.fd(self.max_val * 2)
            self.fd(self.max_val * -2)
            self.pensize(10)
            
            g = .5
            for y in range(self.max_val):
                self.color(0, g, 0)  # bright green
                g += .002
                self.fd(2)
        
        screen.update()

    def change_value(self, value, special_color = None):
        self.num = value
        
        self.clear()
        self.penup()
        self.goto(self.start_bar[0], self.start_bar[1])
        self.pendown()

        if self.direction == 'up':
            self.color(0, 0, .3)
            if special_color == 'red':
                self.color(.3, 0, 0)
            self.pensize(30)
            self.fd(self.max_val * 8)
            self.fd(self.max_val * -8)
            
            self.pensize(20)      

            b = .5
            for y in range(int(value)):
                self.color(0, 0, b)
                if special_color == 'red':
                    self.color(b, 0, 0)
                b += 0.02
                self.fd(8)

        else:
        
            self.color('dark green')
            self.pensize(15)
            self.fd(self.max_val * 2)
            self.fd(self.max_val * -2)
            
            self.pensize(10)
            
            x = .5
            for y in range(value):
                self.color(0, x, 0)  # bright green
                x += .002
                self.fd(2)
        screen.update()

    def not_enough_stam(self):
        for x in range(3):
            self.clear()
            screen.update()
            t.sleep(.1)
            self.change_value(self.num, 'red')
            screen.update()
            t.sleep(.2)
        self.change_value(self.num)
            
        
        
class Bar(turtle.Turtle):
    def __init__(self, host_value, side):
        super().__init__()
        self.ht()
        self.host_value = host_value
        self.side = side
        
        
    def change_value(self, value):
        self.clear()
        self.write(int(value), False, 'center', ("Calabri", 15, "bold"))
        self.vis.change_value(value)
        pass


class health_bar(Bar):
    
    def __init__(self, host_value, side):
        super().__init__(host_value, side)
        
        self.penup()
        if self.side == 'left':
            self.start_bar = [-300, 250]
            self.goto(self.start_bar[0], self.start_bar[1])
        else:
            self.start_bar = [300, 250]
            self.goto(self.start_bar[0], self.start_bar[1])
            self.setheading(180)
        self.pendown()
        
        self.color(.6, .9, .6)  # pale green
        self.write(host_value, False, 'center', ("Calabri", 15, "bold"))
        

        self.vis = vis_bar(self, side)

class stamina_bar(Bar):

    def __init__(self, host_value, side):
        super().__init__(host_value, side)
        
        self.penup()
        if self.side == 'left':
            self.start_bar = [-300, -100]
            self.goto(self.start_bar[0], self.start_bar[1])
        else:
            self.start_bar = [300, -100]
            self.goto(self.start_bar[0], self.start_bar[1])
            self.setheading(180)
        self.pendown()
        
        self.color(.75, .75, .9)  # pale blue
        self.write(host_value, False, 'center', ("Calabri", 15, "bold"))

        self.vis = vis_bar(self, side, 'up')

    def not_enough_stam(self):
        self.clear()
        self.color(.9, .75, .75)  # pale red
        self.write(int(self.vis.num), False, 'center', ("Calabri", 15, "bold"))

        self.vis.not_enough_stam()

        self.clear()
        
        self.color(.75, .75, .9)  # pale blue
        self.write(int(self.vis.num), False, 'center', ("Calabri", 15, "bold"))

        




    
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


