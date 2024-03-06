#import class
import ursina
from ursina import *
import random
from aStar import astar
from aStar import astar, update_enemy_position


# Run main.py code here


class Background(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        # Other initialization code...
        self.player_position = (4, 0)  # Assuming player's initial position
        
        # Create enemy instance
        self.enemy = DupEnemy()
        
    def update(self):
        # Update enemy's position based on player's position
        update_enemy_position(self.enemy, self.player_position)


       

                       
class Player(Entity):
    def __init__(self):
          super().__init__() 
          self.score=0
          self.model="../Assets/IMG/paperplane.obj"
          self.scale=(5, 5)
          self. texture="../Assets/IMG/26140.jpg"
          self.position=(4,0,-10)
          self.speed = .1
          self.collider="box"
          self.score=0
         # self.score_text = Text(text='POINTS: 0', y=0, x=0, origin=(4,-17),scale=(1,1),font='../Assets/font/space_age.ttf',color=color.green)
          
          
    def update(self):
        #move pane
            if held_keys['w']:
                self.y += self.speed

            if held_keys['s']:
               self.y -= self.speed 

            if held_keys['a']:
                self.x -= self.speed
            if held_keys['d']:
                self.x += self.speed
                self.rotation_y -= .05
        #keep plane in window
            if self.x > 6.5:
                self.x =6.5
            if self.x < 1:
                self.x = 1
            if self.y > 1.5:
                self.y = 1.5
            if self.y < -1.5:
                self.y = -1.5
        
            hit_info=self.intersects()#check if plane is getting 
            if hit_info.hit:
                Text(text = 'GAME OVER', y=0, x=0, origin=(0,0),scale=(3,2),font='../Assets/font/SPACEBOY.TTF',color=color.red)
                Text(text='POINTS: {}'.format(self.score) , y=0, x=0, origin=(0,2),scale=(1,1),font='../Assets/font/SPACEBOY.TTF',color=color.green)
                destroy(self)
            else:
                self.score += 1 # increase the score if there is no collision
               # self.score_text.text = 'POINTS: {}'.format(self.score) 


            
class DupEnemy(Entity):
    def __init__(self):
        super().__init__() 
        
        self.model="../Assets/IMG/rock.obj"
        self.scale=(0.5,0.5,0.5)
        self. texture="../Assets/IMG/dumpTexture.jpg"
        self.z=110
        #self.position=(0,0,0)
        self.speed =1
        self.timer = random.uniform(0, 10)
        self.collider="box"
    
    
    
    def update(self):
        self.timer -= time.dt
        if self.timer <= 0:
            rotation_speed = math.radians(10)
            self.z -= self.speed
            self.rotation_z += rotation_speed
            self.rotation_x += rotation_speed
            self.rotation_y += rotation_speed
            if(self.z<=-22):
                self.z=110
                self.timer = random.uniform(0, 15)
                self.x = random.uniform(-6, 6)
                self.y = random.uniform(-1.5, 1.5)
            
            

        

                
