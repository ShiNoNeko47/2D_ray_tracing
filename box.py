import random

class Box:
    verts = []
    def __init__(self, size, window_size):
        position=(random.randint(0, window_size[0] - size), random.randint(0, window_size[1] - size))
        self.size = size
        Box.verts.append((position))
        Box.verts.append((position[0] + self.size, position[1]))
        Box.verts.append((position[0], position[1] + self.size))
        Box.verts.append((position[0] + self.size, position[1] + self.size))

