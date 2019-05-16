import winsound


def nosound():
    winsound.PlaySound(None, winsound.SND_PURGE)


def yessound_bkgrd(sound):
    winsound.PlaySound(sound + '.wav',
                       winsound.SND_LOOP + winsound.SND_ASYNC)



    
def idle_music():
    nosound()
    yessound_bkgrd('char_select_song')

    
def battle_music():
    nosound()
    yessound_bkgrd('battle_song')

    
def end_screen_music(player_win):
    nosound()
    if player_win:
        yessound_bkgrd('endscreen_song_won')
        
    else:
        yessound_bkgrd('endscreen_song_lost')
        

def menu_music():
    nosound()
    yessound_bkgrd('main_menu_song')

    
def submenu_music():
    nosound()
    yessound_bkgrd('submenu_song')
