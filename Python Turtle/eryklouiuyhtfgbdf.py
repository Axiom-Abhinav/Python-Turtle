import turtle

t = turtle.Turtle()

t.screen.title("Turtle Shape")
t.speed(0)

colors = ["red", "blue", "green", "orange", "purple"]

for i in range(100):
    t.color(colors[i % 5])
    t.forward(i * 3)
    t.left(59)

turtle.done()
