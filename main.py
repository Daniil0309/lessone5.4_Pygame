#Это самая база которая пригодится игры, приложения, итд.
import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Моя игра")

run = True

while run:
    for event in pygame.event.get(): #event - событие, get - получить, каждое событие сохраняется в event переменной
        if event.type == pygame.QUIT: #если тип события равен закрытию окна, крестик в окне
            run = False

    screen.fill((0, 0, 0)) #заполняем экран цветом
    pygame.display.flip() #Все изменения на экране видны благодаря этой функции, обновление экрана

pygame.quit()
