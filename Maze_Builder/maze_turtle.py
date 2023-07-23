#all imports 4
import turtle as turtle
import random 
from random import randint
# variables & objects
maze = turtle.Turtle()
maze_runner = turtle.Turtle()
dist = 40
path_width = 20
door_checker = path_width *2
dist_counter = 0
wn = turtle.Screen()
maze_runner.pencolor("red")
maze_runner.speed(0)
maze.speed(0)
#functions
def draw_door(rand_barrier, rand_door):
    global dist_counter
    while(dist_counter < rand_door):
        maze.forward(2)
        dist_counter += 2
    maze.penup()
    maze.forward(15)
    dist_counter += 15
    maze.pendown()
    if(rand_barrier < (rand_door + 20)):
        maze.left(90)
        maze.forward(20)
        maze.left(180)
        maze.forward(20)
        maze.left(90)
    else:
        while(dist_counter < rand_barrier):
            
            maze.forward(2)
            dist_counter += 2
        maze.left(90)
        maze.forward(20)
        maze.left(180)
        maze.forward(20)
        maze.left(90) 
    while(dist_counter < dist):
        
        maze.forward(2)
        dist_counter += 2                                           
def draw_barrier(rand_barrier, rand_door):
    global dist_counter
    while(dist_counter < rand_barrier):
        
        maze.forward(2)
        dist_counter += 2
    maze.left(90)
    maze.forward(20)
    maze.left(180)
    maze.forward(20)
    maze.left(90)
    while(dist_counter < rand_door):
        
        maze.forward(2)
        dist_counter += 2
    maze.penup()
    maze.forward(20)
    dist_counter += 20
    maze.pendown()
    while(dist_counter < dist):
        
        maze.forward(2)
        dist_counter += 2

def maze_runner_down():
    maze_runner.setheading(270)
    

def maze_runner_up():
    maze_runner.setheading(90)
    
    
def maze_runner_right():
    maze_runner.setheading(0)
    

def maze_runner_left():
    maze_runner.setheading(180)
    
    
def maze_runner_move():
    maze_runner.forward(1)
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
wn.onkeypress(maze_runner_move,"g")
wn.onkeypress(maze_runner_down,"s")

wn.onkeypress(maze_runner_up, "w")  

wn.onkeypress(maze_runner_right,"d")

wn.onkeypress(maze_runner_left,"a")

wn.listen()

wn.mainloop()            
        