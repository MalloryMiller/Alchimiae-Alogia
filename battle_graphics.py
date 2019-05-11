import turtle
import time as t


screen = turtle.Screen()




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



incwar1 = 'incwar1.gif'
incwar2 = 'incwar2.gif'
incwar3 = 'incwar3.gif'
incwar4 = 'incwar4.gif'
incwar5 = 'incwar5.gif'

rawcni1 = 'rawcni1.gif'
rawcni2 = 'rawcni2.gif'
rawcni3 = 'rawcni3.gif'
rawcni4 = 'rawcni4.gif'
rawcni5 = 'rawcni5.gif'



starkn1 = 'starkn1.gif'
starkn2 = 'starkn2.gif'
starkn3 = 'starkn3.gif'
starkn4 = 'starkn4.gif'
starkn5 = 'starkn5.gif'

nkrats1 = 'nkrats1.gif'
nkrats2 = 'nkrats2.gif'
nkrats3 = 'nkrats3.gif'
nkrats4 = 'nkrats4.gif'
nkrats5 = 'nkrats5.gif'



bckgrd_stage = 'stage.gif'
bckgrd_curtain = 'curtain.gif'


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


screen.addshape(incwar1)
screen.addshape(incwar2)
screen.addshape(incwar3)
screen.addshape(incwar4)
screen.addshape(incwar5)

screen.addshape(rawcni1)
screen.addshape(rawcni2)
screen.addshape(rawcni3)
screen.addshape(rawcni4)
screen.addshape(rawcni5)


screen.addshape(starkn1)
screen.addshape(starkn2)
screen.addshape(starkn3)
screen.addshape(starkn4)
screen.addshape(starkn5)

screen.addshape(nkrats1)
screen.addshape(nkrats2)
screen.addshape(nkrats3)
screen.addshape(nkrats4)
screen.addshape(nkrats5)




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

        incwar1: [-162, 7],
        incwar2: [-125, 6],
        incwar3: [-178, 25],
        incwar4: [-151, 5],
        incwar5: [-173, -70]

        },

    "rawcni": {  # ENEMY WARRIOR

        rawcni1: [161, 7],
        rawcni2: [124, 4],
        rawcni3: [176, 26],
        rawcni4: [148, 7],
        rawcni5: [178, -66]

        },

    "starkn": {  # PLAYER KNIGHT

        starkn1: [-232, 11],
        starkn2: [-219, -37],
        starkn3: [-267, 2],
        starkn4: [-233, -83],
        starkn5: [-274, -95]

        },

    "nkrats": {  # ENEMY KNIGHT

        nkrats1: [244, 15],
        nkrats2: [219, -36],
        nkrats3: [268, 7],
        nkrats4: [235, -83],
        nkrats5: [272, -95]

        }


    }









button_coords = [-240, -80, 80, 240]

def game_over(winner, loser, final_blow):
    screen.clear()
    screen.bgpic(bckgrd_curtain)
    end_screen(winner, loser, final_blow)
    


# BUTTONS

class Button(turtle.Turtle):
    def __init__(self, lable, x, unavailable_level, multi):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.speed(100)
        self.x = x

        self.lable = lable
        self.multi = multi
        self.cutoff = unavailable_level
        self.lable = lable


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


    
        self.color('white')
        
        self.goto(self.x - 20, -270)
        self.write("            "  + str(self.multi) + "\n   Power\nMultiplier", False, 'right',
                   ("Calabri", 8))
        
        self.goto(self.x + 23, -270)
        self.write(str(self.cutoff) + "\nStamina\nCost", False, 'left',
                   ("Calabri", 8))



        self.goto(x, -200)

        self.avail = True

    def unavailable(self):
        if self.avail:
            self.shape(image2)
            self.color('black')
            self.clear()

            if len(self.lable.split(" ")) == 2:
                for y in self.lable.split(" "):
                    self.write(y, False, 'center', ("Calabri", 15, "bold"))
                    self.forward(-20)
            else:
                self.forward(-10)
                self.write(self.lable, False, 'center', ("Calabri", 15, "bold"))

            self.color('grey')
            
            self.goto(self.x - 20, -270)
            self.write("            "  + str(self.multi) + "\n   Power\nMultiplier", False, 'right',
                       ("Calabri", 8))
            
            self.goto(self.x + 23, -270)
            self.write(str(self.cutoff) + "\nStamina\nCost", False, 'left',
                       ("Calabri", 8))


            self.goto(self.x, -200)

            self.avail = False

        

    def available(self):

        if not self.avail:
            self.shape(image1)
            self.color(0.11, 0.11, 0.24)
            self.clear()

            if len(self.lable.split(" ")) == 2:
                for y in self.lable.split(" "):
                    self.write(y, False, 'center', ("Calabri", 15, "bold"))
                    self.forward(-20)
            else:
                self.forward(-10)
                self.write(self.lable, False, 'center', ("Calabri", 15, "bold"))

            self.color('white')
            
            self.goto(self.x - 20, -270)
            self.write("            "  + str(self.multi) + "\n   Power\nMultiplier", False, 'right',
                       ("Calabri", 8))
            
            self.goto(self.x + 23, -270)
            self.write(str(self.cutoff) + "\nStamina\nCost", False, 'left',
                       ("Calabri", 8))



            self.goto(self.x, -200)
            self.avail = True


    def option_selected(self, stamina_leftover):
        
        if stamina_leftover < self.cutoff:
            self.unavailable()
        else:
            self.available()
            



class GroupOf4Buttons(turtle.Turtle):
    def __init__(self, lables, cutoff_stamina, multi):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.speed(100)


        self.ch1 = Button(lables[0], button_coords[0], cutoff_stamina[0], multi[0])
        self.ch2 = Button(lables[1], button_coords[1], cutoff_stamina[1], multi[1])
        self.ch3 = Button(lables[2], button_coords[2], cutoff_stamina[2], multi[2])
        self.ch4 = Button(lables[3], button_coords[3], cutoff_stamina[3], multi[3])
        
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





# ONSCREEN TEXT


class flavorText(turtle.Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        if side == 'left':
            self.goto(-320, 200)
        else:
            self.goto(320, 200)
        self.pendown()


        self.ht()
        self.color('white')
        self.text = ''
        self.side = side
        self.write(self.text, False, self.side, ("Calabri", 7, "italic"))

    def change_text(self, update_as):
        self.clear()
        self.text = update_as
        self.write(self.text, False, self.side, ("Calabri", 7, "italic"))



class txt_w_bkgrd(turtle.Turtle):
    def __init__(self, bkgrd_color = 'white'):
        super().__init__()
        self.ht()
        self.pu()
        self.speed(100)
        self.bg_color = bkgrd_color
        
        self.key_file = open('key_settings.txt', 'r')
        self.keys = self.key_file.readlines()

        for x in range(len(self.keys)):
            self.keys.insert(x, self.keys.pop(x).split('\n')[0])

    def writeWbg(self, what_do):
        wha = what_do.split('\n')
        self.clear()
        self.pensize(40)
        self.setheading(0)
        
        self.color('white')
        self.goto(-180, 16)
        self.pd()
        self.fd(360)
        
        self.color('black')
        self.pu()
        self.goto(0, 0)
        self.write(what_do, False, 'center', ("Calabri", 9, 'bold'))
        



class popup_confirm(txt_w_bkgrd):
    def __init__(self):
        super().__init__()
        self.open = False
        
    def closing(self):
        self.open = False
        self.clear()
        screen.update()
        
    def opening(self):
        self.open = True
        self.writeWbg("Are you sure you want to exit?\nYour game will not save (" +
                      self.keys[7] + " for yes/" + self.keys[8] +" for no).")
        screen.update()


class tutorial_text(txt_w_bkgrd):
    def __init__(self, tutorial = True):
        super().__init__('black')
            
        
        self.color('white')
        
        if tutorial:
            self.intro = True
            self.arrow_dir = True
            self.health_bar = True
            self.stamina_bar = True
            self.stamina_inc = True
            self.attacks = True
            self.lables = True
            self.heal = True
            self.random = True
            self.enter = True
            self.fun = True
        else:
            self.intro = False
            self.arrow_dir = False
            self.health_bar = False
            self.stamina_bar = False
            self.stamina_inc = False
            self.attacks = False
            self.lables = False
            self.heal = False
            self.random = False
            self.enter = False
            self.fun = False

    def write_bold(self, what_do):
        wha = what_do.split('\n')
        y = 175
        
        if len(wha) == 1:
            biggest = wha[0]
            y = 167
            self.pensize(20)
            
        elif wha[0] > wha[1]:
            biggest = wha[0]
            self.pensize(40)
            
        else:
            biggest = wha[1]
            self.pensize(40)

        self.goto((len(biggest) * -6), y)
        
        self.color('black')
        
        self.setheading(0)
        
        self.pd()
        self.fd(len(biggest * 12))
        self.pu()

        self.goto(0, 158)

        self.color('white')
        self.write(what_do, False, 'center', ("Courier", 9, 'bold'))

        screen.update()
        

    def check_change(self):
        self.clear()
        txt = ''

        
        if self.intro:
            txt = "You are on the left, your enemy is on the right \
(press " + self.keys[5] + " to move to the next \ntutorial page, " \
+ self.keys[6] + " to skip the tutorial, and " + self.keys[4] + " t\
o exit to the menue)."
            self.intro = False

        
        elif self.arrow_dir:
            txt = "Use the " + self.keys[0] + " and " + self.keys[1] + \
            " keys to change the button you have selected."
            self.arrow_dir = False


        elif self.health_bar:
            txt = "The green bar is your health. \nWhen it meets or goes \
under 0, you will lose."
            self.health_bar = False


        elif self.stamina_bar:
            txt = "The blue bar is your stamina. Every action costs stamina. \
If you don't \nhave enough stamina to do something, the button for that actio\
n will turn grey."
            self.stamina_bar = False

        elif self.stamina_inc:
            txt = "At the beginning of each of your turns \
you will gain 4 stamina."
            self.stamina_inc = False


        elif self.attacks:
            txt = "The first three buttons are attacks. You can tell how \
powerful an attack is \n\
            by its Power Multiplier."
            self.attacks = False


        elif self.lables:
            txt = "How much stamina an action costs is shown under and to the right\n\
of the button, while the other number is the Power Multiplier."
            self.lables = False


        elif self.heal:
            txt = "The last button on the right is to heal."
            self.heal = False

        elif self.random:
            txt = "Every action's value is randomized, so there's no set \
value for attacking or healing.\nPower Multipliers increase the base that \
the random number is added to."
            self.random = False

        elif self.enter:
            txt = "Use the " + self.keys[2] + " key to choose an action."
            self.enter = False


        elif self.fun:
            txt = "Have fun!"
            self.fun = False

        else:
            return
            
        self.write_bold(txt)
            

    def skip_tutorial(self):
        self.clear()
        self.arrow_dir = False
        self.health_bar = False
        self.stamina_bar = False
        self.stamina_inc = False
        self.attacks = False
        self.lables = False
        self.heal = False
        self.random = False
        self.enter = False
        self.fun = False
            
            


                   
    
class end_screen(turtle.Turtle):
    def __init__(self, winner, loser, final_blow):
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.write(winner.t + " prevailed using " + final_blow + "!",
                   False, 'center', ("Calabri", 20, "italic"))
        self.goto(0, -25)
        
        self.key_file = open('key_settings.txt', 'r')
        self.keys = self.key_file.readlines()
        
        self.write("Press " + self.keys[3] + " to restart.", False, 'center')



# HEALTH + STAMINA BARS


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




# PLAYER AND ENEMY DRAWINGS


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
        t.sleep(1.5)


