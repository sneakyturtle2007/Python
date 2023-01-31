#imports
import turtle
# variables, objects, and object setup
red = 1,0.15,0.2
yellow = 1,1,0.47
green = 0.47,1,0.47
blue = 0.28,0.66,0.98
background_colors = [red, yellow, green, blue]
player_height_base = -25
player_height_max = 100
height = -30
height_counter = 1
increment = 1
barrier_x = 485
player_points = 0 
player_on = 0.0
dead_point = 0
repetition_of_player_point = 0
player_shape = "dinosaur.gif"
font_setup = ("Arial", 30, "normal")
font_setup1 = ("Arial", 11, "normal")
wn = turtle.Screen() 
player = turtle.Turtle()
floor = turtle.Turtle()
barrier = turtle.Turtle()
jump_Botton = turtle.Turtle()
point_writer = turtle.Turtle()
color_choice_red = turtle.Turtle()
color_choice_green = turtle.Turtle()
color_choice_yellow = turtle.Turtle()
color_choice_blue = turtle.Turtle()
player.ht()
floor.ht()
barrier.ht()
jump_Botton.ht()
point_writer.ht()
wn.addshape(player_shape) # Make the screen aware of the new file
floor.shape("square")
barrier.shape("square")
jump_Botton.shape("square")
color_choice_red.shape("square")
color_choice_green.shape("square")
color_choice_yellow.shape("square")
color_choice_blue.shape("square")
floor.shapesize(1,100)
barrier.shapesize(2,1)
jump_Botton.shapesize(1.5,2.5)
color_choice_red.shapesize(1.5,2.5)
color_choice_green.shapesize(1.5,2.5)
color_choice_yellow.shapesize(1.5,2.5)
color_choice_blue.shapesize(1.5,2.5)
point_writer.penup()
floor.penup()
barrier.penup()
player.penup()
jump_Botton.penup()
color_choice_red.penup()
color_choice_green.penup()
color_choice_yellow.penup()
color_choice_blue.penup()
floor.setposition(0,-50)
barrier.speed(0)
point_writer.speed(0)
barrier.setposition(485,-25)
player.setposition(0,height)
jump_Botton.setposition(100,120)
point_writer.setposition(-175,100)
color_choice_red.setposition(50,50)
color_choice_green.setposition(-100,50)
color_choice_yellow.setposition(-100,-75)
color_choice_blue.setposition(50,-75)
point_writer.pendown()
point_writer.pensize(2) 
color_choice_red.color("red")
color_choice_green.color("green")
color_choice_yellow.color("yellow")
color_choice_blue.color("blue")

# functions
def draw_apple(active_apple):
  active_apple.shape(player_shape)
  wn.update()
  
def player_physics(x,y):
    global height, height_counter, player_on
    height = 0
    height_counter = 0
    player_on += 1.0
    while height >= player_height_base:
        moving_barrier()
        player.setposition(0,height)
        
        height += (20 - 2* height_counter)
        height_counter += 1
    player_on -= 1.0
    moving_barrier()
    
def moving_barrier():
    global barrier_x, increment, repetition_of_player_point
    if barrier_x > -485:
        player_collision()
        barrier.setposition(barrier_x,-25)
        if player_on == 1.0:
            barrier_x -= 4 * increment
        else:
            barrier_x -= 1.5 * increment
    else:
        if increment <= 7:
            increment += 1.2
        barrier_x = 485
        repetition_of_player_point -= 1
    if(player_on != 1.0):
        wn.ontimer(moving_barrier, 1)
        
def player_collision():
    global repetition_of_player_point, player_points, dead_point
    if(player.ycor() <= 10 and barrier_x <= 15 and barrier_x >= -15):
        floor.ht()
        barrier.ht()
        player.ht()
        point_writer.ht()
        point_writer.clear()
        jump_Botton.ht()
        dead_point += 1
    elif barrier_x < -15 and dead_point <1:
        if repetition_of_player_point < 1:
            player_points += 1
            repetition_of_player_point += 1
            point_writer.showturtle()
            point_writer.clear()
            point_writer.write("Points: " + str(player_points), font = font_setup)
            point_writer.ht()
def dinosaur_game_start():
    player.st()
    floor.st()
    barrier.st()
    jump_Botton.st()
    point_writer.st()
    point_writer.write("Points: " + str(player_points), font = font_setup)
    draw_apple(player)
    player.left(90)
    jump_Botton.onclick(player_physics)
def hide_color_turtles():
    color_choice_blue.ht()
    color_choice_green.ht()
    color_choice_red.ht()
    color_choice_yellow.ht()
def background_color_change_blue(x,y):
    wn.bgcolor(background_colors[3])
    hide_color_turtles()
    dinosaur_game_start()
def background_color_change_red(x,y):
    wn.bgcolor(background_colors[0])
    hide_color_turtles()
    dinosaur_game_start()
def background_color_change_green(x,y):
    wn.bgcolor(background_colors[2]) 
    hide_color_turtles()
    dinosaur_game_start()
def background_color_change_yellow(x,y):
    wn.bgcolor(background_colors[1])
    hide_color_turtles()
    dinosaur_game_start()
# program
color_choice_red.onclick(background_color_change_red)
color_choice_green.onclick(background_color_change_green)
color_choice_yellow.onclick(background_color_change_yellow)
color_choice_blue.onclick(background_color_change_blue)
wn.listen()
wn.mainloop()