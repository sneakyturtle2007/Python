#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
from random import randint
import turtle as trtl
pencil = trtl.Turtle()
pencil.speed(0)
wn = trtl.Screen()
wn.screensize(canvwidth=250,canvheight = 250)
# Works to ocsillate between values.
odd_Or_Even = 0
# Makes the buildings a random size.
def building_Size(pencolor,location):
  size = randint(10,50)
  pencil.penup()
  pencil.setposition(location,-300)
  pencil.pendown()
  pencil.color(pencolor)
  pencil.pendown()
  pencil.forward(500)
  pencil.right(180)
  pencil.forward(1000)
  pencil.right(180)
  pencil.forward(500)
  pencil.fillcolor(pencolor)
  pencil.begin_fill()
  pencil.left(90)
  pencil.forward(size)
  pencil.right(90)
  pencil.forward(size *(3/5))
  pencil.right(90)
  pencil.forward(size)
  pencil.right(90)
  pencil.forward(size *(3/5))
  pencil.end_fill()
  pencil.right(180)
  pencil.penup()
  pencil.forward(size *(3/5))



# Places the buildings in random location while still being visible in the canvas.
def building_Placement(amount_Of_Buildings,pencolor):
  for i in range(amount_Of_Buildings):
    location = randint(-450,450)
    
    
    building_Size(pencolor,location)
    
  
amount_Of_Building = int(input("How Buildings would you like in you city?\n"))
day_Or_Night = input("Is it day or night?\n")

if(day_Or_Night == "night"):
  amount_Of_Stars = int(input("How many stars do you want in the night sky?\n"))
  wn.bgcolor(0.2,0.2,0.2)
  pencil.pencolor("white")
  building_Placement(amount_Of_Building,"grey")
 # Pen color here is white
elif (day_Or_Night == "day"):
 

 
  #Draws the city
  building_Placement(amount_Of_Building,"black")
  #draws the sun
  for i in range(35):

    pencil.penup()
    
    pencil.setposition(500+i*8,300-i*10)
    pencil.fillcolor("yellow")
    pencil.pendown()
    pencil.begin_fill()
    pencil.circle(70)
    pencil.end_fill()
    pencil.fillcolor("white")
    pencil.pencolor("white")
    pencil.begin_fill()
    pencil.circle(70)
    pencil.end_fill()
    pencil.penup()
    pencil.pencolor("black")
  for e in range(35):
    wn.bgcolor(0.2,0.2,0.2)
    pencil.penup()
    pencil.pencolor(0.2,0.2,0.2)
    pencil.setposition(500+e*8,300-e*10)
    pencil.fillcolor(0.2,0.2,0.2)
    pencil.pendown()
    pencil.begin_fill()
    pencil.circle(70)
    pencil.end_fill()
    pencil.fillcolor(0.2,0.2,0.2)
    pencil.pencolor(0.2,0.2,0.2)
    pencil.begin_fill()
    pencil.circle(70)
    pencil.end_fill()
    pencil.penup()
    pencil.pencolor(0.2,0.2,0.2)
  



wn.mainloop()
