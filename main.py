import os
import pygame
import time
import itertools
import json

from services.ImagePlayer import ImagePlayer
from services.TextPlayer import TextPlayer
from services.VideoPlayer import VideoPlayer

from utils.DirectoryStructure import categorize_files
from utils.Common import check_file_extension

content_folder = 'content'
config_file_path = os.path.join('config', 'config.json')

with open(config_file_path, 'r') as file:
    config = json.load(file)

pygame.init()

device_info = pygame.display.Info()
screen_width, screen_height = device_info.current_w, device_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption('Player')
pygame.mouse.set_visible(False)


images, texts, videos = categorize_files(content_folder)

content = itertools.cycle(images + texts + videos) 

display_time = config["default_display_time"]
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
        if check_file_extension(current_content, config["image_supported_formats"]):
            image_player = ImagePlayer(screen, screen_width, screen_height)
            image_player.play_image(current_content)
        elif check_file_extension(current_content, config["video_supported_formats"]):
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
