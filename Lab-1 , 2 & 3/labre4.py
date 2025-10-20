from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def txt(x, y, s):
    glRasterPos2f(x, y)
    for ch in s:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def midpoint_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    sx = 1 if dx >= 0 else -1
    sy = 1 if dy >= 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    pts = []

    if dx > dy:
        p = 2*dy - dx
        for _ in range(dx + 1):
            pts.append((x, y))
            x += sx
            if p >= 0:
                y += sy
                p -= 2*dx
            p += 2*dy
    else:
        p = 2*dx - dy
        for _ in range(dy + 1):
            pts.append((x, y))
            y += sy
            if p >= 0:
                x += sx
                p -= 2*dy
            p += 2*dx

    glBegin(GL_POINTS)
    for px, py in pts:
        glVertex2f(px, py)
    glEnd()

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(1.0, 0, 0)

    points = {
        "A": (260, 355),
        "B": (160, 255),
        "C": (360, 255),
        "D": (460, 355),
        "E": (560, 255),
        "F": (270, 345),
        "G": (185, 255),
        "H": (535, 180),
        "I": (360, 155),
        "J": (185, 180),
        "K": (420, 230),
        "L": (470, 230),
        "M": (420, 165),
        "N": (470, 170),
        "O": (235, 230),
        "P": (285, 230),
        "Q": (235, 175),
        "R": (285, 170),
        "S": (415, 355),
        "T": (445, 355),
        "U": (415, 410),
        "V": (445, 410)
    }

    # House structure lines
    midpoint_line(260, 355, 160, 255)
    midpoint_line(260, 355, 360, 255)
    midpoint_line(260, 355, 460, 355)
    midpoint_line(360, 255, 560, 255)
    midpoint_line(460, 355, 560, 255)
    midpoint_line(270, 345, 185, 255)
    midpoint_line(160, 255, 185, 255)
    midpoint_line(535, 180, 535, 255)
    midpoint_line(360, 255, 360, 155)
    midpoint_line(185, 255, 185, 180)
    midpoint_line(185, 180, 360, 155)
    midpoint_line(360, 155, 535, 180)
    midpoint_line(420, 230, 470, 230)
    midpoint_line(420, 230, 420, 165)
    midpoint_line(470, 230, 470, 170)
    midpoint_line(235, 230, 285, 230)
    midpoint_line(235, 230, 235, 175)
    midpoint_line(285, 230, 285, 170)
    midpoint_line(415, 355, 415, 410)
    midpoint_line(445, 355, 445, 410)
    midpoint_line(415, 410, 445, 410)

    # Points text
    glColor3f(1, 1, 1)
    offsets = [
        (5, 5), (-7, 6), (6, -8), (-8, -7),
        (10, 7), (-9, 9), (9, -9), (-5, -5),
        (4, 8), (-8, 4)
    ]
    i = 0
    for k, (x, y) in points.items():
        ox, oy = offsets[i % len(offsets)]
        txt(x + ox, y + oy, k)
        i += 1

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def start():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"House with Midpoint Line Algorithm")
    glutDisplayFunc(show)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
    glutMainLoop()

if __name__ == "__main__":
    start()
