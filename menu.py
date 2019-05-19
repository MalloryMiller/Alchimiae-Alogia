import menu_graphics as mg
import sound_management as sm
import character_select as cs
import credit as c








def menu_page():
    from settings import full_settings_page as s
    sm.menu_music()

    opts = [
        
        [
            ['Play', cs.select_character_page],
            [0, 0]
            
            ], 
        
        [
            ['Settings', s],
            [0, -70]
            
            ],
        [
            ['Credits', c.credits_page],
            [0, -140]
            
            ]

        ]

    
    mg.screen.clear()
    mg.screen.bgpic('title_screen.gif')
    mg.screen.tracer(1000000, 1000000)
    

    battle_keys_file = open('key_settings.txt', 'r')
    list_keys = battle_keys_file.readlines()

    key_left_option = list_keys[0]
    key_right_option = list_keys[1]
    key_choose_option = list_keys[2]
    key_restart = list_keys[3]
    key_menu = list_keys[4]
    key_next_tut_p = list_keys[5]
    key_skip_tut = list_keys[6]
    key_confirm_exit_tomenu = list_keys[7]
    key_deny_exit_tomenu = list_keys[8]
    key_up_option = list_keys[9]
    key_down_option = list_keys[10]

    battle_keys_file.close()

    instructions = mg.key_instructions(key_up_option,
                                       key_down_option,
                                       key_choose_option)

    
    opt_coords = []
    
    for selection in opts:
        mg.menu_lables(selection[0][0], selection[1])

    select_arrow = mg.selection_cursor(opts)

    def select_menu_option():
        opts[select_arrow.choice][0][1]()

    mg.turtle.onkey(select_arrow.change_up, key_up_option)
    mg.turtle.onkey(select_arrow.change_down, key_down_option)
    mg.turtle.onkey(select_menu_option, key_choose_option)
    
    mg.screen.update()

    mg.turtle.listen()

    


