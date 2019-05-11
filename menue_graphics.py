import turtle

screen = turtle.Screen()


     
class menue_lables(turtle.Turtle):
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
        
        self.goto(self.coords[self.choice][0] - 100,
                  self.coords[self.choice][1] + 20)

    def change_up(self):
        
        if self.choice > 0:
            self.choice -= 1
        else:
            self.choice = len(self.coords) - 1

            
        self.goto(self.coords[self.choice][0] - 100,
                  self.coords[self.choice][1] + 20)

    def change_down(self):
        
        if self.choice < len(self.coords) - 1:
            self.choice += 1
        else:
            self.choice = 0

                       
        self.goto(self.coords[self.choice][0] - 100,
                  self.coords[self.choice][1] + 20)
        
