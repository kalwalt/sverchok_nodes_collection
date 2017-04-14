"""
in vertices v d=[[]] n=0
in octaves s d=2 n=2
in hard_on s d=1 n=2
in noise_type s d=0 n=2
in amp s d=0.5 n=2
in freq s d=2. n=2
in turb s d=3.0 n=2
in red s d=.3 n=2
in green s d=.3 n=2
in blue s d=.6 n=2
out data v
""" 

from mathutils import noise, Vector, Color
import math

def marble(pnt):
    pnt = Vector(pnt)
    y = pnt.y + turb * noise.turbulence(pnt, octaves, hard_on, noise_type, amp, freq)
    y = math.sin (y * math.pi/2)
    return marble_color(y)

def marble_color(x):
    clr = Color((0.0, 0.0, 0.0))
    x = math.sqrt(x + 1.0) * .707
    clr.g = green + .8 * x
    x = math.sqrt(x)
    clr.r = red + .6 * x
    clr.b = blue + .4 * x
    return clr[:]

data = [[marble(v) for v in vertices[0]]]

