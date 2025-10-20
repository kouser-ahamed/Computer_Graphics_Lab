from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_12

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def txt(x, y, s):
    glRasterPos2f(x, y)
    for ch in s:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        return
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    glBegin(GL_POINTS)
    for _ in range(int(steps) + 1):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(1.0, 0.5, 0.2)

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

    draw_line(260, 355, 160, 255)
    draw_line(260, 355, 360, 255)
    draw_line(260, 355, 460, 355)
    draw_line(360, 255, 560, 255)
    draw_line(460, 355, 560, 255)
    draw_line(270, 345, 185, 255)
    draw_line(160, 255, 185, 255)
    draw_line(535, 180, 535, 255)
    draw_line(360, 255, 360, 155)
    draw_line(185, 255, 185, 180)
    draw_line(185, 180, 360, 155)
    draw_line(360, 155, 535, 180)
    draw_line(420, 230, 470, 230)
    draw_line(420, 230, 420, 165)
    draw_line(470, 230, 470, 170)
    draw_line(235, 230, 285, 230)
    draw_line(235, 230, 235, 175)
    draw_line(285, 230, 285, 170)
    draw_line(415, 355, 415, 410)
    draw_line(445, 355, 445, 410)
    draw_line(415, 410, 445, 410)

    glColor3f(1, 1, 1)
    offset_positions = [
        (5, 5), (-7, 6), (6, -8), (-8, -7),
        (10, 7), (-9, 9), (9, -9), (-5, -5),
        (4, 8), (-8, 4)
    ]
    i = 0
    for k, (x, y) in points.items():
        ox, oy = offset_positions[i % len(offset_positions)]
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
    glutCreateWindow(b"House with Alphabet Points on Black Background")
    glutDisplayFunc(show)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
    glutMainLoop()

if __name__ == "__main__":
    start()
