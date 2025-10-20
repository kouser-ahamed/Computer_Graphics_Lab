from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

W = 800
H = 600

def midLine(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x, y = x1, y1
    pts = []

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            pts.append((x, y))
            x += sx
            if p >= 0:
                y += sy
                p -= 2 * dx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            pts.append((x, y))
            y += sy
            if p >= 0:
                x += sx
                p -= 2 * dy
            p += 2 * dx

    glPointSize(4)
    glBegin(GL_POINTS)
    for a, b in pts:
        glVertex2f(a, b)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for a, b in pts:
        glVertex2f(a, b)
    glEnd()

def drawText(x, y, text):
    glRasterPos2f(x + 0.3, y + 0.3)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0.7, 0.2)

    midLine(5, 5, 13, 5)
    midLine(13, 5, 13, 13)
    midLine(13, 13, 5, 13)
    midLine(5, 13, 5, 5)

    midLine(3, 7, 11, 7)
    midLine(11, 7, 11, 15)
    midLine(11, 15, 3, 15)
    midLine(3, 15, 3, 7)

    midLine(5, 5, 3, 7)
    midLine(13, 5, 11, 7)
    midLine(13, 13, 11, 15)
    midLine(5, 13, 3, 15)

    glColor3f(1, 1, 1)
    v = {
        "A": (5, 5),
        "B": (13, 5),
        "C": (13, 13),
        "D": (5, 13),
        "E": (3, 7),
        "F": (11, 7),
        "G": (11, 15),
        "H": (3, 15)
    }
    for k, (x, y) in v.items():
        drawText(x, y, f"{k}({x},{y})")

    glutSwapBuffers()

def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 20, 0, 20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def setup():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"Cube using Midpoint Line Algorithm")
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glClearColor(0, 0, 0, 1)

def main():
    setup()
    glutMainLoop()

if __name__ == "__main__":
    main()
