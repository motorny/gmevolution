

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
        fill(230, 50, 0)
        circle(self.x, self.y, 10)
        
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
    
class Food(BaseActor):
    def __init__(self, x, y):
        super(Food, self).__init__(x, y)

    def draw(self):
        fill(0, 255, 20)
        circle(self.x, self.y, 7)
