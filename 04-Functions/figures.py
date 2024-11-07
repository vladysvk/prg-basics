###
# Draw a square
#
def draw_square(length, pen):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length, pen):
    for i in range(3):
        pen.right(60)
        pen.forward(length)
        pen.right(60)

def draw_rectangle(lenght_a, lenght_b, pen):
    for i in range(2):
        pen.right(90)
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)