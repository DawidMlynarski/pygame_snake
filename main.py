import pygame, sys, random
from pygame.math import Vector2

class snake_class:
    def __init__(self) -> None:
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            # create a rect and draw
            snake_rect = pygame.Rect(block.x*cell_size, block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(250,70,70),snake_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True

class fruit_class:
    def __init__(self) -> None:
        # create an x and y pos
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        # draw a rect
        
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        

class main_class:
    def __init__(self) -> None:
        self.snake = snake_class()
        self.fruit = fruit_class()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            
            # adding block to a snake
            self.snake.add_block()
        

# Initializing pygame and window
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number * cell_size))

# Setting up clock object
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = main_class()

while True:
    # Drawing all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()

    # Setting up maximum fps
    clock.tick(60)