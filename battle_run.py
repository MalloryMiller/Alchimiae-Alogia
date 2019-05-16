

battle_keys_file = open('key_settings.txt', 'r')
list_keys = battle_keys_file.readlines()

battle_keys_file.close()


def cleansekeys():
    for k in list_keys:
        turtle.onkey(None, k)





import turtle
import battle_graphics as g
import player_types as pt
import menu as m
import sound_management as sm




g.screen.tracer(1000000, 1000000)

player_type_num = pt.r.randint(0, 3)





def pve(player_type_num, tutorial = True, list_keys = list_keys):
    sm.battle_music()

    screen_items = []

        
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

    battle_keys_file.close()

    cleansekeys()
    
    confirm_box = g.popup_confirm()
    screen_items.append(confirm_box)


    g.screen.clear()
    g.screen.bgpic(g.bckgrd_stage)
    g.screen.tracer(1000, 1000)


    
    possible_players = [
    
        pt.Alchemist,
        pt.AzureArcher,
        pt.IncendiaryWarrior,
        pt.StarryKnight

        ]




    random_enemy = pt.r.randint(0, 2)

    if random_enemy >= player_type_num:
        random_enemy_true = random_enemy + 1

    else:
        random_enemy_true = random_enemy



    player = possible_players.pop(player_type_num)\
             (pt.player_names[player_type_num][pt.r.randint(0, 3)],
              False)                # player, not enemy

    enemy = possible_players.pop(random_enemy)\
            (pt.enemy_names[random_enemy_true][pt.r.randint(0, 3)],
             True)                  # enemy, not player

    
    screen_items.append(player)
    screen_items.append(enemy)

    

    tutorial = g.tutorial_text(tutorial)
    tutorial.check_change()
    screen_items.append(tutorial)



    action_ordered = [

        player.act1,
        player.act2,
        player.act3,
        player.act4

        ]





    actions = g.GroupOf4Buttons(player.actNames, pt.stamina_cutoffs,
                                pt.multiplier)
    screen_items.append(actions)



    def enemys_turn():
        enemy.begin_turn()


        if enemy.health < pt.r.randint(enemy.full_health // 3, enemy.full_health // 2):
            enemy.act4(player)
            
        elif enemy.stamina > 12:
            if enemy.act3(player):
                return True
            
        else:
            rand = pt.r.randint(0, 1)

            if rand == 0:
                if enemy.act2(player):
                    return True
            else:
                if enemy.act1(player):
                    return True





        player.begin_turn()



    def nullkeys():
        for b in actions.buttons:
            b.option_selected(player.stamina)
            
        cleansekeys()

        turtle.onkey(confirm_exit, key_menu)
        turtle.onkey(tutorial.check_change, key_next_tut_p)
        turtle.onkey(tutorial.skip_tutorial, key_skip_tut)
        actions.ht()
        g.screen.update()


    def castBattlekeys():
        for b in actions.buttons:
            b.option_selected(player.stamina)

        cleansekeys()
        
        turtle.onkey(confirm_exit, key_menu)
        turtle.onkey(left, key_left_option)
        turtle.onkey(right, key_right_option)
        turtle.onkey(enter, key_choose_option)
        turtle.onkey(tutorial.check_change, key_next_tut_p)
        turtle.onkey(tutorial.skip_tutorial, key_skip_tut)
        actions.st()
        g.screen.update()


    def castEndscreenkeys(player_win):            
        tutorial.skip_tutorial()
        sm.end_screen_music(player_win)
        cleansekeys()
        
        turtle.onkey(m.menu_page, key_menu)
        turtle.onkey(pve_notut, key_restart)
        
        for b in actions.buttons:
            b.clear()
            




    def confirm_exit(confirm_box = confirm_box):
        cleansekeys()
        
        
        if not confirm_box.open:
            confirm_box.opening()

            turtle.onkey(exit_to_menu, key_confirm_exit_tomenu) 
            turtle.onkey(not_closing, key_deny_exit_tomenu)
            
        else:
            pass

    def exit_to_menu():
        for b in actions.buttons:
            b.clear()
            
        g.screen.reset()
        g.screen.clear()

        m.menu_page()



    def not_closing():
        confirm_box.closing()
        castBattlekeys()



    def pve_notut():
        pve(player_type_num, False)



    def left():
        actions.select_button(-1)
        g.screen.update()

    def right():
        actions.select_button(1)
        g.screen.update()

    def enter():
        nullkeys()

        if action_ordered[actions.select_opt](enemy):
            castEndscreenkeys(True)
            return

        elif enemys_turn():
            castEndscreenkeys(False)
            return
        
        castBattlekeys()


    castBattlekeys()
    g.screen.update()

    turtle.listen()





