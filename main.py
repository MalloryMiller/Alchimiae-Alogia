import turtle
import battle_graphics as g
import player_types as pt

g.screen.tracer(1000, 1000)
g.screen.bgcolor(0, 0, 0)




battle_keys_file = open('key_settings.txt', 'r')
list_keys = battle_keys_file.readlines()

key_left_option = list_keys[0]
key_right_option = list_keys[1]
key_choose_option = list_keys[2]
key_restart = list_keys[3]
key_menue = list_keys[4]




def mainscreen():
    pass

def settingscreen():
    pass

def default_keys():
    pass


def pve():

    g.screen.clear()
    g.screen.bgpic(g.bckgrd_stage)
    g.screen.tracer(1000, 1000)


    
    possible_players = [
    
        pt.Alchemist,
        pt.AzureArcher,
        pt.IncendiaryWarrior,
        pt.StarryKnight

        ]


    random_player = pt.r.randint(0, 3)
    random_enemy = pt.r.randint(0, 2)



    player = possible_players.pop(random_player)\
             (pt.player_names[random_player][pt.r.randint(0, 3)],
              False)                # player, not enemy

    enemy = possible_players.pop(random_enemy)\
            (pt.enemy_names[random_enemy][pt.r.randint(0, 3)],
             True)                  # enemy, not player



    action_ordered = [

        player.act1,
        player.act2,
        player.act3,
        player.act4

        ]





    actions = g.GroupOf4Buttons(player.actNames, pt.stamina_cutoffs)



    def enemys_turn():
        enemy.begin_turn()

        if enemy.health <= 0:
            return True


        if enemy.health < pt.r.randint(15, 50):
            enemy.act4(player)
        elif enemy.stamina > 15:
            enemy.act3(player)
        else:
            rand = pt.r.randint(0, 1)

            if rand == 0:
                enemy.act2(player)
            else:
                enemy.act1(player)





        player.begin_turn()



    def nullkeys():
        for b in actions.buttons:
            b.option_selected(player.stamina)
            

        turtle.onkey(pve, key_menue)
        turtle.onkey(None, key_left_option)
        turtle.onkey(None, key_right_option)
        turtle.onkey(None, key_choose_option)
        turtle.onkey(None, key_restart)
        actions.ht()
        g.screen.update()


    def castBattlekeys():
        for b in actions.buttons:
            b.option_selected(player.stamina)
            

        turtle.onkey(pve, key_menue)
        turtle.onkey(left, key_left_option)
        turtle.onkey(right, key_right_option)
        turtle.onkey(enter, key_choose_option)
        turtle.onkey(None, key_restart)
        actions.st()
        g.screen.update()

    def castEndscreenkeys():
        turtle.onkey(pve, key_menue)
        turtle.onkey(None, key_left_option)
        turtle.onkey(None, key_right_option)
        turtle.onkey(None, key_choose_option)
        turtle.onkey(pve, key_restart)





    def left():
        actions.select_button(-1)
        g.screen.update()

    def right():
        actions.select_button(1)
        g.screen.update()

    def enter():
        nullkeys()

        if action_ordered[actions.select_opt](enemy):
            castEndscreenkeys()
            return

        if enemys_turn():
            castEndscreenkeys()
            return
        castBattlekeys()


    castBattlekeys()
    g.screen.update()

    turtle.listen()




pve()
g.screen.mainloop()
