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
	# score
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









# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350,0)
# # Paddle B

# paddle_b = turtle.Turtle()
# paddle_b.speed(0)
# paddle_b.shape("square")
# paddle_b.color("white")
# paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# paddle_b.penup()
# paddle_b.goto(350,0)


# #Ball
# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape("square")
# ball.color("white")
# ball.penup()
# ball.goto(0,0)
# ball.dx = 0.07
# ball.dy = -0.07


# #function

# def paddle_a_up():
# 	y = paddle_a.ycor()
# 	#20 pixel
# 	y += 20
# 	paddle_a.sety(y)

# def paddle_a_down():
# 	y = paddle_a.ycor()
# 	y -= 20
# 	paddle_a.sety(y)


# def paddle_b_up():
# 	y = paddle_b.ycor()
# 	y += 20
# 	paddle_b.sety(y)

# def paddle_b_down():
# 	y = paddle_b.ycor()
# 	y -= 20
# 	paddle_b.sety(y)





# # score
# score_a = 0
# score_b = 0


# # Pen
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup() 
# pen.hideturtle()
# pen.goto(0,260)
# pen.write("Player A : 0 - Player B : 0", align = "center", font=("Courier",12,"normal"))

# # Main Loop
# while True:
# 	wn.update()
# 	ball.setx(ball.xcor() + ball.dx)
# 	ball.sety(ball.ycor() + ball.dy)

# 	#Border Checking
# 	if ball.ycor() > 290:
# 		ball.sety(290)
# 		ball.dy *= -1


# 	if ball.ycor() < -290:
# 		ball.sety(-290)
# 		ball.dy *= -1


# 	if ball.xcor() > 390:
# 		ball.goto(0,0)
# 		ball.dx *= -1
# 		score_a += 1
# 		pen.clear()
# 		pen.write("Player A : {} - Player B : {}".format(score_a,score_b), align = "center", font=("Courier",12,"normal"))


# 	if ball.xcor() < -390:
# 		ball.goto(0,0)
# 		ball.dx *= -1
# 		score_b += 1
# 		pen.clear()
# 		pen.write("Player A : {} - Player B : {}".format(score_a,score_b), align = "center", font=("Courier",12,"normal"))
	


# 	if ball.xcor() > 330 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
# 		ball.dx *= -1
	

# 	if ball.xcor() < -330 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
# 		ball.dx *= -1
		



