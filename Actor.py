import math

class BaseActor(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def step(self):
        pass
    
    def draw(self):
        pass
        
    
class Creature(BaseActor):
    def __init__(self, x, y, vel, field):
        super(Creature, self).__init__(x, y)
        self.vel = vel
        self.field = field
        self.vx = 0
        self.vy = 0
        self.steps_to_turn=0
        
    def draw(self):
        fill(0, 230, 20)
        circle(self.x, self.y, 20)    
        line(self.x + 10, self.y, self.x+20, self.y)
        line(self.x-10, self.y, self.x-20, self.y)
        line(self.x, self.y+10, self.x, self.y+20)
        line(self.x, self.y-10, self.x, self.y-20)
        line(self.x+6, self.y+6, self.x+16, self.y+16)
        line(self.x-6, self.y+6, self.x-16, self.y+16)
        line(self.x+6, self.y-6, self.x+16, self.y-16)
        line(self.x-6, self.y-6, self.x-16, self.y-16)
        
    def _normalize_v(self):
        cvel = math.sqrt((self.vx)**2 +(self.vy)**2)
        self.vx = self.vx / cvel * self.vel
        self.vy = self.vy / cvel * self.vel
    
    def step(self):
        self.steps_to_turn -= 1
        if self.steps_to_turn <= 0:
            angle = random(2 * PI)
            self.vx = self.vel * cos(angle)
            self.vy = self.vel * sin(angle)
            self.steps_to_turn = random(20, 100)
        
        vx, vy = self.field.check_border(self.x, self.y, self.vx, self.vy)
        self.x += vx
        self.y += vy
        
     # check food
        food, min_dist = self.field.nearest_food(self.x, self.y)
        
        if min_dist < 50 and not food.eated:
            self.steps_to_turn += int(min_dist / self.vel)
            self.vx = food.x - self.x
            self.vy = food.y - self.y
            self._normalize_v()
        
        if min_dist < 29:
            print("I am eating")
            food.eat_it()
            
            
    
class Food(BaseActor):
    def __init__(self, x, y):
        super(Food, self).__init__(x, y)
        self.eated = False
        
    def draw(self):
        if not self.eated:
          fill(230, 0, 50)
          circle(self.x, self.y, 14)
          fill(250, 250, 250)
          circle(self.x, self.y, 7)
          
    def eat_it(self):
        self.eated = True
