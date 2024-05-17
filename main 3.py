import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800  # Ширина окна игры
SCREEN_HEIGHT = 600  # Высота окна игры
BG_COLOR = (0, 0, 0)  # Цвет фона (черный)
PADDLE_COLOR = (255, 255, 255)  # Цвет ракетки (белый)
BALL_COLOR = (255, 0, 0)  # Цвет мяча (красный)
BRICK_COLOR = (0, 255, 0)  # Цвет кирпичей (зеленый)
PADDLE_WIDTH = 100  # Ширина ракетки
PADDLE_HEIGHT = 20  # Высота ракетки
BALL_RADIUS = 10  # Радиус мяча
BRICK_WIDTH = 80  # Ширина кирпича
BRICK_HEIGHT = 30  # Высота кирпича
NUM_BRICKS_X = 10  # Количество кирпичей по горизонтали
NUM_BRICKS_Y = 5  # Количество кирпичей по вертикали

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Арканоид')


class Paddle:
    def __init__(self):
        # Создание прямоугольника ракетки
        self.rect = pygame.Rect((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2), SCREEN_HEIGHT - 40, PADDLE_WIDTH,
                                PADDLE_HEIGHT)
        self.speed = 10  # Скорость перемещения ракетки

    def move(self, direction):
        # Перемещение ракетки влево или вправо
        if direction == 'left' and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == 'right' and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        # Отрисовка ракетки на экране
        pygame.draw.rect(surface, PADDLE_COLOR, self.rect)


class Ball:
    def __init__(self):
        # Создание прямоугольника мяча
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = 5  # Горизонтальная скорость мяча
        self.dy = -5  # Вертикальная скорость мяча

    def move(self):
        # Перемещение мяча
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Отскок мяча от стенок
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top <= 0:
            self.dy = -self.dy

    def draw(self, surface):
        # Отрисовка мяча на экране
        pygame.draw.ellipse(surface, BALL_COLOR, self.rect)


class Brick:
    def __init__(self, x, y):
        # Создание прямоугольника кирпича
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, surface):
        # Отрисовка кирпича на экране
        pygame.draw.rect(surface, BRICK_COLOR, self.rect)


def create_bricks():
    # Создание списка кирпичей
    bricks = []
    for row in range(NUM_BRICKS_Y):
        for col in range(NUM_BRICKS_X):
            x = col * (BRICK_WIDTH + 10) + 35  # Вычисление позиции по X
            y = row * (BRICK_HEIGHT + 10) + 35  # Вычисление позиции по Y
            bricks.append(Brick(x, y))  # Добавление кирпича в список
    return bricks


def main():
    clock = pygame.time.Clock()  # Создание объекта для отслеживания времени
    paddle = Paddle()  # Создание ракетки
    ball = Ball()  # Создание мяча
    bricks = create_bricks()  # Создание кирпичей
    running = True  # Флаг для основного цикла игры

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move('left')
        if keys[pygame.K_RIGHT]:
            paddle.move('right')

        # Перемещение мяча
        ball.move()

        # Проверка столкновений мяча с ракеткой
        if ball.rect.colliderect(paddle.rect):
            ball.dy = -ball.dy

        # Проверка столкновений мяча с кирпичами
        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                ball.dy = -ball.dy
                bricks.remove(brick)
                break

        # Проверка проигрыша (мяч упал вниз)
        if ball.rect.bottom >= SCREEN_HEIGHT:
            running = False

        # Очистка экрана
        screen.fill(BG_COLOR)

        # Отрисовка всех игровых объектов
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Ограничение FPS до 60

    pygame.quit()  # Завершение работы Pygame
    sys.exit()  # Завершение работы программы


if __name__ == "__main__":
    main()

