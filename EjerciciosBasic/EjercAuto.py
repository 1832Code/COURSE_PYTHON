import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Creación de los autos
auto_jugador1 = turtle.Turtle()
auto_jugador1.shape("square")
auto_jugador1.color("red")
auto_jugador1.shapesize(stretch_wid=1, stretch_len=2)
auto_jugador1.penup()
auto_jugador1.goto(-300, -100)

auto_jugador2 = turtle.Turtle()
auto_jugador2.shape("square")
auto_jugador2.color("blue")
auto_jugador2.shapesize(stretch_wid=1, stretch_len=2)
auto_jugador2.penup()
auto_jugador2.goto(-300, 100)

# Funciones para mover los autos del jugador 1
def mover_izquierda_jugador1():
    x = auto_jugador1.xcor()
    if x > -300:
        auto_jugador1.setx(x - 10)

def mover_derecha_jugador1():
    x = auto_jugador1.xcor()
    if x < 300:
        auto_jugador1.setx(x + 10)

# Funciones para mover los autos del jugador 2
def mover_izquierda_jugador2():
    x = auto_jugador2.xcor()
    if x > -300:
        auto_jugador2.setx(x - 10)

def mover_derecha_jugador2():
    x = auto_jugador2.xcor()
    if x < 300:
        auto_jugador2.setx(x + 10)

# Configuración del teclado
screen.listen()
screen.onkey(mover_izquierda_jugador1, "a")
screen.onkey(mover_derecha_jugador1, "d")
screen.onkey(mover_izquierda_jugador2, "Left")
screen.onkey(mover_derecha_jugador2, "Right")

# Cerrar ventana al hacer clic
screen.exitonclick()
