from Actor import Creature, Food
from Field import Field

W = 500
H = 500

field = Field(W * 0.1, H * 0.1, W * 0.9, H * 0.9)
creatures = [Creature(W * 0.5 , H * 0.5, random(0.5, 2.5), field) for _ in range(10)]
foods = [Food(random(W * 0.1, W * 0.9), random(H * 0.1, H * 0.9)) for _ in range(30)]
field.place_food(foods)


def setup():
    size(W, H)
    frameRate(120)

def draw():
    background(255)
    field.draw()
    for food in foods:
        food.draw() 
    for cr in creatures:
        cr.step()
        cr.draw()

    
