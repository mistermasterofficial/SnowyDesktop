import math

class Vec():
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[-1]

def length(vec, start_coords=Vec(0)):
    return math.hypot(abs(vec.x-start_coords.x), abs(vec.y-start_coords.y))

def norm(vec):
    return Vec(vec.x/length(vec), vec.y/length(vec))

def dot(vec1, vec2):
    return vec1.x*vec2.x+vec1.y*vec2.y