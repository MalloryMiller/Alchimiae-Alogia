#import winsound
from pygame import mixer

mixer.init()

def check_sett():
    settin = open('musicon.txt', 'r')
    seting = int(settin.readlines()[0])
    if bool(seting):
        return True
    else:
        return False






def yessound_bkgrd(sound):
    #winsound.PlaySound(sound + '.wav',
    #                   winsound.SND_LOOP + winsound.SND_ASYNC)
    mixer.music.load(sound + ".wav")
    mixer.music.play(loops=-1)
    pass

def nosound():
    #winsound.PlaySound(None, winsound.SND_PURGE)
    mixer.music.stop()
    pass


    
def idle_music():
    if check_sett():
        nosound()
        yessound_bkgrd('char_select_song')

        
def battle_music():
    if check_sett():
        nosound()
        yessound_bkgrd('battle_song')

        
def end_screen_music(player_win):
    if check_sett():
        nosound()
        if player_win:
            yessound_bkgrd('endscreen_song_won')
            
        else:
            yessound_bkgrd('endscreen_song_lost')
            

def menu_music():
    if check_sett():
        nosound()
        yessound_bkgrd('main_menu_song')

        
def submenu_music(ignore_setting = False):
    if check_sett() or ignore_setting:
        nosound()
        yessound_bkgrd('submenu_song')
