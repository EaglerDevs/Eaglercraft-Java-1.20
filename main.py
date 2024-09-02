from tkinter import *
from time import sleep
import webbrowser


root = Tk()
root.title('Eaglercraft 1.20')
root.geometry('800x600')
root.resizable(False, False)


def extract_png_asset(asset_name):
    return PhotoImage(file='assets/' + asset_name + '.png')

eagicon_photo = extract_png_asset('eagicon')




titlescreen_top_photo = extract_png_asset('titlescreen_top')
login_photo = extract_png_asset('login')
download_terrian_photo = extract_png_asset('download_terrain')
original_server_photo = extract_png_asset('original_server')
titlescreen_bg_photo = extract_png_asset('titlescreen_bg')
timed_out_photo = extract_png_asset('timed_out')
back_2_titlescreen_photo = extract_png_asset('buttons/back_2_titlescreen')
cancel_photo = extract_png_asset('buttons/cancel')
done_photo = extract_png_asset('buttons/done')
done_hover_photo = extract_png_asset('buttons/hover/done')
multiplayer_photo = extract_png_asset('buttons/multiplayer')
new_world_photo = extract_png_asset('buttons/new_world')
options_photo = extract_png_asset('buttons/options')
realms_photo = extract_png_asset('buttons/realms')
singleplayer_photo = extract_png_asset('buttons/singleplayer')
entry_bar_photo = extract_png_asset('entry_bar')
dropdown_def_steve_photo = extract_png_asset('dropdown_def_steve')
dropdown_def_alex_photo = extract_png_asset('dropdown_def_alex')
dropdown_herobrine_photo = extract_png_asset('dropdown_herobrine')
dropdown_noob_photo = extract_png_asset('dropdown_noob')
def_steve_photo = extract_png_asset('def_steve')
def_alex_photo = extract_png_asset('def_alex')
noob_photo = extract_png_asset('noob')
herobrine_photo = extract_png_asset('herobrine')
def_steve_option_photo = extract_png_asset('options/def_steve')
def_alex_option_photo = extract_png_asset('options/def_alex')
herobrine_option_photo = extract_png_asset('options/herobrine')
noob_option_photo = extract_png_asset('options/noob')
more_skins_option_photo = extract_png_asset('options/more_skins')
pets_button_photo = extract_png_asset('buttons/pets')
pets_hover_button_photo = extract_png_asset('buttons/hover/pets')
login2_photo = extract_png_asset('login2')
pig_option_photo = extract_png_asset('options/pig')
athlete_steve_option_photo = extract_png_asset('options/athlete_steve')
athlete_alex_option_photo = extract_png_asset('options/athlete_alex')
developer_steve_option_photo = extract_png_asset('options/developer_steve')
developer_alex_option_photo = extract_png_asset('options/developer_alex')
prisoner_steve_option_photo = extract_png_asset('options/prisoner_steve')
prisoner_alex_option_photo = extract_png_asset('options/prisoner_alex')
tennis_steve_option_photo = extract_png_asset('options/tennis_steve')
tennis_alex_option_photo = extract_png_asset('options/tennis_alex')
tuxedo_steve_option_photo = extract_png_asset('options/tuxedo_steve')
tuxedo_alex_option_photo = extract_png_asset('options/tuxedo_alex')
slime_option_photo = extract_png_asset('options/slime')
scottish_steve_option_photo = extract_png_asset('options/scottish_steve')
scottish_alex_option_photo = extract_png_asset('options/scottish_alex')
barney_option_photo = extract_png_asset('options/barney')
boxer_steve_option_photo = extract_png_asset('options/boxer_steve')
boxer_alex_option_photo = extract_png_asset('options/boxer_alex')
cyclist_steve_option_photo = extract_png_asset('options/cyclist_steve')
cyclist_alex_option_photo = extract_png_asset('options/cyclist_alex')
more_button_photo = extract_png_asset('buttons/more')
more_hover_button_photo = extract_png_asset('buttons/hover/more')
discord_button_photo = extract_png_asset('buttons/discord')
discord_hover_button_photo = extract_png_asset('buttons/hover/discord')
blank_dirt_photo = extract_png_asset('blank_dirt')
github_fork_button_photo = extract_png_asset('buttons/github_fork')
github_fork_button_hover_photo = extract_png_asset('buttons/hover/github_fork')

root.iconphoto(False, eagicon_photo)

shown_klock_options = [False]

login_label = Label(root, image=login_photo)
login_label.place(x=0, y=0)

login_avatar = Label(root, image=def_steve_photo)
login_avatar.place(x=50, y=50)




chosen_character = ['def_steve']


def choose_character(char):
    chosen_character.clear()
    chosen_character.append(char)


class EntryBar:
    def __init__(self, x, y):
        self.entry_sprite = Label(root, image=entry_bar_photo)
        self.entry_sprite.place(x=x, y=y)
        self.x = x
        self.y = y
    def hide(self):
        self.entry_sprite.place_forget()
    def show(self):
        self.entry_sprite.place(x=self.x, y=self.y)

class KlockcraftButton:
    def __init__(self, x=0, y=0, photo=None, hover_photo=None, command_func=None):
        self.photo = photo
        self.hover_photo = hover_photo
        self.x = x
        self.y = y
        if command_func == None: self.button = Button(root, image=self.photo)
        else: self.button = Button(root, image=self.photo, command=command_func)
        self.button.place(x=x, y=y)
        self.button.bind('<Enter>', self.hover)
        self.button.bind('<Leave>', self.no_hover)
    def hover(self, _):
        if self.hover_photo != None: self.button.config(image=self.hover_photo)
    def no_hover(self, _):
        if self.hover_photo != None: self.button.config(image=self.photo)
    def change_photo(self, new_photo):
        self.button.config(image=new_photo)
    def destroy(self):
        self.button.place_forget()
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.button.place(x=new_x, y=new_y)
        self.button.update()
    def hide(self):
        self.button.place(x=1000, y=1000)
    def show(self):
        self.button.place(x=self.x, y=self.y)

def open_discord(): webbrowser.open('https://discord.gg/pKfvNxAv')
def open_github(): webbrowser.open('https://github.com/eaglerdevs/Eaglercraft-Java-1.20/fork')


def choose_def_steve(): 
    choose_character('def_steve')
    login_avatar.config(image=def_steve_photo)
    login_dropdown.change_photo(dropdown_def_steve_photo)

def choose_def_alex(): 
    choose_character('def_alex')
    login_avatar.config(image=def_alex_photo)
    login_dropdown.change_photo(dropdown_def_alex_photo)


def choose_herobrine():
    choose_character('herobrine')
    login_avatar.config(image=herobrine_photo)
    login_dropdown.change_photo(dropdown_herobrine_photo)

def choose_noob():
    choose_character('noob')
    login_avatar.config(image=noob_photo)
    login_dropdown.change_photo(dropdown_noob_photo)

def open_pets():
    def_steve_option.hide()
    def_alex_option.hide()
    herobrine_option.hide()
    noob_option.hide()
    more_skins_option.hide()
    screename_bar.hide()
    pets_button.hide()
    done_button.hide()
    login_dropdown.hide()
    login_label.place_forget()
    more_button.hide()

    login2_label = Label(root, image=login2_photo)
    login2_label.place(x=0, y=0)

    char = chosen_character[0]
    if char == 'def_steve': char = def_steve_photo
    elif char == 'def_alex': char = def_alex_photo
    elif char == 'noob': char = noob_photo
    elif char == 'herobrine': char = herobrine_photo
    login_avatar2 = Label(root, image=char)
    login_avatar2.place(x=50, y=50)


    def return_normal_login():
        more_skins_done_button.hide()
        login_avatar2.place_forget()
        login2_label.place_forget()
        def_steve_option.show()
        def_alex_option.show()
        herobrine_option.show()
        noob_option.show()
        more_skins_option.show()
        screename_bar.show()
        pets_button.show()
        done_button.show()
        login_dropdown.show()
        more_button.show()
        login_label.place(x=0, y=0)


    more_skins_done_button = KlockcraftButton(300, 550, done_photo, done_hover_photo, return_normal_login)
    

def more_skins():
    def_steve_option.hide()
    def_alex_option.hide()
    herobrine_option.hide()
    noob_option.hide()
    more_skins_option.hide()
    screename_bar.hide()
    pets_button.hide()
    done_button.hide()
    login_dropdown.hide()
    login_label.place_forget()
    more_button.hide()

    login2_label = Label(root, image=login2_photo)
    login2_label.place(x=0, y=0)

    char = chosen_character[0]
    if char == 'def_steve': char = def_steve_photo
    elif char == 'def_alex': char = def_alex_photo
    elif char == 'noob': char = noob_photo
    elif char == 'herobrine': char = herobrine_photo
    login_avatar2 = Label(root, image=char)
    login_avatar2.place(x=50, y=50)

    developer_steve_option = KlockcraftButton(300, 70, developer_steve_option_photo, None, None)
    developer_alex_option = KlockcraftButton(300, 120, developer_alex_option_photo, None, None)
    tuxedo_steve_option = KlockcraftButton(300, 170, tuxedo_steve_option_photo, None, None)
    tuxedo_alex_option = KlockcraftButton(300, 220, tuxedo_alex_option_photo, None, None)
    prisoner_steve_option = KlockcraftButton(300, 270, prisoner_steve_option_photo, None, None)
    prisoner_alex_option = KlockcraftButton(300, 320, prisoner_alex_option_photo, None, None)
    tennis_steve_option = KlockcraftButton(300, 370, tennis_steve_option_photo, None, None)
    tennis_alex_option = KlockcraftButton(300, 420, tennis_alex_option_photo, None, None)

    more_skins2_button = KlockcraftButton(300, 480, more_skins_option_photo, None, None)

    def return_normal_login():
        more_skins2_button.hide()
        tennis_alex_option.hide()
        tennis_steve_option.hide()
        prisoner_steve_option.hide()
        prisoner_alex_option.hide()
        developer_steve_option.hide()
        developer_alex_option.hide()
        tuxedo_steve_option.hide()
        tuxedo_alex_option.hide()
        more_skins_done_button.hide()
        login_avatar2.place_forget()
        login2_label.place_forget()
        def_steve_option.show()
        def_alex_option.show()
        herobrine_option.show()
        noob_option.show()
        more_skins_option.show()
        screename_bar.show()
        pets_button.show()
        done_button.show()
        login_dropdown.show()
        more_button.show()
        login_label.place(x=0, y=0)


    more_skins_done_button = KlockcraftButton(300, 550, done_photo, done_hover_photo, return_normal_login)
    if char == 'def_steve': login_avatar2.config(image=def_steve_photo)
    elif char == 'def_alex': login_avatar2.config(image=def_alex_photo)
    elif char == 'herobrine': login_avatar2.config(image=herobrine_photo)
    elif char == 'noob': login_avatar2.config(image=noob_photo)
    
def open_more():
    def_steve_option.hide()
    def_alex_option.hide()
    herobrine_option.hide()
    noob_option.hide()
    more_skins_option.hide()
    screename_bar.hide()
    pets_button.hide()
    done_button.hide()
    login_dropdown.hide()
    login_label.place_forget()
    more_button.hide()

    blank_dirt_label = Label(root, image=blank_dirt_photo)
    blank_dirt_label.place(x=0, y=0)

    discord_button = KlockcraftButton(230, 30, discord_button_photo, discord_hover_button_photo, open_discord)
    fork_github_button = KlockcraftButton(230, 80, github_fork_button_photo, github_fork_button_hover_photo, open_github)

    def return_normal_login():
        blank_dirt_label.place_forget()
        discord_button.hide()
        fork_github_button.hide()
        more_done_button.hide()
        screename_bar.show()
        pets_button.show()
        done_button.show()
        login_dropdown.show()
        more_button.show()
        login_label.place(x=0, y=0)
    

    more_done_button = KlockcraftButton(270, 550, done_photo, done_hover_photo, return_normal_login)



def_steve_option = KlockcraftButton(350, 340, def_steve_option_photo, None, choose_def_steve)
def_alex_option = KlockcraftButton(350, 370, def_alex_option_photo, None, choose_def_alex)
herobrine_option = KlockcraftButton(350, 400, herobrine_option_photo, None, choose_herobrine)
noob_option = KlockcraftButton(350, 430, noob_option_photo, None, choose_noob)
more_skins_option = KlockcraftButton(350, 460, more_skins_option_photo, None, more_skins)

def_steve_option.hide()
def_alex_option.hide()
herobrine_option.hide()
noob_option.hide()
more_skins_option.hide()

def klock_options(): 
    if shown_klock_options == [False]:
        def_steve_option.show()
        def_alex_option.show()
        herobrine_option.show()
        noob_option.show()
        more_skins_option.show()
        shown_klock_options.remove(False); shown_klock_options.append(True)
    else:
        def_steve_option.hide()
        def_alex_option.hide()
        herobrine_option.hide()
        noob_option.hide()
        more_skins_option.hide()
        shown_klock_options.remove(True); shown_klock_options.append(False)

global login_dropdown
login_dropdown = KlockcraftButton(350, 290, dropdown_def_steve_photo, None, klock_options)



screename_bar = EntryBar(350, 160)
done_button = KlockcraftButton(50, 550, done_photo, done_hover_photo)
pets_button = KlockcraftButton(400, 540, pets_button_photo, pets_hover_button_photo, open_pets)
more_button = KlockcraftButton(670, 520, more_button_photo, more_hover_button_photo, open_more)

root.mainloop()
