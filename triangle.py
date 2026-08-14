import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()

t.screen.title("Triangle")
t.screen.bgcolor("black")
t.speed(0)

colors = ["red","yellow"]#,"orange","green","blue","indigo","violet"]

for i in range(100):
    t.color(colors[i % 2])
    t.forward(i * 2)
    t.left(100)

    t1.color(colors[i % 2])
    t1.forward(i * 2)
    t1.right(100)

turtle.done()