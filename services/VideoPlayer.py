import pygame
import cv2

class VideoPlayer:
    def __init__(self, screen, screen_width, screen_height, clock):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = clock

    def play_video(self, path):
        try:
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = cv2.resize(frame, (self.screen_width, self.screen_height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.transpose(frame)
                frame_surface = pygame.surfarray.make_surface(frame)
                self.screen.blit(frame_surface, (0, 0))
                pygame.display.update()
                
                self.clock.tick(fps)

            cap.release()

        except Exception as e:
            print(f"An error occurred: {e}")
            if 'cap' in locals() and cap.isOpened():
                cap.release()