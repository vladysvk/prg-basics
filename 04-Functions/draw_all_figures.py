import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

figures.draw_square(100, pen)
pen.penup()
pen.goto(-100, 100)
pen.pendown()
figures.draw_square(100, pen)

pen.penup()
pen.goto(-100, 300)
pen.pendown()

figures.draw_triangle(100, pen)
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_triangle(100, pen)

pen.penup()
pen.goto(100, 300)
pen.pendown()

figures.draw_rectangle(50, 100, pen)
pen.penup()
pen.goto(50, -150)
pen.pendown()
figures.draw_rectangle(50, 100, pen)

pen.hideturtle()
window.mainloop()