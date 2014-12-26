import pygame


PLAYER1_UP = pygame.K_q
PLAYER1_DOWN = pygame.K_a

PLAYER2_UP = pygame.K_UP
PLATER2_DOWN = pygame.K_DOWN


class PygView(object):
    def __init__(self, width=1024, height=768, fps=30):
        pygame.init()
        pygame.display.set_caption('Press ESC to quit')

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.DOUBLEBUF)

        self.background = pygame.Surface(self.screen.get_size()).convert()

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    else:
                        print event.key

            self.draw_text('pong')
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_text(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, (
            (self.width - fw) / 2,
            (self.height - fh) / 2))


if __name__ == '__main__':
    PygView(1000, 600).run()
