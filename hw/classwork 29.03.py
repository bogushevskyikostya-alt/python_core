import turtle as t

t.shape('turtle')
t.pensize(5)
t.color('red')
t.color("#2eff25")
t.color(0.1, 0.4, 0.6)
t.fillcolor((0.3,0.3,0.6))
t.speed("slowest")


screen = t.Screen()
screen. onkey(lambda: t.forward(5), "w")
screen. onkey(lambda: t.right(15), "d")
screen. onkey(lambda: t.left(15), "a")
screen.onkey(lambda: t.backward(5), "s")
screen.onclick(lambda x, y: t.goto(x, y))
screen.listen()
t.done()