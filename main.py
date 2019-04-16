import turtle
import graphics as g
import player_types as pt


def main():
    
    random_player = 0 #pt.r(0, 3)
    random_enemy = 0 #pt.r(0, 3)


    player = pt.player_types[random_player](pt.player_names[random_player][pt.r.randint(0, 3)], False)
    print(player)

    enemy = pt.player_types[random_enemy](pt.enemy_names[random_enemy][pt.r.randint(0, 3)], True)
    print(enemy, '\n')



    action_ordered = [
        
        player.act1,
        player.act2,
        player.act3,
        player.act4
        
        ]




    actions = g.GroupOf4Buttons(player.actNames)

    def left():
        actions.select_button(-1)
        g.screen.update()

    def right():
        actions.select_button(1)
        g.screen.update()

    def enter():
        action_ordered[actions.select_opt](enemy)
        print("\n")
        

    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkey(enter, "Return")
    g.screen.update()
    turtle.listen()


main()
