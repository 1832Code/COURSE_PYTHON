import turtle
import random

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Creación de las tortugas
tortuga1 = turtle.Turtle()
tortuga1.shape("turtle")
tortuga1.color("red")
tortuga1.penup()
tortuga1.goto(-300, 100)

tortuga2 = turtle.Turtle()
tortuga2.shape("turtle")
tortuga2.color("blue")
tortuga2.penup()
tortuga2.goto(-300, 0)

tortuga3 = turtle.Turtle()
tortuga3.shape("turtle")
tortuga3.color("green")
tortuga3.penup()
tortuga3.goto(-300, -100)

# Función para mover las tortugas
def avanzar(tortuga):
    distancia = random.randint(1, 20)
    tortuga.forward(distancia)

# Carrera
for _ in range(150):
    avanzar(tortuga1)
    avanzar(tortuga2)
    avanzar(tortuga3)

# Determinar el ganador
ganador = max(tortuga1.xcor(), tortuga2.xcor(), tortuga3.xcor())

# Mostrar el resultado
resultado = turtle.Turtle()
resultado.penup()
resultado.hideturtle()
resultado.color("purple")
resultado.goto(0, 50)
if ganador == tortuga1.xcor():
    resultado.write("¡La tortuga roja gana!", align="center", font=("Arial", 24, "normal"))
elif ganador == tortuga2.xcor():
    resultado.write("¡La tortuga azul gana!", align="center", font=("Arial", 24, "normal"))
else:
    resultado.write("¡La tortuga verde gana!", align="center", font=("Arial", 24, "normal"))

# Cerrar ventana al hacer clic
screen.exitonclick()
