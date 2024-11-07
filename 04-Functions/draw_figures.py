import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100
lenght_a = 50
lenght_b = 100
# Draw a square
figures.draw_rectangle(lenght_a, lenght_b, pen)
# Hide the turtle and finish
pen.hideturtle()
window.mainloop()