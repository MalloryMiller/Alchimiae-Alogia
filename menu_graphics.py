import turtle

screen = turtle.Screen()


     
class menu_lables(turtle.Turtle):
    def __init__(self, lable, coords):
        super().__init__()
        self.lable = lable
        self.color(1, 1, .98)
        self.pu()
        self.ht()
        
        self.goto(coords[0], coords[1])
        self.write(self.lable, False, 'center', ('Calabri', 25))


        
class selection_cursor(turtle.Turtle):
    def __init__(self, coords):
        super().__init__()
        
        self.color(1, .98, 1)
        self.pu()
        self.shapesize(2)
        
        self.meanin = []
        self.coords = []

        for x in coords:
            self.meanin.append(x[0][0])
            self.coords.append(x[1])
            
        self.choice = 0
        
        self.goto(self.coords[self.choice][0] - 70,
                  self.coords[self.choice][1] + 20)


        if self.coords[self.choice][1] == -125:
            self.goto(self.coords[self.choice][0] - 70,
                      self.coords[self.choice][1] + 35)

        screen.update()
        
    def change_up(self):
        
        if self.choice > 0:
            self.choice -= 1
        else:
            self.choice = len(self.coords) - 1

            
        self.goto(self.coords[self.choice][0] - 70,
                  self.coords[self.choice][1] + 20)

        if self.coords[self.choice][1] == -125:
            self.goto(self.coords[self.choice][0] - 70,
                      self.coords[self.choice][1] + 35)
            
        screen.update()

    def change_down(self):
        
        if self.choice < len(self.coords) - 1:
            self.choice += 1
        else:
            self.choice = 0

                       
        self.goto(self.coords[self.choice][0] - 70,
                  self.coords[self.choice][1] + 20)

        if self.coords[self.choice][1] == -125:
            self.goto(self.coords[self.choice][0] - 70,
                      self.coords[self.choice][1] + 35)
        
        screen.update()
        
class key_instructions(turtle.Turtle):
    def __init__(self, up, down, enter):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(0, -260)
        self.color('white')
        self.write("Use the {} key and the {} key to\n\
change the selection and \n\
the {} key to choose the selected item.".format(
    up.split('\n')[0], down.split('\n')[0], enter.split('\n')[0]),
                   None, 'center')


    
