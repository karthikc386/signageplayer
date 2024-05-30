import pygame

class TextPlayer:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

    def play_text(self, text):
        base_font_size = self.screen_width // 40
        font = pygame.font.Font(None, base_font_size)
        self.render_text(text, font, pygame.Color('white'), (self.screen_width, self.screen_height))

    def render_text(self, text, font, color, center):
        text = text.rstrip('\r\n')
        words = text.split(' ')
        lines = []
        current_line = []
        width, height = center

        width = width - 200

        while words:
            current_line.append(words.pop(0))
            test_line = ' '.join(current_line)
            if font.size(test_line)[0] > width:
                lines.append(' '.join(current_line[:-1]))
                current_line = [current_line[-1]]
        lines.append(' '.join(current_line))

        # Clear the screen
        self.screen.fill((0, 0, 0))

        y_offset = (self.screen.get_height() - (font.get_height() * len(lines))) // 2

        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += font.get_height()

        pygame.display.flip()