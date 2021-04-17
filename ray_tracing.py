#!/usr/bin/python

import pygame
import math
import random

class Box:
    verts = []
    def __init__(self, size = 25):
        position=(random.randint(0, 775), random.randint(0, 575))
        self.size = size
        Box.verts.append((position))
        Box.verts.append((position[0] + self.size, position[1]))
        Box.verts.append((position[0], position[1] + self.size))
        Box.verts.append((position[0] + self.size, position[1] + self.size))

def draw_shadows(window, verts, cursor_pos):
    #print(verts)
    p1 = [0, 0]
    p2 = [0, 0]
    if cursor_pos[0] < verts[0][0]:
        if cursor_pos[1] < verts[0][1]:
            #NW
            del verts[3]
            del verts[0]
        elif cursor_pos[1] < verts[2][1]:
            #W
            del verts[3]
            del verts[1]
        else:
            #SW
            del verts[2]
            del verts[1]
        shadow_width1 = 800 - verts[0][0]
        shadow_height1 = shadow_width1 * ((cursor_pos[1] - verts[0][1]) / (cursor_pos[0] - verts[0][0]))
        shadow_width2 = 800 - verts[1][0]
        shadow_height2 = shadow_width2 * ((cursor_pos[1] - verts[1][1]) / (cursor_pos[0] - verts[1][0]))

    elif cursor_pos[0] > verts[1][0]:
        x_border = 0
        if cursor_pos[1] < verts[1][1]:
            #NE
            del verts[2]
            del verts[1]
        elif cursor_pos[1] < verts[2][1]:
            #E
            del verts[2]
            del verts[0]
        else:
            #SE
            del verts[3]
            del verts[0]
        shadow_width1 = -verts[0][0]
        shadow_height1 = shadow_width1 * ((cursor_pos[1] - verts[0][1]) / (cursor_pos[0] - verts[0][0]))
        shadow_width2 = -verts[1][0]
        shadow_height2 = shadow_width2 * ((cursor_pos[1] - verts[1][1]) / (cursor_pos[0] - verts[1][0]))

    elif cursor_pos[1] < verts[0][1]:
        #N
        del verts[3]
        del verts[2]
        shadow_height1 = 600 - verts[0][1]
        shadow_width1 = shadow_height1 * ((cursor_pos[0] - verts[0][0]) / (cursor_pos[1] - verts[0][1]))
        shadow_height2 = 600 - verts[1][1]
        shadow_width2 = shadow_height2 * ((cursor_pos[0] - verts[1][0]) / (cursor_pos[1] - verts[1][1]))

    elif cursor_pos[1] > verts[2][1]:
        #S
        del verts[1]
        del verts[0]
        shadow_height1 = -verts[0][1]
        shadow_width1 = shadow_height1 * ((cursor_pos[0] - verts[0][0]) / (cursor_pos[1] - verts[0][1]))
        shadow_height2 = -verts[1][1]
        shadow_width2 = shadow_height2 * ((cursor_pos[0] - verts[1][0]) / (cursor_pos[1] - verts[1][1]))

    else:
        return False

    p1 = (verts[0][0] + shadow_width1, verts[0][1] + shadow_height1)
    p2 = (verts[1][0] + shadow_width2, verts[1][1] + shadow_height2)
    pygame.draw.polygon(window, (32, 32, 32, 128), (p2, p1, *verts))
    return True


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    loop = True
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)
    boxes = {}
    for i in range(15):
        boxes[str(i)] = Box(i + 20)

    cursor_pos = (0, 0)
    light_img = pygame.image.load('assets/Ligth_point.png')

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEMOTION:
                cursor_pos = event.pos
        window.blit(light_img, (cursor_pos[0] - 800, cursor_pos[1] - 600))

        verts = []

        n = 0
        for vert in Box.verts:
            verts.append((vert))
            if len(verts) == 4:
                pygame.draw.rect(window, (32, 32, 32), pygame.Rect(*verts[0], boxes[str(n)].size, boxes[str(n)].size))
                n += 1
                verts.clear()

        for vert in Box.verts:
            verts.append((vert))
            if len(verts) == 4:
                if not draw_shadows(window, verts, cursor_pos):
                    window.fill((32, 32, 32))
                    break
                verts.clear()


        pygame.display.update()

if __name__ == '__main__':
    main()

