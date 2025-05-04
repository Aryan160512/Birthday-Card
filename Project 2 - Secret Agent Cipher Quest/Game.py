import os

x = 100
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun

WIDTH = 1000
HEIGHT = 600
TITLE = 'Secret Agent Cipher Quest'

instructions = """Welcome, Agent.

Your mission is to decode a series of encrypted messages, each using a different cipher. 
As you progress, the difficulty will increase. 
Don't worry—you have access to two hints if needed.

Stay sharp. Good luck, Secret Agent!"""

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    screen.draw.text(TITLE, (WIDTH//3, 50), fontsize=40, color="white")
    screen.draw.text(instructions, (50, 150), fontsize=30, color="white")

pgzrun.go()

