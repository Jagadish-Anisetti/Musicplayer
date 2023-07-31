import pygame
import os

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (optional)
screen_width, screen_height = 400, 200
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window (optional)
pygame.display.set_caption("Music Player")

# Set the directory where your music files are located
music_dir = r"C:\musicplayer\patalu"

# Initialize the music player
pygame.mixer.init()

# Function to play music
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Load the play and stop button images
play_button_img = pygame.image.load("play_button.png")
stop_button_img = pygame.image.load("stop_button.png")

# Scale the button images to fit the screen
button_width, button_height = 80, 80
play_button_img = pygame.transform.scale(play_button_img, (button_width, button_height))
stop_button_img = pygame.transform.scale(stop_button_img, (button_width, button_height))

# Set the initial position of the buttons
play_button_x, play_button_y = 50, 60
stop_button_x, stop_button_y = 270, 60

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if the play button is clicked
            if play_button_x <= mouse_x <= play_button_x + button_width and \
                    play_button_y <= mouse_y <= play_button_y + button_height:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
                    if len(music_files) > 0:
                        play_music(os.path.join(music_dir, music_files[0]))
                    else:
                        print("No music files found in the specified directory.")
            # Check if the stop button is clicked
            elif stop_button_x <= mouse_x <= stop_button_x + button_width and \
                    stop_button_y <= mouse_y <= stop_button_y + button_height:
                stop_music()

    # Draw the buttons on the screen
    screen.blit(play_button_img, (play_button_x, play_button_y))
    screen.blit(stop_button_img, (stop_button_x, stop_button_y))

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()