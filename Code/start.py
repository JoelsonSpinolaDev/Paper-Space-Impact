from ursina import *
from main import *



class Menu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.main_menu = Entity(parent = self, enabled = True)
        # More menus
        
        background = Entity(model='quad', texture='../Assets/IMG/bg.jpg', scale=(4, 2), parent=self.main_menu)

        
        Text(text = 'PAPER SPACE IMPACT', parent = self.main_menu, y=0.4, x=0, origin=(0,0),scale=(2,1),font='../Assets/font/SPACEBOY.TTF')

        def starting(): # Game starts
            self.main_menu.disable()
            Player()
          #  Enemy()
            Background()
            
            
        
        def quit_game():
            exit()   
        
        ButtonList(button_dict = {
            'Start':Func(starting),
            'Quit':Func(quit_game)
            
            },x=-0.5, y = 0, parent = self.main_menu,font='../Assets/font/space_age.ttf',scale=(1.5,2))


app = Ursina(fullscreen = True)
menu = Menu()
app.run()




