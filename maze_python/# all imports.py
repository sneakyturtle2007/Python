# all imports
import turtle as mazemaker
import random
from random import randint

# all variables & objects
maze = mazemaker.Turtle()
dist = 10
wn = mazemaker.Screen()
dist_counter = 0
barrier_amount = 0
barrier_range_check = 0
# functions

    
    
    
def mazemacer():
    global dist
    
    for i in range(5):
        for x in range(4):
            maze.left(90)
            maze.pendown()
            draw_door()
            dist += 10
            
def draw_barrier( rand_barrier1 ):
    global dist
    
    maze.forward(dist)
    maze.pendown()
    maze.left(180)
    maze.forward(rand_barrier1)
    maze.left(90)
    maze.forward(20)
    maze.left(180)
    maze.forward(20)
    maze.right(90)
    maze.forward(rand_barrier1+1)
    
def draw_door():
    global dist, dist_counter
    rand_door = random.randint(0,dist-10)
    door_and_barrier_chance_num = random.randint(0,100)
    door_chance = door_and_barrier_chance_num >= 25 and door_and_barrier_chance_num <= 100
    rand_barrier = random.randint(0,dist-10)
    if(rand_door < rand_barrier):
        
        while(dist_counter <= dist):
            if(dist_counter == rand_door and  door_chance == True):
                maze.penup()
                maze.forward(10)
                dist_counter += 10
                maze.pendown()
            else:
                maze.forward(1)
                dist_counter += 1 
        dist_counter = 0
        maze.penup()
        maze.left(180)
        maze.forward(dist)
        maze.left(180)
        
        rand_barrier -= (dist - rand_door)
        draw_barrier(rand_barrier)
        rand_barrier += (dist - rand_door)
    else:
        draw_barrier(rand_barrier)
        rand_door -= (dist - rand_barrier)
        maze.left(180)
        maze.forward(dist)
        maze.left(180)
        while(dist_counter <= dist):
            if(dist_counter == rand_door and  door_chance == True):
                maze.pencolor("white")
                maze.forward(10)
                dist_counter += 10
                maze.pencolor("black")
            else:
                maze.forward(1)
                dist_counter += 1 
        dist_counter = 0
        rand_door += (dist - rand_barrier)
        
        
    
        
    
# program
mazemacer()


wn.listen()

wn.mainloop()            

