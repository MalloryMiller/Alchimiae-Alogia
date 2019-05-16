import turtle
import battle_run as br
import menu as m

screen = turtle.Screen()


choose_alchem = "character_select_alchemist.gif"
choose_archer = "character_select_archer.gif"
choose_warrior = "character_select_warrior.gif"
choose_knight = "character_select_knight.gif"

screens = [choose_alchem, choose_archer, choose_warrior, choose_knight]

screen_text_color = {choose_alchem: 'black', choose_archer: 'black',
                     choose_warrior: 'white', choose_knight: 'white'}


class char_selection_screen(turtle.Turtle):
    def __init__(self, image_list):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(-290, -273)
        self.chosen_char = 0
        self.txt_color = screen_text_color[screens[self.chosen_char]]

        
        battle_keys_file = open('key_settings.txt', 'r')
        list_keys = battle_keys_file.readlines()
        
        self.left = list_keys[0].split('\n')[0]
        self.right = list_keys[1].split('\n')[0]
        self.enter = list_keys[2].split('\n')[0]

        battle_keys_file.close()

        
        
        self.color(self.txt_color)
        self.write("Use the " + self.left + " and " + self.right +
                   " keys to change character selection, and " + self.enter +
                   " to choose an option.", False,
                   'left', ("Calabri", 10, 'italic'))

    def text_instructions(self):
        self.clear()
        self.txt_color = screen_text_color[screens[self.chosen_char]]
        self.color(self.txt_color)
        self.write("Use the " + self.left + " and " + self.right +
                   " keys to change character selection, and " + self.enter +
                   " to choose an option.", False,
                   'left', ("Calabri", 10, 'italic'))


    

def select_character_page():
    screen.tracer(1000000, 1000000)
    
    screen.reset()
    screen.clear()

    br.cleansekeys()
        
    battle_keys_file = open('key_settings.txt', 'r')
    list_keys = battle_keys_file.readlines()

    key_left_option = list_keys[0]
    key_right_option = list_keys[1]
    key_choose_option = list_keys[2]
    key_leave_to_menu = list_keys[4]

    battle_keys_file.close()

    

    char_screen = char_selection_screen(screens)
    
    screen.bgpic(screens[char_screen.chosen_char])

    
    def next_char(char_screen = char_screen):
        
        if char_screen.chosen_char == len(screens) - 1:
            char_screen.chosen_char = 0
            
        else:
            char_screen.chosen_char += 1

   
        screen.bgpic(screens[char_screen.chosen_char])
        char_screen.text_instructions()



    def last_char(char_screen = char_screen):
        
        if char_screen.chosen_char == 0:
            char_screen.chosen_char = len(screens) - 1
            
        else:
            char_screen.chosen_char -= 1
            
        screen.bgpic(screens[char_screen.chosen_char])
        char_screen.text_instructions()



    def choose_char(char_screen = char_screen):
        br.pve(char_screen.chosen_char, True)

    turtle.onkey(last_char, key_left_option)
    turtle.onkey(next_char, key_right_option)
    turtle.onkey(choose_char, key_choose_option)
    turtle.onkey(m.menu_page, key_leave_to_menu)

    turtle.listen()

