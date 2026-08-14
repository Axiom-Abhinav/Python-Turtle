import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()

t.screen.title("Spiral")
t.screen.bgcolor("black")
t.speed(0)
t1.speed(0)


distance = 5

colors = ["yellow","red"]
colors2 = ["purple","blue"]

for i in range(100):
     t.forward(10)
     t.color(colors2[i % 2])
     t.pensize(2)
     t.right(69)
     t.circle(69)
     # t1.forward(100)
     # t1.color(colors[i % 2])
     # t1.pensize(2)
     # t1.left(89)



turtle.done()