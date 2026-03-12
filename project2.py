'''
Jenna Rodriguez
I made a midnight scene with a pink house with yellow windows, a door, a red roof, a tree, 2 clouds, and a moon.
'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("midnightblue")

    # Draw the ground
    jump_to(t, -400, -50)
    t.setheading(0)
    draw_rectangle(t, 800, 300, "darkgreen")            


    # Draw the moon
    jump_to(t, 200, 150)
    t.fillcolor("lightyellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Draw cloud 1 (no visible outline)
    t.penup()   
    t.pencolor("white")
    jump_to(t, -150, 100)
    draw_circle(t, 20, "white")
    jump_to(t, -130, 120)
    draw_circle(t, 25, "white")
    jump_to(t, -110, 100)
    draw_circle(t, 20, "white")
      # Draw cloud 2 (no visible outline)
    jump_to(t, -250, 130)
    draw_circle(t, 20, "white")
    jump_to(t, -230, 150)
    draw_circle(t, 25, "white")
    jump_to(t, -210, 130)
    draw_circle(t, 20, "white")
    t.pencolor("black")
    t.pendown()

    # Draw a building
    jump_to(t, -120, 0)
    t.setheading(0)
    draw_rectangle(t, 200, 120, "pink")

    # Draw a door
    jump_to(t,-30, -120)
    t.setheading(0)
    draw_rectangle(t, 30, -60,  "black")

    # Draw the roof
    jump_to(t, -130, 0)
    t.setheading(0)
    draw_triangle(t, 220, "red")

    # Draw window 1
    jump_to(t, -100, -50)
    t.setheading(0)
    draw_square(t, 40, "yellow")
 
    # Draw window 2
    jump_to(t, 20, -50)
    t.setheading(0)
    draw_square(t, 40, "yellow")
    

    # Draw a tree trunk
    jump_to(t, 150, -40)
    t.setheading(0)
    draw_rectangle(t, 30, 80, "brown")  # trunk
   
    # Draw tree top
    jump_to(t, 160, -50)
    t.setheading(0)
    draw_circle(t, 50, "darkgreen")  # top trunk        

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()