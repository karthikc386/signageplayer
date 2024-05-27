import pygame
import time
import itertools

from services.ImagePlayer import ImagePlayer
from services.TextPlayer import TextPlayer
from services.VideoPlayer import VideoPlayer

from utils.DirectoryStructure import categorize_files
from utils.ScreenSize import get_screen_size

pygame.init()

screen_width, screen_height = get_screen_size()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Digital Signage Player')

content_folder = 'content'
images, texts, videos = categorize_files(content_folder)

content = itertools.cycle(images + texts + videos) 

display_time = 5
clock = pygame.time.Clock()

def main():

    running = True
    start_time = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # Get the current content
        current_content = next(content)

        # Display the content
        if current_content.endswith(('.png', '.jpg', '.jpeg')):
            image_player = ImagePlayer(screen, screen_width, screen_height)
            image_player.play_image(current_content)
        elif current_content.endswith(('.mp4')):
            video_player = VideoPlayer(screen, screen_width, screen_height, clock)
            video_player.play_video(current_content)
        else:
            text_player = TextPlayer(screen, screen_width, screen_height)
            text_player.play_text(current_content)

        # Wait for the display time
        while time.time() - start_time < display_time:
            pygame.time.wait(100)

        start_time = time.time()

if __name__ == "__main__":
    main()   
    pygame.quit()
