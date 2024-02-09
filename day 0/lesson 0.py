from turtle import *


#we want to paint a house 

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left (90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing the door

forward(70)
left(90)

forward(100) #height of door

right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200,200)
pendown()

#end of the door


#start of the roof

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#end of the roof


#start of the windows

penup()
goto(20,125)
pendown()

left(210)
forward(50)
right(90)
forward(50)
left(270)
forward(50)

right(90)
forward(50)

penup()
goto(125,125)
pendown()

left(180)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)


exitonclick()