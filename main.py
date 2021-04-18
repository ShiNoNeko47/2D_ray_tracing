#!/usr/bin/python

import pygame
from box import Box
from shadows import draw_shadows

def main():

#==================================================
    box_number = 100
    box_size = 20
    shadow_color = (32, 32, 32)
#==================================================

    pygame.init()
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    loop = True
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)
    boxes = {}
    for i in range(box_number):
        boxes[str(i)] = Box(box_size, window_size)

    cursor_pos = (0, 0)
    light_img = pygame.image.load('Ligth_point.png')

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
                pygame.draw.rect(window, shadow_color, pygame.Rect(*verts[0], boxes[str(n)].size, boxes[str(n)].size))
                n += 1
                verts.clear()

        for vert in Box.verts:
            verts.append((vert))
            if len(verts) == 4:
                if not draw_shadows(window, verts, cursor_pos, shadow_color, window_size):
                    window.fill(shadow_color)
                    break
                verts.clear()


        pygame.display.update()

if __name__ == '__main__':
    main()

