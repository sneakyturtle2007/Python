# all imports 2
import turtle as turtle
import random
from random import randint
# all variables and objects
dist = 50
path_width = 20
wn = turtle.Screen()
maze = turtle.Turtle()
rep_counter = 0
door_checker = path_width * 2 + 10
maze.pensize(2)

       
# all functions
def draw_door(len):
    maze.forward(len)
    maze.penup()
    maze.forward(path_width*2)
    maze.pendown()
    
def draw_barrier():
    maze.left(90)
    maze.forward(20)
    maze.left(180)
    maze.forward(20)
    maze.left(90)
    
# The program
for i in range(5):
    for x in range(5):
        
        maze.left(90)
        if(rep_counter <= 4):
            maze.penup()
           
            maze.forward(dist)
            maze.pendown()
        else:
            rand_door = random.randint(0,(dist- door_checker))
            rand_barrier = random.randint(0,(dist-door_checker))
       
           
            if(rand_door < rand_barrier):
                difference = rand_barrier - rand_door
                total = door_checker + difference + rand_door
                draw_door(rand_door)
                maze.forward(difference)
                draw_barrier()
                if(dist - total > 0):
                    maze.forward(dist - total)
            else:
                difference = rand_door- rand_barrier
                total = door_checker + difference + rand_barrier
                total_total = dist - total
                difference_and_door_checker = (difference + door_checker)
                maze.forward(rand_barrier)
                draw_barrier()
                if(dist - rand_barrier ==  difference_and_door_checker):
                    draw_door(difference)
                elif dist - rand_barrier >  difference_and_door_checker:
                    draw_door(difference)
                    dist_minus_total = dist - total
                    if( dist_minus_total> 0):
                        while dist_minus_total >= 0:
                            maze.forward(1)
                            dist_minus_total -= 1
                    
        dist += 10
        rep_counter += 1
maze.ht()
wn.listen()
wn.mainloop()