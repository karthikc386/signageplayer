import pygame

class ImagePlayer:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

    def play_image(self, image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (self.screen_width, self.screen_height))
        self.screen.blit(image, (0, 0))
        pygame.display.flip()