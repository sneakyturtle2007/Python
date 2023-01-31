#all imports 4
import turtle as turtle
import random 
from random import randint
# variables & objects
maze = turtle.Turtle()
dist = 40
path_width = 20
door_checker = path_width *2
dist_counter = 0
wn = turtle.Screen()
maze.speed(0)
#functions
def draw_door(rand_barrier, rand_door):
    global dist_counter
    while(dist_counter < rand_door):
        maze.forward(1)
        dist_counter += 1
    maze.penup()
    maze.forward(20)
    dist_counter += 20
    maze.pendown()
    if(rand_barrier < (rand_door + 20)):
        maze.right(90)
        maze.forward(20)
        maze.right(180)
        maze.forward(20)
        maze.right(90)
    else:
        while(dist_counter < rand_barrier):
            dist_counter += 1
            maze.forward(1)
        maze.right(90)
        maze.forward(20)
        maze.right(180)
        maze.forward(20)
        maze.right(90) 
    while(dist_counter < dist):
        
        maze.forward(1)
        dist_counter += 1                                            
def draw_barrier(rand_barrier, rand_door):
    global dist_counter
    while(dist_counter < rand_barrier):
        
        maze.forward(1)
        dist_counter += 1
    maze.right(90)
    maze.forward(20)
    maze.right(180)
    maze.forward(20)
    maze.right(90)
    while(dist_counter < rand_door):
        
        maze.forward(1)
        dist_counter += 1 
    maze.penup()
    maze.forward(20)
    dist_counter += 20
    maze.pendown()
    while(dist_counter < dist):
        
        maze.forward(1)
        dist_counter += 1
# program
for i in range(5):
    for x in range(5):
        
        dist_counter = 0
        rand_door = random.randint(0,(dist -door_checker))
        rand_barrier = random.randint(20,(dist-20))
        maze.left(90)
        if(rand_door < rand_barrier):
            draw_door(rand_barrier, rand_door)
        else:
            draw_barrier(rand_barrier, rand_door)
       
        dist += 10
maze.ht()
            
wn.listen()

wn.mainloop()            
        