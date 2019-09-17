import pygame
import time
import random

def color_detection(x, y, bg):
    #DDetect the boundaries around the Pac-Man
    for a in range(x, x + 20):
        for b in range(y, y + 20):
            color = screen.get_at((a,b))
            #Determine the colors (Didn't work with color == (0, 0, 255, 255))
            if color != (0, 0, 0, 255) and color != (1, 1, 0, 255) and color != (0, 0, 0, 255) and color != (1, 0, 0, 255) and  color != (0, 1, 0, 255) and color != (255, 255, 255, 255) and color != (0, 0, 1, 255) and color != (1, 0, 1, 255) and color != (0, 1, 1, 255) and color != (1, 1, 1, 255):
                returned = False
                break
            else:
                returned = True
        if returned == False:
            break
    return returned

def color_detection_g(x, y, bg):
    #DDetect the boundaries around the Pac-Man
    for a in range(x, x + 20):
        for b in range(y, y + 20):
            color = screen.get_at((a,b))
            #Determine the colors (Didn't work with color == (0, 0, 255, 255))
            if color == (0,0,255,255):
                returned = False
                break
            else:
                returned = True
        if returned == False:
            break
    return returned

def movements(screen, ghost, ghost_x, ghost_y, bg, dir, count):
    #The movement of the ghost
    #Auto adjustments for early or late turns
    count += 1
    if count >= 20:
        dir = random_dir()
        count -= 20
    if dir == 'pos_y' and color_detection_g(ghost_x, ghost_y + 4, bg) == False:
        ghost_x -= 8
        if color_detection_g(ghost_x, ghost_y + 4, bg) == False:
            ghost_x += 16
            if color_detection_g(ghost_x, ghost_y + 4, bg) == False:
                ghost_x -= 8
                dir = random_dir()

    elif dir == 'neg_y' and color_detection_g(ghost_x, ghost_y - 3, bg) == False:
        ghost_x -= 8
        if color_detection_g(ghost_x, ghost_y - 3, bg) == False:
            ghost_x += 16
            if color_detection_g(ghost_x, ghost_y - 3, bg) == False:
                ghost_x -= 8
                dir = random_dir()

    elif dir == 'pos_x' and color_detection_g(ghost_x + 4, ghost_y, bg) == False:
        ghost_y -= 8
        if color_detection_g(ghost_x + 4, ghost_y, bg) == False:
            ghost_y += 16
            if color_detection_g(ghost_x + 4, ghost_y, bg) == False:
                ghost_y -= 8
                dir = random_dir()

    elif dir == 'neg_x' and color_detection_g(ghost_x - 1 , ghost_y, bg) == False:
        ghost_y -= 8
        if color_detection_g(ghost_x - 1 , ghost_y, bg) == False:
            ghost_y += 16
            if color_detection_g(ghost_x - 1 , ghost_y, bg) == False:
                ghost_y -= 8
                dir = random_dir()

    #Directions and Movements
    if dir == 'pos_y' and color_detection_g(ghost_x, ghost_y + 4, bg) == True:
        ghost_y += 2
    elif dir == 'neg_y' and color_detection_g(ghost_x, ghost_y - 3, bg) == True:
        ghost_y -= 2
    elif dir == 'pos_x' and color_detection_g(ghost_x + 4, ghost_y, bg) == True:
        ghost_x += 2
    elif dir == 'neg_x' and color_detection_g(ghost_x - 1 , ghost_y, bg) == True:
        ghost_x -= 2
    if ghost_x >= 540 or ghost_y >= 600 or ghost_x <= 0 or ghost_y <= 0:
        dir = 'stop'
    #displaying a single image
    screen.blit(ghost, (ghost_x, ghost_y))
    return ghost_x, ghost_y, dir, count;
    #collision = pygame.sprite.collide_rect(ghostman, dots)
def random_dir():
    random_dir = random.randint(1,4)
    if random_dir == 1:
        dir = 'neg_y'
    elif random_dir == 2:
        dir = 'pos_y'
    elif random_dir == 3:
        dir = 'neg_x'
    elif random_dir == 4:
        dir = 'pos_x'
    return dir
def main(screen):
    pac = pygame.image.load('pacr.png')
    pac_x = 20
    pac_y = 20
    ghost1 = pygame.image.load('pinkghost.png')
    ghost2 = pygame.image.load('blueghost.png')
    ghost3 = pygame.image.load('redghost.png')
    ghost4 = pygame.image.load('orange_ghost.png')
    ghost_x1 = 300
    ghost_x2 = 280
    ghost_x3 = 260
    ghost_x4 = 240
    ghost_y1 = 300
    ghost_y2 = 300
    ghost_y3 = 300
    ghost_y4 = 300
    bg = pygame.image.load("background.png")
    dots_bg = pygame.image.load("dotsbackground.png")
    pygame.mixer.music.load('pacman_chomp.wav')
    pygame.mixer.music.play(-1)

    pacman.movements(screen, pac, pac_x, pac_y, bg, dots_bg, ghost1, ghost_x1, ghost_y1, ghost2, ghost_x2, ghost_y2, ghost3, ghost_x3, ghost_y3, ghost4, ghost_x4, ghost_y4)


class pacman():

    def movements(screen, pac, pac_x, pac_y, bg, dots_bg, ghost1, ghost_x1, ghost_y1, ghost2, ghost_x2, ghost_y2, ghost3, ghost_x3, ghost_y3, ghost4, ghost_x4, ghost_y4):
        #The movement of the Pac-Man
            live = True
            dir = ''
            dir_g1 = 'neg_x'
            dir_g2 = 'neg_x'
            dir_g3 = 'neg_x'
            dir_g4 = 'neg_x'
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            dots_list = dots.create_dots(bg, dots_bg)
            while live == True:
                screen.blit(bg, (0, 0))
                #Key detections
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            dir = 'neg_y'
                            pac = pygame.image.load('pacu.png')
                        elif event.key == pygame.K_DOWN:
                            dir = 'pos_y'
                            pac = pygame.image.load('pacd.png')
                        elif event.key == pygame.K_LEFT:
                            dir = 'neg_x'
                            pac = pygame.image.load('pacl.png')
                        elif event.key == pygame.K_RIGHT:
                            dir = 'pos_x'
                            pac = pygame.image.load('pacr.png')
                        elif event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('pac.mp3')
                            pygame.mixer.music.play(-1)
                            menu(screen)
                #Auto adjustments for early or late turns
                if dir == 'pos_y' and color_detection(pac_x, pac_y + 4, bg) == False:
                    pac_x -= 8
                    if color_detection(pac_x, pac_y + 4, bg) == False:
                        pac_x += 16
                        if color_detection(pac_x, pac_y + 4, bg) == False:
                            pac_x -= 8

                elif dir == 'neg_y' and color_detection(pac_x, pac_y - 3, bg) == False:
                    pac_x -= 8
                    if color_detection(pac_x, pac_y - 3, bg) == False:
                        pac_x += 16
                        if color_detection(pac_x, pac_y - 3, bg) == False:
                            pac_x -= 8

                elif dir == 'pos_x' and color_detection(pac_x + 4, pac_y, bg) == False:
                    pac_y -= 8
                    if color_detection(pac_x + 4, pac_y, bg) == False:
                        pac_y += 16
                        if color_detection(pac_x + 4, pac_y, bg) == False:
                            pac_y -= 8

                elif dir == 'neg_x' and color_detection(pac_x - 1 , pac_y, bg) == False:
                    pac_y -= 8
                    if color_detection(pac_x - 1 , pac_y, bg) == False:
                        pac_y += 16
                        if color_detection(pac_x - 1 , pac_y, bg) == False:
                            pac_y -= 8

                #Directions and Movements
                if dir == 'pos_y' and color_detection(pac_x, pac_y + 4, bg) == True:
                    pac_y += 2
                elif dir == 'neg_y' and color_detection(pac_x, pac_y - 3, bg) == True:
                    pac_y -= 2
                elif dir == 'pos_x' and color_detection(pac_x + 4, pac_y, bg) == True:
                    pac_x += 2
                elif dir == 'neg_x' and color_detection(pac_x - 1 , pac_y, bg) == True:
                    pac_x -= 2
                if pac_x >= 540 or pac_y >= 600 or pac_x <= 0 or pac_y <= 0:
                    dir = 'stop'
    			#displaying a single image
                screen.blit(pac, (pac_x, pac_y))
                movements(screen, ghost1, ghost_x1, ghost_y1, bg, dir_g1, count1)
                movements(screen, ghost2, ghost_x2, ghost_y2, bg, dir_g2, count2)
                movements(screen, ghost3, ghost_x3, ghost_y3, bg, dir_g3, count3)
                movements(screen, ghost4, ghost_x4, ghost_y4, bg, dir_g4, count4)
                ghost_x1, ghost_y1, dir_g1, count1 = (movements(screen, ghost1, ghost_x1, ghost_y1, bg, dir_g1, count1))
                ghost_x2, ghost_y2, dir_g2, count2 = (movements(screen, ghost2, ghost_x2, ghost_y2, bg, dir_g2, count2))
                ghost_x3, ghost_y3, dir_g3, count3 = (movements(screen, ghost3, ghost_x3, ghost_y3, bg, dir_g3, count3))
                ghost_x4, ghost_y4, dir_g4, count4 = (movements(screen, ghost4, ghost_x4, ghost_y4, bg, dir_g4, count4))
                #collision = pygame.sprite.collide_rect(pacman, dots)
                for x in range(len(dots_list)):
                    #print(dots_list[x])
                    if dots_list[x][1] == pac_x and dots_list[x][2] == pac_y:
                        print("Collision")
                pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((560, 620))
main(screen)
