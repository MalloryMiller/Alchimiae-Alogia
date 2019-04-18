import turtle
import graphics as g
import player_types as pt



def main():
    
    random_player = pt.r(0, 3)
    random_enemy = pt.r(0, 3)


    player = pt.player_types[random_player]\
             (pt.player_names[random_player][pt.r.randint(0, 3)],
              False)  # player, not enemy
    print(player)

    enemy = pt.player_types[random_enemy]\
            (pt.enemy_names[random_enemy][pt.r.randint(0, 3)],
             True)  # enemy, not player
    print(enemy, '\n')



    action_ordered = [
        
        player.act1,
        player.act2,
        player.act3,
        player.act4
        
        ]




    actions = g.GroupOf4Buttons(player.actNames)

    def enemys_turn():
        enemy.begin_turn()
        
        if enemy.health < 50:
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
        
        

    def left():
        actions.select_button(-1)
        g.screen.update()

    def right():
        actions.select_button(1)
        g.screen.update()

    def enter():
        action_ordered[actions.select_opt](enemy)
        print("\n")
        print("Enemy Health:", enemy.health)
        print("Player Health:", player.health)
        enemys_turn()
        print("Enemy Health:", enemy.health)
        print("Player Health:", player.health)
        

    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkey(enter, "Return")
    g.screen.update()
    turtle.listen()
    g.screen.mainloop()



main()
