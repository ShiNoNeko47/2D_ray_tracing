import pygame

def draw_shadows(window, verts, cursor_pos, shadow_color, window_size):
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
        shadow_width1 = window_size[0] - verts[0][0]
        shadow_height1 = shadow_width1 * ((cursor_pos[1] - verts[0][1]) / (cursor_pos[0] - verts[0][0]))
        shadow_width2 = window_size[0] - verts[1][0]
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
        shadow_height1 = window_size[1] - verts[0][1]
        shadow_width1 = shadow_height1 * ((cursor_pos[0] - verts[0][0]) / (cursor_pos[1] - verts[0][1]))
        shadow_height2 = window_size[1] - verts[1][1]
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
    pygame.draw.polygon(window, shadow_color, (p2, p1, *verts))
    return True

