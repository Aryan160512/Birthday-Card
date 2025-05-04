import pygame, time
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Birthday Card')

img1 = pygame.image.load('IMG1.jpg')
img2 = pygame.image.load('IMG2.jpg')
img3 = pygame.image.load('IMG3.jpg')

img1 = pygame.transform.scale(img1, (WIDTH, HEIGHT))
img2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
img3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))

while True:
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('HAPPY BIRTHDAY', True, (134, 102, 215))

    screen.fill((0, 0, 0))

    screen.blit(img1, (0, 0))
    screen.blit(text, (400, 300))
    pygame.display.update()
    time.sleep(2)

    screen.fill((134, 102, 215))

    screen.blit(img2, (0, 0))
    screen.blit(text, (400, 300))
    pygame.display.update()
    time.sleep(2)

    screen.fill((210, 162, 198))

    font = pygame.font.SysFont('Times New Roman', 20)
    text = font.render('HAPPY BIRTHDAY', True, (210, 162, 198))

    screen.blit(img3, (0, 0))
    screen.blit(text, (300, 300))
    pygame.display.update()
    time.sleep(2)