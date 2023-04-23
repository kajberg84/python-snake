import pygame

# Define the Snake class
class Snake:
  
    def __init__(self, color, speed, length):
      self._color = color
      self._speed = speed
      self._length = length
      self.body = []
    def move(self,pressed_key):
      x_move = 0
      y_move = 0

      if pressed_key == pygame.K_LEFT:
        x_move = -10
        y_move = 0
      elif pressed_key == pygame.K_RIGHT:
        x_move = 10
        y_move = 0
      elif pressed_key == pygame.K_UP:
        x_move = 0
        y_move = -10
      elif pressed_key == pygame.K_DOWN:
        x_move = 0
        y_move = 10
      return(x_move,y_move)

    @property
    def color(self):
      return self._color

    @color.setter
    def speed(self, value):
      self._color = value

    @property
    def speed(self):
      return self._speed

    @speed.setter
    def speed(self, value):
      self._speed = value

    @property
    def length(self):
      return self._length

    @length.setter
    def length(self, value):
      self._length = value

    def snake_head_coord(self, x_coord, y_coord):
      temp_list = []
      temp_list.append(x_coord)
      temp_list.append(y_coord)
      return temp_list
    
    def snake_body(self, x_coord, y_coord):
      temp_list = []
      temp_list.append(x_coord)
      temp_list.append(y_coord)
      self.body.append(temp_list)
      return self.body
