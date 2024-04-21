import pyglet
import random

# Initialize the window
window = pyglet.window.Window(800, 600, "Dice Rolling Simulator")

# Set up the background color
pyglet.gl.glClearColor(0.2, 0.3, 0.2, 0.8)

# Define some constants
DICE_SIZE = 50
DICE_SPACING = 20
PREVIOUS_ROLLS_X = 20
PREVIOUS_ROLLS_Y = 500

# Define global variables
num_dice = int(input("dice: "))
num_faces = int(input("faces: "))
previous_rolls = []

# Define a dice label
dice_label = pyglet.text.Label("Number of Dice: {}   Number of Faces: {}".format(num_dice, num_faces),
                               font_name='Times New Roman',
                               font_size=16,
                               x=20, y=570,
                               anchor_x='left', anchor_y='top')

# Define a function to draw a single dice
def draw_dice(x, y, value):
    dice_sprite = pyglet.image.load('src/assets/dice{}.png'.format(value))
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
    x = 20
    y = 20
    roll = []
    for i in range(num_dice):
        value = random.randint(1, num_faces)
        draw_dice(x, y, value)
        roll.append(value)
        x += DICE_SIZE + DICE_SPACING
    previous_rolls.append(roll)
    draw_previous_rolls()

# Define the on_key_press event handler
@window.event
def on_key_press(symbol, modifiers):
    global num_dice, num_faces
    if symbol == pyglet.window.key.N:
        num_dice = int(pyglet.window.get_input().text(caption="Enter the number of dice:", initial="2"))
    elif symbol == pyglet.window.key.F:
        num_faces = int(pyglet.window.get_input().text(caption="Enter the number of faces:", initial="6"))
    dice_label.text = "Number of Dice: {}   Number of Faces: {}".format(num_dice, num_faces)

# Start the Pyglet event loop
pyglet.app.run()