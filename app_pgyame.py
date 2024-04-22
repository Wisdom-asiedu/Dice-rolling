import pygame
from pygame.locals import *

import random

class DiceSimulator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.dice_size = 70
        self.dice_spacing = 20
        self.previous_rolls = []
        self.roll_again = False
        self.roll_start_time = 0
        
        self.num_dice = 0
        self.num_faces = 0

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Dice Rolling Simulator")

        # Colors
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 70, 0)
        self.WHITE = (255, 255, 255)

        # Fonts
        self.font = pygame.font.Font(None, 24)

        # Text inputs
        self.dice_input_text = "2"
        self.faces_input_text = "6"

    def draw_dice(self, x, y, value):
        dice_image = pygame.image.load(f'src/assets/dice{value}.png')
        dice_image = pygame.transform.scale(dice_image, (self.dice_size, self.dice_size))
        self.screen.blit(dice_image, (x, y))

    def draw_previous_rolls(self):
        y = 200
        for roll in self.previous_rolls:
            roll_label = self.font.render(str(roll), True, self.WHITE)
            self.screen.blit(roll_label, (20, y))
            y -= 20

    def draw(self):
        self.screen.fill(self.GREEN)

        # Draw text inputs
        self.draw_text_input("Number of Dice:", self.dice_input_text, (20, 50))
        self.draw_text_input("Number of Faces:", self.faces_input_text, (20, 20))

        # Draw buttons
        self.draw_button("Roll", (300, 20))

        # Draw dice
        x = 20
        y = 150
        if self.num_dice > 0 and self.num_faces > 0:
            for i in range(self.num_dice):
                if self.roll_again:
                    value = random.randint(1, self.num_faces)
                else:
                    value = self.previous_rolls[i] if i < len(self.previous_rolls) else random.randint(1, self.num_faces)
                self.draw_dice(x, y, value)
                x += self.dice_size + self.dice_spacing

        self.draw_previous_rolls()

        pygame.display.flip()

    def draw_text_input(self, label, text, pos):
        label_surface = self.font.render(label, True, self.WHITE)
        self.screen.blit(label_surface, pos)
        input_surface = self.font.render(text, True, self.WHITE)
        self.screen.blit(input_surface, (pos[0] + 150, pos[1]))

    def draw_button(self, label, pos):
        button_surface = self.font.render(label, True, self.WHITE)
        self.screen.blit(button_surface, pos)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if pygame.key.get_mods() & KMOD_CTRL:
                        # Handle Ctrl + Backspace for clearing the input
                        self.dice_input_text = ""
                        self.faces_input_text = ""
                    else:
                        # Otherwise, just remove the last character
                        self.dice_input_text = self.dice_input_text[:-1]
                        self.faces_input_text = self.faces_input_text[:-1]
                elif event.key == K_RETURN:
                    # Roll the dice when Enter is pressed
                    self.roll_dice()
                else:
                    # Add typed characters to the input text ####Shall add a hover event
                    self.dice_input_text += event.unicode
                    self.faces_input_text += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 < event.pos[0] < 400 and 20 < event.pos[1] < 50:  # Roll Button
                        self.roll_dice()
                        self.roll_again = True
                    #elif 400 < event.pos[0] < 500 and 20 < event.pos[1] < 50:  # Roll Again Button
                        

    def roll_dice(self):
        if self.dice_input_text and self.faces_input_text:
            self.num_dice = int(self.dice_input_text)
            self.num_faces = int(self.faces_input_text)
            self.previous_rolls.clear()
            self.roll_start_time = pygame.time.get_ticks()
            for _ in range(self.num_dice):
                roll = random.randint(1, self.num_faces)
                self.previous_rolls.append(roll)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(30)
            self.handle_events()
            if self.roll_again:
                current_time = pygame.time.get_ticks()
                if current_time - self.roll_start_time >= 1200:
                    self.roll_again = False
            self.draw()

if __name__ == "__main__":
    simulator = DiceSimulator(800, 600)
    simulator.run()
