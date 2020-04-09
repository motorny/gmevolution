from Actor import Creature, Food
from Field import Field

import copy

W = 700
H = 700

field = Field(W * 0.1, H * 0.1, W * 0.9, H * 0.9)
creatures = [Creature(W * 0.5 , H * 0.5, random(0.2, 4), 10, field) for _ in range(3)]
foods = [Food(random(W * 0.1, W * 0.9), random(H * 0.1, H * 0.9)) for _ in range(50)]
field.place_food(foods)


def setup():
    size(W, H)
    frameRate(120)
            

day_step = 0

def draw():
    global day_step
    global foods
    global creatures
    day_step += 1
    
    background(255)
    field.draw()
    for food in foods:
        food.draw() 
    for cr in creatures:
        cr.step()
        cr.draw()
    

    if day_step == 1000:
        day_step = 0
        creatures = filter(lambda x : x.survive(), creatures)
        new_creatures = []
        print("Survived {} creatures".format(len(creatures)))
        for cr in creatures:
            if cr.pie >= 2:
                copied = copy.copy(cr)
                if random(0.0, 4.0) < 1.0:
                    copied.vel *= random(0.8, 1.2)
                
                new_creatures.append(copied)
        print("Newly born {}".format(len(new_creatures)))
        creatures += new_creatures
        for cr in creatures:
            cr.pie = 0
            cr.steps_to_turn = 0
            cr.cur_energy = cr.max_energy
            cr.x = W / 2.0
            cr.y = H / 2.0
        foods = [Food(random(W * 0.1, W * 0.9), random(H * 0.1, H * 0.9)) for _ in range(50)]
        field.place_food(foods)
        
