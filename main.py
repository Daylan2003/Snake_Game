from tkinter import *
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "blue"
FOOD_COLOUR = "red"
BACKGROUND_COLOUR = "black"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOUR, tag="snake")
            self.squares.append(square)      

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE  # to generate x random location for food
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE  # to generate y random location for food

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")
      

def next_turn():
    pass  # Implement snake movement and food collision

def change_direction(new_direction):
    pass  # Implement direction change logic

def check_collisions():
    pass  # Check for collisions with walls or the snake itself

def game_over():
    pass  # Handle the end of the game

# Create the main window
window = Tk()
window.title("SNAKE !!!!")
window.resizable(False, False)

# Initial score and direction
score = 0
direction = 'down'

# Create a label to display the score
label = Label(window, text="Score:{}".format(score), font=('Ariel', 40))
label.pack()

# Create the canvas where the game will be drawn
canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Update the window to ensure dimensions are correct before positioning it
window.update()

# Calculate the window's position to center it on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Now set the geometry to center the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

# Start the main loop
window.mainloop()
