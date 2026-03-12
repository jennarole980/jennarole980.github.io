# Name: Jenna Rodriguez
# Date: Jan 13, 2026
# Description: This shows a sunny day with a blue sky, grass, two trees, and an orange apartment building.
from turtle import *
import turtle
# Setting up the screen
screen= turtle.Screen()
screen.bgcolor("skyblue")  # Sky color

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ---------------------------
# Variables - Defines colors and dimensions
# ---------------------------
# Store color values for different parts of the scene
ground_color = "lightgreen"
sun_color = "yellow"
tree_trunk_color = "brown"
tree_leaf_color = "green"
building_color = "orange"
window_color = "white"

tree_height = 60
num_trees = 2
num_floors = 5
windows_per_floor = 3

# ---------------------------
# Draw Ground - Creates a green rectangle for the ground
# ---------------------------
# Draws a filled rectangle at the bottom of the scene
t.penup()
t.goto(-270, -150)
t.pendown()
t.color(ground_color)
t.begin_fill()

for i in range(2):
    t.forward(370)
    t.left(90)
    t.forward(200)
    t.left(90)

t.end_fill()

# ---------------------------
# Draw Sun - Creates a yellow circle in the sky
# ---------------------------
# Draws a filled yellow circle representing the sun
t.penup()
t.goto(350, 50)
t.pendown()
t.color(sun_color)
t.begin_fill()
t.circle(60)
t.end_fill()

# ---------------------------
# Draw Clouds - Creates white fluffy clouds in the sky
# ---------------------------
# Each cloud is made of white circles
# Cloud 1
t.penup()
t.goto(-200, 200)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(-170, 210)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-140, 200)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# Cloud 2
t.penup()
t.goto(100, 220)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(130, 228)
t.pendown()
t.begin_fill()
t.circle(28)
t.end_fill()

t.penup()
t.goto(160, 220)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# ---------------------------
# Draw Trees - Uses a loop to create multiple trees
# ---------------------------
# For each tree: draws a brown trunk and green circular leaves
# Trees vary in leaf size 
x_position = -250

for i in range(num_trees):

    # Draw trunk - Brown rectangle that forms the base of the tree
    t.penup()
    t.goto(x_position, -150)
    t.pendown()
    t.color(tree_trunk_color)
    t.begin_fill()

    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(tree_height)
        t.left(90)

    t.end_fill()

    # Draw leaves - Green circle positioned on top of the trunk
    t.penup()
    t.goto(x_position + 10, -150 + tree_height)
    t.pendown()
    t.color(tree_leaf_color)

    if i % 2 == 0:
        leaf_size = 30  # Smaller leaves for trees at even positions
    else:
        leaf_size = 70  # Larger leaves for trees at odd positions

    t.begin_fill()
    t.circle(leaf_size)
    t.end_fill()

    x_position = x_position + 150  # Move to next tree

# ---------------------------
# Draw Apartment Building - Creates an orange rectangular building
# ---------------------------
# Draws a filled rectangle that serves as the main building structure
t.penup()
t.goto(-50, -150)
t.pendown()
t.color(building_color)
t.begin_fill()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(num_floors * 60)
    t.left(90)

t.end_fill()

# ---------------------------
# Draw Windows - Uses nested loops to fill the building with windows
# ---------------------------
# Outer loop: iterates through each floor of the building
# Inner loop: places multiple windows on each floor
# Windows alternate between white and light blue colors by floor
for floor in range(num_floors):
    for window in range(windows_per_floor):

        t.penup()
        t.goto(-30 + window * 45, -120 + floor * 60)
        t.pendown()

        # Alternate window colors: white for even floors, light blue for odd floors
        if floor % 2 == 0:
            t.color("white")
        else:
            t.color("lightblue")

        t.begin_fill()
        for i in range(2):
            t.forward(30)
            t.left(90)
            t.forward(20)
            t.left(90)
        t.end_fill()

# ---------------------------
# Display the final drawing
# ---------------------------
# Keeps the window open until the user closes it
screen.mainloop()