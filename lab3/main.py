import pygame
import math as m
import pygame.draw as pd

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    print(screen.get_size())
    screen.fill((255, 255, 255))
    FPS = 1

    # draw the face
    draw_face(screen)

    pygame.display.update()
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def draw_face(screen):
    """Draw the face at the center of the screen"""
    screen_coordinate = screen.get_size()
    face = pd.circle(screen, 'yellow', (screen_coordinate[0]/2, screen_coordinate[1]/2), 200)
    draw_evil_eyes(screen, face)
    draw_mouth(screen, face)


def draw_evil_eyes(screen, face):
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


def increase_color(object):
    pass

if __name__ == '__main__':
    main()