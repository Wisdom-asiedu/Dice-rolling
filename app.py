import pyglet
import random

class DiceSimulator(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.dice_size = 50
        self.dice_spacing = 20
        self.previous_rolls = []
        self.roll_again = False
        
        self.num_dice = 0
        self.num_faces = 0

        # Create text inputs
        self.dice_input_label = pyglet.text.Label('Number of Dice:', font_size=14, x=20, y=50)
        self.dice_input = pyglet.text.Label('', font_size=14, x=150, y=50)
        
        self.faces_input_label = pyglet.text.Label('Number of Faces:', font_size=14, x=20, y=20)
        self.faces_input = pyglet.text.Label('', font_size=14, x=150, y=20)

        # Create buttons
        self.roll_button = pyglet.text.Label('Roll', font_size=14, x=300, y=20)
        self.roll_again_button = pyglet.text.Label('Roll Again', font_size=14, x=400, y=20)

        # Set up text input handlers
        self.dice_input.caret = "|"
        self.faces_input.caret = "|"

        # Initialize number of dice and faces
        self.num_dice = 0
        self.num_faces = 0

    def draw_dice(self, x, y, value):
        dice_sprite = pyglet.image.load('src/assets/dice{}.png'.format(value))
        dice_sprite.blit(x, y, width=self.dice_size, height=self.dice_size)

    def draw_previous_rolls(self):
        y = 200
        for roll in self.previous_rolls:
            roll_label = pyglet.text.Label(str(roll), font_size=14, x=20, y=y)
            roll_label.draw()
            y -= 20

    def on_draw(self):
        self.clear()
        self.dice_input_label.draw()
        self.dice_input.draw()
        self.faces_input_label.draw()
        self.faces_input.draw()
        self.roll_button.draw()
        self.roll_again_button.draw()
        
        x = 20
        y = 150
        if self.num_dice > 0 and self.num_faces > 0:
            for i in range(self.num_dice):
                value = random.randint(1, self.num_faces)
                self.draw_dice(x, y, value)
                x += self.dice_size + self.dice_spacing

        self.draw_previous_rolls()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            if 300 < x < 400 and 20 < y < 40:  # Roll Button
                self.roll_dice()

    def on_text(self, text):
        if self.dice_input.text and self.faces_input.text:
            self.num_dice = int(self.dice_input.text)
            self.num_faces = int(self.faces_input.text)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.BACKSPACE:
            self.dice_input.text = self.dice_input.text[:-1]
            self.faces_input.text = self.faces_input.text[:-1]

    def roll_dice(self):
        if self.num_dice > 0 and self.num_faces > 0:
            self.previous_rolls.clear()
            for _ in range(self.num_dice):
                roll = random.randint(1, self.num_faces)
                self.previous_rolls.append(roll)

    def update(self, dt):
        if self.roll_again:
            self.roll_dice()
            self.roll_again = False

if __name__ == "__main__":
    window = DiceSimulator(800, 600, "Dice Rolling Simulator")
    pyglet.clock.schedule_interval(window.update, 1/60)
    pyglet.app.run()
