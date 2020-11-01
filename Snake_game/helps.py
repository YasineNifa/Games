# def create_cube(screen):
# 	rect = pygame.Rect(START,END)
# 	image = pygame.Surface(SURFACE)
# 	image.fill(WHITE)
# 	while True:
# 		clock.tick(FPS)
# 		move_cube(rect)
# 		screen.fill(BLACK)
# 		screen.blit(image, rect)
# 		pygame.display.update()  # Or pygame.display.flip()



		
# def drawGrid(w, rows, surface):
# 	sizeBtwn = w // rows

# 	x = 0
# 	y = 0
# 	for l in range(rows):
# 		print(l)
# 		x = x + sizeBtwn
# 		y = y +sizeBtwn

# 		pygame.draw.line(surface, (255,140,240), (x, 0),(x,w))
# 		pygame.draw.line(surface, (255,140,240), (0, y),(w,y))


# def _food_init(screen):
# 	rect = pygame.Rect((150,150),(175,175))
# 	image = pygame.Surface((25,25))
# 	image.fill(YELLOW)
# 	screen.blit(image, rect)
# def _snake_init(screen):
# 	rect = pygame.Rect((100,50),(125,75))
# 	image = pygame.Surface((25,25))
# 	image.fill(WHITE)
# 	screen.blit(image, rect)

# def _grid_init(w, rows, surface):
# 	sizeBtwn = w // rows
# 	x = 0
# 	y = 0
# 	for l in range(rows):
# 		x = x + sizeBtwn
# 		y = y +sizeBtwn
# 		pygame.draw.line(surface, (255,140,240), (x, 0),(x,w))
# 		pygame.draw.line(surface, (255,140,240), (0, y),(w,y))
	
# def screen_init(w, rows, surface):
# 	_grid_init(w, rows, surface)
# 	_snake_init(screen)
# 	_food_init(screen)
