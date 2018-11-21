import pygame.font

class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # display the score font
        self.test_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prep the scoreimg
        self.prep_score()

    def prep_score(self):
        """ turn the score into a img """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, slef.text_color, slef.ai_settings.bg_color)

        # put the score on the right-top conner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ display the score on the screen """
        self.screen.blit(self.score_image, self.score_rect)
