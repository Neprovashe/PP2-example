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


                elif event.key == pygame.K_4:
                    tool = 'r_triangle'
                elif event.key == pygame.K_5:
                    tool = 'triangle'
                elif event.key == pygame.K_6:
                    tool = 'romb'
                
                
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
                    elif tool == 'r_triangle':
                        p1 = start_pos
                        p2 = end_pos
                        p3 = (start_pos[0], end_pos[1])
                        pygame.draw.polygon(screen, get_color(), (p1,p2,p3))
                    elif tool == 'triangle':
                        p1 = start_pos
                        p2 = end_pos

                        x1, y1 = p1
                        x2, y2 = p2

                        dx = x2 - x1
                        dy = y2 - y1
                        side = (dx*dx + dy*dy)**0.5

                        if side != 0:
                            
                            h = (3**0.5) / 2 * side

                            mx = (x1 + x2) / 2
                            my = (y1 + y2) / 2

                            
                            px = -dy / side
                            py =  dx / side

                            
                            p3 = (mx + px * h, my + py * h)

                            pygame.draw.polygon(screen, get_color(), (p1, p2, p3))
                    elif tool == 'romb':
                        p1 = start_pos
                        p2 = end_pos

                        x1, y1 = p1
                        x2, y2 = p2

                        dx = x2 - x1
                        dy = y2 - y1
                        d = (dx*dx + dy*dy) ** 0.5
                        if d == 0:
                            continue

                        mx = (x1 + x2) / 2
                        my = (y1 + y2) / 2

                        px = -dy / d
                        py =  dx / d

                        ratio = 0.6
                        h = (d * ratio) / 2

                        q1 = (mx + px*h, my + py*h)
                        q2 = (mx - px*h, my - py*h)

                        pygame.draw.polygon(screen, get_color(), (p1, q1, p2, q2))

                        

            elif event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'brush':
                    pygame.draw.circle(screen, get_color(), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)


main()
