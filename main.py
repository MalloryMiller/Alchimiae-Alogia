import turtle
import battle_graphics as g
import player_types as pt

g.screen.tracer(1000, 1000)


key_left_option = 'Left'
key_right_option = 'Right'
key_choose_option = 'Return'




def mainscreen():
    pass

def settingscreen():
    pass


def pve():

    random_player = pt.r.randint(0, 2)
    random_enemy = pt.r.randint(0, 1)

    possible_players = pt.player_types


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

        nullkeys()

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
            
        
        turtle.onkey(None, key_left_option)
        turtle.onkey(None, key_right_option)
        turtle.onkey(None, key_choose_option)
        actions.ht()
        g.screen.update()


    def castBattlekeys():
        for b in actions.buttons:
            b.option_selected(player.stamina)
            
    
        turtle.onkey(left, key_left_option)
        turtle.onkey(right, key_right_option)
        turtle.onkey(enter, key_choose_option)
        actions.st()
        g.screen.update()





    def left():
        actions.select_button(-1)
        g.screen.update()

    def right():
        actions.select_button(1)
        g.screen.update()

    def enter():
        nullkeys()

        action_ordered[actions.select_opt](enemy)

        enemys_turn()
        castBattlekeys()


    castBattlekeys()
    g.screen.update()

    turtle.listen()




pve()
g.screen.mainloop()
