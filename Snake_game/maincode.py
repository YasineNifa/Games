import pygame

FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)


WIDTH = 500
HEIGHT = 500


START = (10,10)
END = (12,12)
SURFACE = (32,32)



background_colour = (255,255,255) # White color
(width, height) = (300, 200) # Screen size
color=(0,0,0) #For retangle


def create_cube(screen):
	rect = pygame.Rect(START,END)
	image = pygame.Surface(SURFACE)
	image.fill(WHITE)
	while True:
		clock.tick(FPS)
		move_cube(rect)
		screen.fill(BLACK)
		screen.blit(image, rect)
		pygame.display.update()  # Or pygame.display.flip()

def move_cube(rect):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				rect.move_ip(0, -2)
			elif event.key == pygame.K_s:
				rect.move_ip(0, 2)
			elif event.key == pygame.K_a:
				rect.move_ip(-2, 0)
			elif event.key == pygame.K_d:
				rect.move_ip(2, 0)

		
def drawGrid(w, rows, surface):
	sizeBtwn = w // rows

	x = 0
	y = 0
	for l in range(rows):
		print(l)
		x = x + sizeBtwn
		y = y +sizeBtwn

		pygame.draw.line(surface, (255,140,240), (x, 0),(x,w))
		pygame.draw.line(surface, (255,140,240), (0, y),(w,y))


def food_init(screen):
	rect = pygame.Rect((150,150),(175,175))
	image = pygame.Surface((25,25))
	image.fill(YELLOW)
	screen.blit(image, rect)
def snake_init(screen):
	rect = pygame.Rect((100,50),(125,75))
	image = pygame.Surface((25,25))
	image.fill(WHITE)
	screen.blit(image, rect)

def grid_init(w, rows, surface):
	sizeBtwn = w // rows
	x = 0
	y = 0
	for l in range(rows):
		print(l)
		x = x + sizeBtwn
		y = y +sizeBtwn
		pygame.draw.line(surface, (255,140,240), (x, 0),(x,w))
		pygame.draw.line(surface, (255,140,240), (0, y),(w,y))
	
def screen_init(w, rows, surface):
	grid_init(w, rows, surface)
	snake_init(screen)
	food_init(screen)

	

if __name__ == "__main__":

	successes, failures = pygame.init()
	print("{0} successes and {1} failures".format(successes, failures))


	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Snake Game')
	clock = pygame.time.Clock()
	screen.fill(BLACK)
	screen_init(WIDTH,20,screen)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
	
	
