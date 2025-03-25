import pygame

pygame.init()

screen_x = 800
screen_y = 600

screen = pygame.display.set_mode((screen_x, screen_y))

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
			
	pygame.display.update()