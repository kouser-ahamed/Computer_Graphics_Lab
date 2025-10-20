from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

x0, y0 = 100, 80
x1, y1 = 500, 520

def get_zone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx >= 0 and dy < 0:
            return 7
        elif dx < 0 and dy >= 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
    elif abs(dx) < abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx >= 0 and dy < 0:
            return 6
        elif dx < 0 and dy >= 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5

def convert_to_zone_0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convert_back_from_zone_0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def midpoint(x1, y1, x2, y2):
    points = []

    zone = get_zone(x1, y1, x2, y2)

    x1_zone0, y1_zone0 = convert_to_zone_0(x1, y1, zone)
    x2_zone0, y2_zone0 = convert_to_zone_0(x2, y2, zone)

    dx = x2_zone0 - x1_zone0
    dy = y2_zone0 - y1_zone0

    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x1_zone0
    y = y1_zone0

    while x <= x2_zone0:
        real_x, real_y = convert_back_from_zone_0(x, y, zone)
        points.append((real_x, real_y))
        if d <= 0:
            d += incE
        else:
            d += incNE
            y += 1
        x += 1

    glBegin(GL_POINTS)
    for px, py in points:
        glVertex2f(px, py)
    glEnd()

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0, 1.0, 0)

    midpoint(100, 100, 260, 100)
    midpoint(260, 100, 260, 260)
    midpoint(260, 260, 100, 260)
    midpoint(100, 260, 100, 100)

    midpoint(60, 140, 220, 140)
    midpoint(220, 140, 220, 300)
    midpoint(220, 300, 60, 300)
    midpoint(60, 300, 60, 140)

    midpoint(100, 100, 60, 140)
    midpoint(260, 100, 220, 140)
    midpoint(260, 260, 220, 300)
    midpoint(100, 260, 60, 300)


    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def start():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"Square with Midpoint Line Algorithm")
    glutDisplayFunc(show)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    start()
