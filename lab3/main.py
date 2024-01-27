# -.- coding: utf8 -.-
import pygame
import math as m
import pygame.draw as pd
import sys
import random

screen_color = (255, 255, 255)
screen_size_x, screen_size_y = 900, 900
bot_steps = (-3, -2, -1, 1, 2, 3)
max_size = 500
min_size = 100

def main():
    global screen_color
    pygame.init()
    screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    screen.fill(screen_color)
    FPS = 60

    # draw the face
    face = Face(screen)
    face.draw_face()

    pygame.display.update()
    clock = pygame.time.Clock()

    any_faces = create_faces(screen, 3, bot_steps)

    while True:
        screen.fill(screen_color)
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
        for bot_face in any_faces:
            bot_face.move_auto()
            bot_face.draw_face()

        pygame.display.flip()


class Face():
    """Draws the face at the center of the screen and returns the face"""
    global draw_mouth, draw_eyes, max_size, mix_size
    def __init__(self, screen, speed_x = 0, speed_y = 0):
        self.screen = screen
        screen_coordinate = self.screen.get_size()
        self.coord = screen_coordinate
        self.face = None
        self.pos_y = self.coord[1]/2
        self.pos_x = self.coord[0]/2
        self.size = 100
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.max_size = max_size
        self.min_size = min_size


    def draw_face(self):
        self.face = pd.circle(self.screen, 'orange', (self.pos_x, self.pos_y), self.size)
        draw_mouth(self.screen, self.face)
        draw_eyes(self.screen, self.face)


    def move(self, keys, dist, size):
        global screen_color
        check_y_min = self.pos_y <= self.size
        check_y_plus = self.pos_y >= self.coord[1] - self.size
        if keys[pygame.K_LSHIFT]:
            dist *= 2
        if keys[pygame.K_w]:
            if keys[pygame.K_d] or keys[pygame.K_a]:
                if self.pos_y > self.size:
                    self.pos_y -= dist*0.71
            else:
                if self.pos_y > self.size:
                    self.pos_y -= dist
        if keys[pygame.K_s]:
            if keys[pygame.K_d] or keys[pygame.K_a]:
                if self.pos_y < self.coord[1] - self.size:
                    self.pos_y += dist*0.71
            else:
                if self.pos_y < self.coord[1] - self.size:
                    self.pos_y += dist
        if keys[pygame.K_d]:
            if keys[pygame.K_w] or keys[pygame.K_s]:
                if self.pos_x < self.coord[0] - self.size:
                    self.pos_x += dist*0.71
            else:
                if self.pos_x < self.coord[0] - self.size:
                    self.pos_x += dist
        if keys[pygame.K_a]:
            if keys[pygame.K_w] or keys[pygame.K_s]:
                if self.pos_x > self.size:
                    self.pos_x -= dist*0.71
            else:
                if self.pos_x > self.size:
                    self.pos_x -= dist
        if keys[pygame.K_UP]:
            if self.size < self.coord[0]/2 and self.coord[1]/2 and self.size < self.max_size/2:
                self.size += size
                if self.pos_x < self.size:
                    self.pos_x += size
                if self.pos_x > self.coord[0] - self.size:
                    self.pos_x -= size
                if self.pos_y < self.size:
                    self.pos_y += size
                if self.pos_y > self.coord[1] - self.size:
                    self.pos_y -= size

        if keys[pygame.K_DOWN]:
            if self.size > self.min_size/2:
                self.size -= size

        self.draw_face()


    def move_auto(self):

        if self.pos_x < self.size or self.pos_x > self.coord[0] - self.size:
            self.speed_x = -self.speed_x
        if self.pos_y < self.size or self.pos_y > self.coord[1] - self.size:
            self.speed_y = -self.speed_y
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y


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


def create_faces(screen, value: int, steps):
    faces = []
    for i in range(value):
        value_x = random.choice(steps)
        value_y = random.choice(steps)
        faces.append(Face(screen, speed_x=value_x, speed_y=value_y))
    return faces


if __name__ == '__main__':
    main()