

import numpy as np
import pygame
import itertools

from ..base_object import BaseObject
from ...colors import *



class BaseRectangle(BaseObject):

    def __init__(self,x,y,width = 1,height = 1,color = (255,0,0),circle = False):
        
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.circle = circle


    def __repr__(self):
        return f"Rectangle(x={self.x},y={self.y},w={self.width},h={self.height})"


    @property
    def value(self):
        return 1


    @property
    def pos(self):
        return self.x,self.y


    @property
    def pos_array(self):
        # TODO see if faster not as property but attribute
        xs = range(self.x,self.x + self.width)
        ys = range(self.y,self.y + self.height)

        pos = list(itertools.product(ys,xs))
        return pos


    @property
    def stationary(self):
        return True


    @property
    def blocking(self):
        return True


    @property
    def obstacle(self):
        return self.stationary and self.blocking


    @property
    def dimensions(self):
        return (
            self.x * self.box_size,
            self.y * self.box_size,
            self.width * self.box_size,
            self.height * self.box_size
        )


    @property
    def radius(self):
        assert self.width == self.height
        return int((self.width * self.box_size)/2)


    @property
    def center(self):
        radius = self.radius
        return (
            int(self.x * self.box_size + radius),
            int(self.y * self.box_size + radius),
        )

    @property
    def collider(self):
        return pygame.rect.Rect(self.dimensions)


    @property
    def sprite(self):
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.Surface(self.dimensions[-2:])
        sprite.image.set_colorkey((0,0,0))
        sprite.image.fill(self.color)
        
        # Prepare mask and rect
        sprite.rect = self.collider
        sprite.mask = pygame.mask.from_surface(sprite.image)
        return sprite

        
        

    @property
    def box_size(self):
        if hasattr(self,"_box_size"):
            return self._box_size
        else:
            raise Exception("Object must be added to an environment first to setup box size")


    def set_env(self,env):
        self._env = env

        if hasattr(env,"box_size"):
            self._box_size = env.box_size




    def get_collider(self,x,y):
        dimensions = (
            x * self.box_size,
            y * self.box_size,
            self.width * self.box_size,
            self.height * self.box_size
        )
        return pygame.rect.Rect(dimensions)


    def get_sprite(self,x,y):
        sprite = self.sprite
        sprite.rect = self.get_collider(x,y)
        return sprite




    def get_data(self):
        data = {
            "id":self.id,
            "pos":self.pos,
            "type":self.__class__.__name__
        }
        
        if hasattr(self,"attrs"):
            data = {
                **data,
                **{key:getattr(self,key) for key in self.attrs}
            }
        
        return data



    #=================================================================================
    # MOVEMENT
    #=================================================================================

    def move(self,*args,**kwargs):
        pass

    def step(self,*args,**kwargs):
        pass


    def collides_with(self,others,x = None,y = None):
        """Compute collisions between the object and any other objects
        Returns if there is a collision + the list of object ids in collision
        """

        # In the absence of external colliders
        # We take the internal collider
        if x is None and y is None:
            collider = self.collider
            sprite = self.sprite
        else:
            collider = self.get_collider(x,y)
            sprite = self.get_sprite(x,y)

        
        # If no other colliders
        if len(others) == 0:
            collisions = []

        # Compute collisions using PyGame
        else:
            other_colliders = [(other.id,other.collider) for other in others if (other.id != self.id and other.blocking)]
            if len(other_colliders) > 0:
                ids,other_colliders = list(zip(*other_colliders))
                collisions = collider.collidelistall(other_colliders)
                collisions = [ids[i] for i in collisions]
            else:
                collisions = []

        # Compute collisions with obstacle layer group using pixel perfect collision
        if self.env.has_layers:
            layer_collisions = pygame.sprite.spritecollide(sprite,self.env._obstacle_layer_group,False,pygame.sprite.collide_mask)
            if len(layer_collisions) > 0:
                collisions.append("obstacle_layer")

        # Return signal of collision and colliders touched
        if len(collisions) > 0:
            return True,collisions
        else:
            return False,collisions





    #=================================================================================
    # RENDERERS
    #=================================================================================


    def render(self,screen = None):
        """Render function to visualize object in the environment
        Visualize either a circle or square in any color
        Vision range can be visualized as well

        TODO: 
            - Improve visualization not only within PyGame
            - Visualize with Sprites as well in PyGame 
        """

        if screen is None:
            screen = self.env.screen

        if not self.circle:
            # Draw a rectangle on the grid using pygame
            pygame.draw.rect(screen,self.color,self.dimensions)

        else:

            # Draw a circle on the grid using pygame
            pygame.draw.circle(screen,self.color,self.center,self.radius)


        if hasattr(self,"vision_range") and self.vision_range is not None:
            if hasattr(self,"show_vision_range"):
                if self.show_vision_range:
                    pygame.draw.circle(screen,WHITE,self.center,int(self.vision_range * self.box_size),1)
