import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Creación del auto controlado por el usuario
auto_usuario = turtle.Turtle()
auto_usuario.shape("square")
auto_usuario.color("red")
auto_usuario.shapesize(stretch_wid=1, stretch_len=2)
auto_usuario.penup()
auto_usuario.goto(-300, -100)

# Creación del auto controlado por la computadora
auto_computadora = turtle.Turtle()
auto_computadora.shape("square")
auto_computadora.color("blue")
auto_computadora.shapesize(stretch_wid=1, stretch_len=2)
auto_computadora.penup()
auto_computadora.goto(-300, 100)

# Funciones para mover los autos
def mover_izquierda():
    x = auto_usuario.xcor()
    if x > -300:
        auto_usuario.setx(x - 10)

def mover_derecha():
    x = auto_usuario.xcor()
    if x < 300:
        auto_usuario.setx(x + 10)

# Configuración del teclado
screen.listen()
screen.onkey(mover_izquierda, "Left")
screen.onkey(mover_derecha, "Right")

# Carr
