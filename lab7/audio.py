import pygame
import os


pygame.init()
pygame.mixer.init()
print("P = play \n" \
"S = stop\n" \
"B = previous\n" \
"N = next")
WIDTH = 1600
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎵 Simple Music Player")


songs = [
    "attack on glyphids.mp3",
    "Hammer of justice.mp3",
    "Nightmare king.mp3"
]
images = [
    "drg.jpeg",
    "gerson.jpeg",
    "grimm.jpeg"
]
current = 0  

def play_song(index):
    
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    pygame.display.set_caption(f"Now Playing: {os.path.basename(songs[index])}")


play_song(current)

running = True
paused = False

def load_background(image_path):
    img = pygame.image.load(image_path)
    img = pygame.transform.scale(img, (WIDTH, HEIGHT))
    return img
clock = pygame.time.Clock()
background = load_background(images[current])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("▶️ Resumed")
                
            elif event.key == pygame.K_s:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("⏸️ Paused")
                

            elif event.key == pygame.K_n:  
                current = (current + 1) % len(songs)
                play_song(current)
                print("⏭️ Next song")
                background = load_background(images[current])

            elif event.key == pygame.K_b:  
                current = (current - 1) % len(songs)
                play_song(current)
                print("⏮️ Previous song")
                background = load_background(images[current])

    screen.blit(background, (0, 0))
    
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
