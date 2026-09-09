import turtle

pantalla = turtle.Screen()
pantalla.title("Bandera de Colombia")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300, 150)
t.pendown()

# Amarillo
t.fillcolor("#FCD116")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

# Azul
t.goto(-300, 0)
t.fillcolor("#003893")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(75)
    t.right(90)
t.end_fill()

# Rojo
t.goto(-300, -75)
t.fillcolor("#CE1126")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(75)
    t.right(90)
t.end_fill()

t.hideturtle()
turtle.done()
