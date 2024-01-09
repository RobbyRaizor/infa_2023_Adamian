# -.- coding: utf8 -.-
import pygame
import math as m
import pygame.draw as pd
import sys

screen_color = (255, 255, 255)

def main():
    global screen_color
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill(screen_color)
    FPS = 60

    # draw the face
    face = Face(screen)
    face.draw_face()

    pygame.display.update()
    clock = pygame.time.Clock()

    while True:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if screen_color == (255, 255, 255):
                        screen_color = (0, 0, 0)
                    elif screen_color == (0, 0, 0):
                        screen_color = (255, 255, 255)

        face.move(keys, 2, 1)
        pygame.display.flip()


class Face():
    """Draw the face at the center of the screen and returns the face"""
    def __init__(self, screen):
        self.screen = screen
        screen_coordinate = self.screen.get_size()
        self.coord = screen_coordinate
        self.face = None
        self.pos_y = self.coord[1]/2
        self.pos_x = self.coord[0]/2
        self.size = 100

    global draw_mouth, draw_eyes

    def draw_face(self):
        self.face = pd.circle(self.screen, 'orange', (self.pos_x, self.pos_y), self.size)
        draw_mouth(self.screen, self.face)
        draw_eyes(self.screen, self.face)


    def move(self, keys, dist, size):
        global screen_color
        if keys[pygame.K_w]:
            self.pos_y -= dist
        if keys[pygame.K_s]:
            self.pos_y += dist
        if keys[pygame.K_d]:
            self.pos_x += dist
        if keys[pygame.K_a]:
            self.pos_x -= dist
        if keys[pygame.K_UP]:
            self.size += size
        if keys[pygame.K_DOWN]:
            self.size -= size

        self.screen.fill(screen_color)
        self.draw_face()


def draw_eyes(screen, face):
    """Draws eveil eyes on the particular face"""
    face_radius = face.width/2
    eye_radius = face_radius*0.1
    eye_coordinate_diff = (face_radius * m.sin(m.radians(45)))*0.5

    #draw the left eye
    pd.circle(screen, 'orange', ((face.centerx - eye_coordinate_diff),
                                 (face.centery - eye_coordinate_diff)),
                                  eye_radius)
    pd.circle(screen, 'white', ((face.centerx - eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
                                 eye_radius*0.9)
    pd.circle(screen, 'black', ((face.centerx - eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
                                 eye_radius*0.5)

    #draw the right eye
    pd.circle(screen, 'orange', ((face.centerx + eye_coordinate_diff),
                                 (face.centery - eye_coordinate_diff)),
              eye_radius)
    pd.circle(screen, 'white', ((face.centerx + eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
              eye_radius * 0.9)
    pd.circle(screen, 'black', ((face.centerx + eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
              eye_radius * 0.5)


    #draw the right eye
    pd.circle(screen, 'orange', ((face.centerx + eye_coordinate_diff),
                                 (face.centery - eye_coordinate_diff)),
              eye_radius)
    pd.circle(screen, 'white', ((face.centerx + eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
              eye_radius * 0.9)
    pd.circle(screen, 'black', ((face.centerx + eye_coordinate_diff),
                                (face.centery - eye_coordinate_diff)),
              eye_radius * 0.5)


def draw_mouth(screen, face):
    """Draws a mouth on the particular face"""
    face_radius = face.width / 2
    mouth_coord_diff_y = face_radius*0.5
    mouth_width = face_radius*0.6
    mouth_height = face_radius*0.1
    #draw lips
    pd.rect(screen, 'red', ((face.centerx-mouth_width/2),
                            (face.centery+mouth_coord_diff_y+mouth_height/2),
                             mouth_width, mouth_height))
    pd.rect(screen, 'black', ((face.centerx - mouth_width*0.9 / 2),
                            (face.centery + mouth_coord_diff_y + mouth_height*1.2 / 2),
                            mouth_width*0.9, mouth_height*0.8))

if __name__ == '__main__':
    main()