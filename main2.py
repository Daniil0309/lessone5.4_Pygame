# перемешение картинки при нажатии клавиш и клавиатуры
import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Моя игра")

image = pygame.image.load("png.png")
image_reck = image.get_rect()

image2 = pygame.image.load("picPython2.png.png")
image2_reck = image.get_rect()

# speed = 5

run = True

while run:
    for event in pygame.event.get(): #event - событие, get - получить, каждое событие сохраняется в event переменной
        if event.type == pygame.QUIT: #если тип события равен закрытию окна, крестик в окне
            run = False
    # keys = pygame.key.get_pressed() #получаем нажатые клавиши
    # if  keys[pygame.K_LEFT]:
    #     image_reck.x -= speed  # Перемешене с помошью клавиш влево и вправо
    # if  keys[pygame.K_RIGHT]:
    #     image_reck.x += speed
    # if  keys[pygame.K_UP]:
    #     image_reck.y -= speed
    # if  keys[pygame.K_DOWN]:
    #     image_reck.y += speed
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
        image_reck.center = (mouseX, mouseY)


    if image2_reck.colliderect(image_reck):
        print("Картинка пересеклась")
        time.sleep(1)



    screen.fill((0, 0, 0)) #заполняем экран цветом
    screen.blit(image, image_reck) #рисуем картинку на экран()
    screen.blit(image2, image2_reck)
    pygame.display.flip() #Все изменения на экране видны благодаря этой функции, обновление экрана

pygame.quit()
