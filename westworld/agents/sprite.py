"""Experimental class to enhance pygame sprite capabilities
To be used to override grid agents in more general environments
To simply use circle and mask colliders in particular
Group gestion seems interesting as well

References for beginners: 
- Collisions in French https://openclassrooms.com/forum/sujet/pygame-gestion-mask-de-collision
- Nice tutorials in French https://riptutorial.com/fr/pygame/example/23787/les-surfaces
- Official documentation https://www.pygame.org/docs/ref/sprite.html
- Video on pixel perfect collision https://www.youtube.com/watch?v=Idu8XfwKUao
- Pygame Platformer Part 17: Using Collision Masks https://www.youtube.com/watch?v=Dspz3kaTKUg&t=44s
- https://kidscancode.org/blog/2016/08/pygame_1-2_working-with-sprites/
- https://fr.wikibooks.org/wiki/Pygame/Introduction_au_module_Sprite


- Convert transforms to pygame
- Convert_alpha transforms and keeps transparency
- 


"""
import pygame
from pygame.sprite import Sprite
from PIL import Image
from .base_object import BaseObject





class BaseSprite(BaseObject):
    def __init__(self,x = 0,y = 0,filepath = None,width = None,transparency = (0,0,0),init_window = False):

        super().__init__()

        self.sprite = pygame.sprite.Sprite()

        if init_window:
            pygame.init()
            shape = Image.open(filepath).size
            window = pygame.display.set_mode(shape)

        
        # Convert alpha instead of convert with transparent pictures
        self.sprite.image = pygame.image.load(filepath).convert() 
        self.sprite.image.set_colorkey(transparency)
        
        # Rescale
        self.rescale(width = width)
        
        # Prepare mask and rect
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)


    @property
    def x(self):
        return self.sprite.rect.x

    @property
    def y(self):
        return self.sprite.rect.y
        
    @property
    def pos(self):
        return self.x,self.y
    
    def rescale(self,width = None):
        if width is not None:
            w,h = self.get_size()
            self.sprite.image = pygame.transform.scale(self.sprite.image, (width,int(h*width/w)))
   
    
    def render(self,screen):
        screen.blit(self.sprite.image,self.pos)
        
        
    def get_size(self):
        return self.sprite.image.get_size()

                                         
                                         