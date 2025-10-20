from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

W = 800
H = 600

def drawLine(xa, ya, xb, yb):
    dx = xb - xa
    dy = yb - ya
    m = dy / dx if dx != 0 else None
    p = []

    if abs(dx) >= abs(dy):
        if xa > xb:
            xa, xb = xb, xa
            ya, yb = yb, ya
        x, y = xa, ya
        while x <= xb:
            p.append((round(x), round(y)))
            x += 1
            if m is not None:
                y += m
    else:
        if ya > yb:
            xa, xb = xb, xa
            ya, yb = yb, ya
        x, y = xa, ya
        inv = 1 / m if (m is not None and m != 0) else 0
        while y <= yb:
            p.append((round(x), round(y)))
            y += 1
            if m is not None:
                x += inv

    glPointSize(4)
    glBegin(GL_POINTS)
    for a, b in p:
        glVertex2f(a, b)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for a, b in p:
        glVertex2f(a, b)
    glEnd()

def txt(x, y, s):
    glRasterPos2f(x + 0.3, y + 0.3)
    for ch in s:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.2, 1, 0.6)

    drawLine(5, 5, 13, 5)
    drawLine(13, 5, 13, 13)
    drawLine(13, 13, 5, 13)
    drawLine(5, 13, 5, 5)

    drawLine(3, 7, 11, 7)
    drawLine(11, 7, 11, 15)
    drawLine(11, 15, 3, 15)
    drawLine(3, 15, 3, 7)

    drawLine(5, 5, 3, 7)
    drawLine(13, 5, 11, 7)
    drawLine(13, 13, 11, 15)
    drawLine(5, 13, 3, 15)

    glColor3f(1, 1, 1)
    pts = {
        "A": (5, 5),
        "B": (13, 5),
        "C": (13, 13),
        "D": (5, 13),
        "E": (3, 7),
        "F": (11, 7),
        "G": (11, 15),
        "H": (3, 15)
    }
    for k, (x, y) in pts.items():
        txt(x, y, f"{k}({x},{y})")

    glutSwapBuffers()

def reshape2D(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 20, 0, 20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def start():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"Cube_Projection_View")
    glutDisplayFunc(render)
    glutReshapeFunc(reshape2D)
    glClearColor(0, 0, 0, 1)

def run():
    start()
    glutMainLoop()

if __name__ == "__main__":
    run()
