import menue_graphics as mg
import battle_run as b


mg.screen.tracer(1000000, 1000000)



opts = [
    
    [
        ['Play', b.pve],
        [0, 30]
        
        ], 
    
    [
        ['Settings', None],
        [0, -30]
        
        ]

    ]



def menue_page():

    

    battle_keys_file = open('key_settings.txt', 'r')
    list_keys = battle_keys_file.readlines()

    key_left_option = list_keys[0]
    key_right_option = list_keys[1]
    key_choose_option = list_keys[2]
    key_restart = list_keys[3]
    key_menue = list_keys[4]
    key_next_tut_p = list_keys[5]
    key_skip_tut = list_keys[6]
    key_confirm_exit_tomenue = list_keys[7]
    key_deny_exit_tomenue = list_keys[8]
    key_up_option = list_keys[9]
    key_down_option = list_keys[10]

    battle_keys_file.close()

    mg.screen.clear()
    mg.screen.bgcolor(.02, 0, 0)
    
    opt_coords = []
    
    for selection in opts:
        mg.menue_lables(selection[0][0], selection[1])

    select_arrow = mg.selection_cursor(opts)

    def select_menue_option():
        opts[select_arrow.choice][0][1]()

    mg.turtle.onkey(select_arrow.change_up, key_up_option)
    mg.turtle.onkey(select_arrow.change_down, key_down_option)
    mg.turtle.onkey(select_menue_option, key_choose_option)

    mg.turtle.listen()

    


