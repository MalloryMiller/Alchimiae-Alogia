import menu as m
import turtle as t
import sound_management as sm

blue = [0.5, 0.5, 1]
red = [1, .5, .5]

chosen_setting = [0]
screen = t.Screen()

def full_settings_page(chosen_setting = chosen_setting):
    sm.submenu_music()
    different_key_uses = []

    screen.reset()
    screen.clear()
    screen.tracer(100000, 100000)
    screen.bgcolor(0, 0, 0)


    class key(t.Turtle):
        def __init__(self, current_val, deffault_val, desc, coords, pos):
            super().__init__()
            different_key_uses.append(self)
            self.ht()
            self.pos = pos
            self.val = current_val
            self.desc = desc
            self.deffault = deffault_val
            self.coords = coords

            self.clear()
            self.x = self.coords[0] - 20
            self.y = self.coords[1] + 9

            self.color('white')
            self.pu()
            self.st()
            self.goto(self.coords[0], self.coords[1])
            self.write(self.desc + self.val, None, 'left', ('Calabri', 11))
            self.goto(self.x, self.y)
            self.shapesize(2)

            self.color('gray')
            screen.update()



        def select(self, x = 0, y = 0, chosen_setting = chosen_setting):
            

            
            different_key_uses[chosen_setting[0]].unselect()

            chosen_setting.insert(0, self.pos)
            del chosen_setting[1]

            self.color('white')
            screen.update()



        def unselect(self, x = 0, y = 0):
            self.color('gray')
            screen.update()

        def defaul_unselect(self, x = 0, y = 0):
            if self.pos == chosen_setting[0]:
                self.color('white')
                
            else:
                self.color('gray')

            screen.update()



        def new_key(self, key = None, color = 'white'):
            if key == None:
                key = self.deffault
            self.clear()
            self.val = key

            self.goto(self.coords[0], self.coords[1])
            self.color('white')
            self.write(self.desc + self.val, None, 'left', ('Calabri', 11))
            self.goto(self.coords[0] - 20, self.coords[1] + 9)
            self.color(color)
            

            screen.update()

        def default_key(self, x = 0, y = 0):
            self.new_key(self.deffault, blue)

    coords = [

        [-260, 100],
        [-260, 50],
        [-260, 0],
        [-260, -50],
        [-260, -100],
        [-260, -150],
        [80, 100],
        [80, 50],
        [80, 0],
        [80, -50],
        [80, -100]

        ]




    battle_keys_file = open('key_settings.txt', 'r')
    list_keys = battle_keys_file.readlines()

    # ALL OF THE DIFFERENT EDITABLE KEYS:
    left = key(list_keys[0].split('\n')[0], 'Left',
                  'Change selection to the left: ', coords[0], 0)
    right = key(list_keys[1].split('\n')[0], 'Right',
                   'Change selection to the right: ', coords[1], 1)
    retur = key(list_keys[2].split('\n')[0], 'Return',
               'Choose an option: ', coords[2], 2)
    r = key(list_keys[3].split('\n')[0], 'r',
                  'Restart a game from the end screen: ', coords[3], 3)
    escape = key(list_keys[4].split('\n')[0], 'Escape',
                    'Exit to menu: ', coords[4], 4)
    space = key(list_keys[5].split('\n')[0], 'space',
                   'Move to next tutorial page: ', coords[5], 5)
    x = key(list_keys[6].split('\n')[0], 'x',
               'Skip tutorial: ', coords[6], 6)
    y = key(list_keys[7].split('\n')[0], 'y',
               'Confirm leaving to menu: ', coords[7], 7)
    n = key(list_keys[8].split('\n')[0], 'n',
               'Decline leaving to menu: ', coords[8], 8)
    up = key(list_keys[9].split('\n')[0], 'Up',
                'Change selection upward: ', coords[9], 9)
    down = key(list_keys[10].split('\n')[0], 'Down',
                  'Change selection downward: ', coords[10], 10)

    battle_keys_file.close()

    tt = [0]

    def check_t(t = tt):
        if len(t) >= 10:
            for p in different_key_uses:
                p.x += 5
                p.goto(p.x, p.y)
                p.shape('turtle')
            t = [0]



    def set_key(key):
        different_key_uses[chosen_setting[0]].new_key(key)



    def set_key_1():
        set_key('1')

    def set_key_2():
        set_key('2')

    def set_key_3():
        set_key('3')

    def set_key_4():
        set_key('4')

    def set_key_5():
        set_key('5')

    def set_key_6():
        set_key('6')

    def set_key_7():
        set_key('7')

    def set_key_8():
        set_key('8')

    def set_key_9():
        set_key('9')

    def set_key_0():
        set_key('0')

    def set_key_delete():
        set_key('Delete')

    def set_key_tab():
        set_key('Tab')

    def set_key_q():
        set_key('q')

    def set_key_w():
        set_key('w')

    def set_key_e():
        set_key('e')

    def set_key_r():
        set_key('r')

    def set_key_t(tt = tt):
        set_key('t')
        tt.append(0)
        check_t()

    def set_key_y():
        set_key('y')

    def set_key_u():
        set_key('u')

    def set_key_i():
        set_key('i')

    def set_key_o():
        set_key('o')

    def set_key_p():
        set_key('p')

    def set_key_a():
        set_key('a')

    def set_key_s():
        set_key('s')

    def set_key_d():
        set_key('d')

    def set_key_f():
        set_key('f')

    def set_key_g():
        set_key('g')

    def set_key_h():
        set_key('h')

    def set_key_j():
        set_key('j')

    def set_key_k():
        set_key('k')

    def set_key_l():
        set_key('l')

    def set_key_semicolon():
        set_key(';')

    def set_key_apostrophe():
        set_key("'")

    def set_key_return():
        set_key('Return')

    def set_key_z():
        set_key('z')

    def set_key_x():
        set_key('x')

    def set_key_c():
        set_key('c')

    def set_key_v():
        set_key('v')

    def set_key_b():
        set_key('b')

    def set_key_n():
        set_key('n')

    def set_key_m():
        set_key('m')

    def set_key_comma():
        set_key(',')

    def set_key_period():
        set_key('.')

    def set_key_slash():
        set_key('/')

    def set_key_space():
        set_key('space')

    def set_key_home():
        set_key('Home')

    def set_key_end():
        set_key('End')

    def set_key_left():
        set_key('Left')

    def set_key_right():
        set_key('Right')

    def set_key_up():
        set_key('Up')

    def set_key_down():
        set_key('Down')

    def set_key_escape():
        set_key('Escape')




    keys_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Delete',
            'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Return',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',
            'space', 'Home', 'End', 'Left', 'Right', 'Up', 'Down', 'Escape']



    keys_n_functs = {'1': set_key_1, '2': set_key_2, '3': set_key_3, '4': set_key_4, '5': set_key_5,
                     '6': set_key_6, '7': set_key_7, '8': set_key_8, '9': set_key_9, '0': set_key_0, 'Delete': set_key_delete,
                     'Tab': set_key_tab, 'q': set_key_q, 'w': set_key_w, 'e': set_key_e, 'r': set_key_r,
                     't': set_key_t, 'y': set_key_y, 'u': set_key_u, 'i': set_key_i, 'o': set_key_o, 'p': set_key_p,
                     'a': set_key_a, 's': set_key_s, 'd': set_key_d, 'f': set_key_f, 'g': set_key_g, 'h': set_key_h,
                     'j': set_key_j, 'k': set_key_k, 'l': set_key_l, ';': set_key_semicolon, "'": set_key_apostrophe, 'Return': set_key_return,
                     'z': set_key_z, 'x': set_key_x, 'c': set_key_c, 'v': set_key_v,
                     'b': set_key_b, 'n': set_key_n, 'm': set_key_m, ',': set_key_comma, '.': set_key_period, '/': set_key_slash,
                     'space': set_key_space, 'Home': set_key_home, 'End': set_key_end, 'Left': set_key_left, 'Right': set_key_right,
                     'Up': set_key_up, 'Down': set_key_down, 'Escape': set_key_escape}







    class buttons_for_settings(t.Turtle):
        def __init__(self, color):
            super().__init__()
            self.c = color


        def clicking(self, x = 0, y = 0):
            self.color(self.c)
            screen.update()
            self.funct()

        def click_off(self, x = 0, y = 0):
            self.color('gray')
            screen.update()


    class buttons_w_functs(buttons_for_settings):
        def __init__(self, lable, funct, coords, side = 'right', \
                     size = 15, color = blue):
            super().__init__(color)
            self.c = color            
            self.shape('circle')
            self.color('white')
            self.funct = funct
            self.size = size
            self.pu()
            self.goto(coords[0], coords[1])
            self.write(lable, None, side, ('Calabri', self.size))
            if side == 'right':
                self.goto(coords[0] + 30, coords[1] + 12)
            elif side == 'left':
                self.goto(coords[0] - 30, coords[1] + 12)
            elif side == 'center':
                self.goto(coords[0], coords[1])
            self.color('gray')
            self.onclick(self.clicking)
            self.onrelease(self.click_off)
            screen.update()



    instructions = None


    def default_keys(battle_keys_file = battle_keys_file):
        for x in different_key_uses:
            x.default_key()
            x.defaul_unselect()


        battle_keys_file = open('key_settings.txt', 'w')
        battle_keys_file.write('Left\nRight\nReturn\nr\nEscape\n\
space\nx\ny\nn\nUp\nDown')



    def save_changes(battle_keys_file = battle_keys_file):
        new_stuff = ''
        for x in different_key_uses:
            if not x.val in new_stuff.split('\n'):
                new_stuff += x.val + '\n'
            else:
                instructions.bad_save()
                return

        instructions.good_save()

        battle_keys_file = open('key_settings.txt', 'w')
        battle_keys_file.write(new_stuff)


    class instructions(t.Turtle):
        def __init__(self):
            super().__init__()
            self.pu()
            self.ht()
            self.goto(300, 145)
            self.color('white')
            self.write("\
To select a key binding to change, left click the \n\
arrow pointing to it. A selected option's \n\
arrow will be white, and you may then press \n\
on the keyboard the new key you \n\
want to replace the old one with. \n\
The circular buttons may be clicked on \n\
to preform any action they sit next to.\n\
Right click an arrow to reset it to its default.\
", None, 'right', ('Calabri', 10))

            for x in [

                ['Save New Keys', save_changes, [-180, -250], 'left'],
                ['Menu', m.menu_page, [-200, 200], 'left'],
                ['Default All Settings', default_keys, [180, -250], 'right'],
                

                 ]:

                buttons_w_functs(x[0], x[1], x[2], x[3])
            self.bad = False

        def bad_save(self):
            self.goto(-200, -200)
            self.color(red)
            self.write("Two or more of your settings share the same key.\n\
You must fix this before you can save.")
            self.bad = True

        def good_save(self):
            if self.bad:
                self.undo()



    class sound_setting(buttons_w_functs):
        def __init__(self, funct):
            self.stt = open("musicon.txt", 'r')
            self.current_setting = int(self.stt.readlines()[0])
            print(self.current_setting)
            self.stt.close()
            
            if self.current_setting:
                self.lable = 'Turn Music Off'
                self.clr = 'white'
            else:
                self.lable = 'Turn Music On'
                self.clr = 'grey'

            
            super().__init__(self.lable, funct, [80, -150], 'left', 10)
            self.color(self.clr)

            

        def clicking(self, x = 0, y = 0):
            self.color(blue)
            screen.update() 
            self.clr = self.funct(self)

        def click_off(self, x = 0, y = 0):
            self.color(self.clr)
            screen.update()

        def new_text(self, lable, new):
            c = self.color()[0]
            self.color('white')
            self.clear()
            self.goto(80, -150)
            self.write(lable, None, 'left', ('Calabri', 10))
            self.goto(50, -138)
            self.color(c)



    def toggle_music(core):
        core.stt = open("musicon.txt", 'w')
        
        
        if bool(core.current_setting):
            core.current_setting = 0
            core.stt.write('0')
            core.stt.close()
            core.new_text("Turn Music On", 0)
            sm.nosound()
            return 'gray'
        else:
            core.current_setting = 1
            core.stt.write('1')
            core.stt.close()
            core.new_text("Turn Music Off", 1)
            sm.submenu_music(True)
            return 'white'
        


    instructions = instructions()

    for x in different_key_uses:
        x.onclick(x.select)
        x.onclick(x.default_key, 3)
        x.onrelease(x.defaul_unselect, 3)
        
    sett = sound_setting(toggle_music)

        
    different_key_uses[0].select()


    for x in keys_:
        screen.onkey(keys_n_functs[x], x)






    screen.update()
    screen.listen()




