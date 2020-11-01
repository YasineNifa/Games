import turtle






class Ball():
	def __init__(self,pos=(0,0)):
		self.pos = pos
		self.ball = turtle.Turtle()
		self.ball.speed(0)
		self.ball.shape("square")
		self.ball.color("white")
		self.ball.penup()
		self.ball.goto(0,0)
		self.dx = 0.07
		self.dy = -0.07

	

	def getx(self):
		return self.ball.xcor()
	def gety(self):
		return self.ball.ycor()

	def setx(self, value):
		return self.ball.setx(value)
	def sety(self, value):
		return self.ball.sety(value)

	def reset(self):
		self.ball.goto(0,0)




class Paddle():
	def __init__(self,pos):
		self.pos = pos
		self.paddle = turtle.Turtle()
		self.paddle.speed(0)
		self.paddle.shape("square")
		self.paddle.color("white")
		self.paddle.shapesize(stretch_wid=5, stretch_len=1)
		self.paddle.penup()
		self.paddle.goto(self.pos[0],self.pos[1])


	def getx(self):
		return self.paddle.xcor()
	def gety(self):
		return self.paddle.ycor()

	def setx(self, value):
		return self.paddle.setx(value)
	def sety(self, value):
		return self.paddle.sety(value)


	def paddle_up(self):
		y = self.gety()
		y += 20
		self.sety(y)

	def paddle_down(self):
		y = self.gety()
		y -= 20
		self.sety(y)

	

	


def check_border(ball, paddle_a,paddle_b):
	global score_a,score_b
	if ball.gety() > 290:
		ball.sety(290)
		ball.dy *= -1


	if ball.gety() < -290:
		ball.sety(-290)
		ball.dy *= -1


	if ball.getx() > 390:
		ball.reset()
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A : {} - Player B : {}".format(score_a,score_b), align = "center", font=("Courier",12,"normal"))


	if ball.getx() < -390:
		ball.reset()
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A : {} - Player B : {}".format(score_a,score_b), align = "center", font=("Courier",12,"normal"))
	


	if ball.getx() > 330 and (ball.gety() < paddle_b.gety() + 40 and ball.gety() > paddle_b.gety() - 40):
		ball.dx *= -1
	

	if ball.getx() < -330 and (ball.gety() < paddle_a.gety() + 40 and ball.gety() > paddle_a.gety() - 40):
		ball.dx *= -1




if __name__ == "__main__":
	score_a = 0
	score_b = 0

	wn = turtle.Screen()
	wn.title("Pong By YassineNifa")
	wn.bgcolor("black")
	wn.setup(width=800,height=600)
	wn.tracer(0)

	# Pen
	pen = turtle.Turtle()
	pen.speed(0)
	pen.color("white")
	pen.penup() 
	pen.hideturtle()
	pen.goto(0,260)
	pen.write("Player A : 0 - Player B : 0", align = "center", font=("Courier",12,"normal"))

	paddle_b = Paddle((350,0))
	paddle_a = Paddle((-350,0))
	ball = Ball()

	wn.listen()
	wn.onkeypress(paddle_a.paddle_down,"s")
	wn.onkeypress(paddle_a.paddle_up,"z")
	wn.onkeypress(paddle_b.paddle_down,"Down")
	wn.onkeypress(paddle_b.paddle_up,"Up")

	while True:
		wn.update()
		ball.setx(ball.getx() + ball.dx)
		ball.sety(ball.gety() + ball.dy)

		#Border Checking
		check_border(ball, paddle_a,paddle_b)