import pyglet
import random

# Initialize the window
window = pyglet.window.Window(800, 600, "Dice Rolling Simulator")

# Set up the background color
pyglet.gl.glClearColor(0.2, 0.3, 0.2, 1.0)

# Define some constants
DICE_SIZE = 70
DICE_SPACING = 20
PREVIOUS_ROLLS_X = 20
PREVIOUS_ROLLS_Y = 500

# Define global variables
num_dice = 2
num_faces = 6
previous_rolls = []
dice_values = []
rolling = False

# Define a dice label
dice_label = pyglet.text.Label("",
                               font_name='Times New Roman',
                               font_size=16,
                               x=20, y=570,
                               anchor_x='left', anchor_y='top')

# Define a function to draw a single dice
def draw_dice(x, y, value):
    dice_sprite = pyglet.image.load(f'src/assets/dice{value}.png')
    dice_sprite.blit(x, y, width=DICE_SIZE, height=DICE_SIZE)

# Define a function to draw the previous rolls
def draw_previous_rolls():
    y = PREVIOUS_ROLLS_Y
    for roll in previous_rolls:
        roll_label = pyglet.text.Label(str(roll), font_name='Times New Roman', font_size=12, x=PREVIOUS_ROLLS_X, y=y, anchor_x='left', anchor_y='top')
        roll_label.draw()
        y -= 20

# Define the on_draw event handler
@window.event
def on_draw():
    window.clear()
    dice_label.draw()
    if not rolling:
        x = 20
        y = 20
        for value in dice_values:
            draw_dice(x, y, value)
            x += DICE_SIZE + DICE_SPACING
    draw_previous_rolls()

# Define the on_key_press event handler
@window.event
def on_key_press(symbol, modifiers):
    global num_dice, num_faces, rolling, dice_values, previous_rolls
    if symbol == pyglet.window.key.N:
        num_dice = int(pyglet.window.get_input().text(caption="Enter the number of dice:", initial="2"))
    elif symbol == pyglet.window.key.F:
        num_faces = int(pyglet.window.get_input().text(caption="Enter the number of faces:", initial="6"))
    elif symbol == pyglet.window.key.R:
        rolling = True
        dice_values = [random.randint(1, num_faces) for _ in range(num_dice)]
        previous_rolls.append(dice_values.copy())
        rolling = False
    dice_label.text = "Number of Dice: {}   Number of Faces: {}".format(num_dice, num_faces)

# Define the update function
def update(dt):
    pass  # No need for an update function in this case

# Start the Pyglet event loop
pyglet.app.run()