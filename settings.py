import menue_graphics as mg

def setting_page():
    
    battle_keys_file = open('key_settings.txt', 'w+')
    list_keys = battle_keys_file.readlines()

    def default_keys(battle_keys_file = battle_keys_file):
        battle_keys_file.write(\
            'Left\n\
Right\n\
Return\n\
r\n\
Escape\n\
space\n\
x\n\
y\n\
n\n\
Up\n\
Down')


    
    
