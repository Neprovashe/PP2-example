import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 5
    color = 'blue'
    tool = 'brush'  
    drawing = False
    start_pos = None

    def get_color():
        if color == 'red':
            return (255, 0, 0)
        elif color == 'green':
            return (0, 255, 0)
        elif color == 'blue':
            return (0, 0, 255)
        return (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:  
                    radius = min(200, radius + 1)
                elif event.y < 0: 
                    radius = max(1, radius - 1)
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                # colors
                if event.key == pygame.K_r:
                    color = 'red'
                elif event.key == pygame.K_g:
                    color = 'green'
                elif event.key == pygame.K_b:
                    color = 'blue'
                elif event.key == pygame.K_e:
                    color = 'Judgment of hell'
                # tools
                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                
                
                # clear
                elif event.key == pygame.K_c:
                    screen.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    if tool == 'rect':
                        rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                           min(start_pos[1], end_pos[1]),
                                           abs(end_pos[0] - start_pos[0]),
                                           abs(end_pos[1] - start_pos[1]))
                        pygame.draw.rect(screen, get_color(), rect)
                    elif tool == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        r = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                        pygame.draw.circle(screen, get_color(), center, r)

            elif event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'brush':
                    pygame.draw.circle(screen, get_color(), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)


main()
