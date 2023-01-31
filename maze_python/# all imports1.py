# all imports1
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
def main():
    global dist
    for i in range(5):
        for x in range(5):
            maze.left(90)
            maze.pendown()
            
            
            draw_door_and_barrier()
            dist += 10
            
    maze.ht()
def draw_door_and_barrier():
    global dist_counter
    rand_door = random.randint(0,dist)
    rand_barrier = random.randint(0,dist)
    if(dist >= 20):
        if(rand_door < rand_barrier):
            while dist_counter <= rand_door:
                maze.forward(1)
                dist_counter += 1
            maze.penup()
            maze.forward(10)
            maze.pendown()
            maze.forward(dist - (dist_counter + 10))
            barrier_function(rand_barrier)
            maze.forward(dist - ( dist_counter + 10))
            dist_counter = 0
        else:
            barrier_function(rand_barrier)
            while dist_counter <= rand_door:
                maze.forward(1)
                dist_counter += 1
            maze.penup()
            maze.forward(10)
            maze.pendown()
            maze.forward(dist - (dist_counter + 10))
            dist_counter = 0
    else:
        maze.forward(10)
def barrier_function (rand):
    global dist_counter
    while dist_counter <= rand:
        maze.forward(1)
        dist_counter += 1
    maze.right(90)
    maze.forward(10)
    maze.left(180)
    maze.forward(10)
    maze.right(90)

    
# program
main()


wn.listen()

wn.mainloop()            

