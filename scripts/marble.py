"""
in vertices v d=[[]] n=0
in octaves s d=2 n=2
in hard_on s d=1 n=2
in noise_type s d=0 n=2
in amp s d=0.5 n=2
in freq s d=2. n=2
out data v
""" 

from mathutils import noise, Vector, Color
import math

def marble(pnt):
    pnt = Vector(pnt)
    y = pnt.y + 3.0 * noise.turbulence(pnt, octaves, hard_on, noise_type, amp, freq)
    y = math.sin (y * math.pi/2)
    return marble_color(y)

def marble_color(x):
    clr = Color((0.0, 0.0, 0.0))
    x = math.sqrt(x + 1.0) * .707
    clr.g = .30 + .8 * x
    x = math.sqrt(x)
    clr.r = .30 + .6 * x
    clr.b = .60 + .4 * x
    return clr[:]

data = [[marble(v) for v in vertices[0]]]

