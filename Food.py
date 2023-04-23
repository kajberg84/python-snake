import random
import time
# Init a class that generate a food
class Food:
  def coord_spawn(self):
      coords = (random.randint(1,63) *10 , random.randint(3, 47) * 10)
      return(coords)
    
    # return a random color. Right now white
  def color(self):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)
