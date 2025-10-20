from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def midpoint_circle(x_centre, y_centre, r):
    x = r
    y = 0
    points = []

    points.append((x + x_centre, y + y_centre))
    if r > 0:
        points.append((x + x_centre, -y + y_centre))
        points.append((y + x_centre, x + y_centre))
        points.append((-y + x_centre, x + y_centre))

    P = 1 - r

    while x > y:
        y += 1
        if P <= 0:
            P = P + 2*y + 1
        else:
            x -= 1
            P = P + 2*y - 2*x + 1

        if x < y:
            break

        points.append((x + x_centre, y + y_centre))
        points.append((-x + x_centre, y + y_centre))
        points.append((x + x_centre, -y + y_centre))
        points.append((-x + x_centre, -y + y_centre))

        if x != y:
            points.append((y + x_centre, x + y_centre))
            points.append((-y + x_centre, x + y_centre))
            points.append((y + x_centre, -x + y_centre))
            points.append((-y + x_centre, -x + y_centre))

    glBegin(GL_POINTS)
    for px, py in points:
        glVertex2f(px, py)
    glEnd()

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(1.0, 0, 0)

    midpoint_circle(400, 300, 50)
    midpoint_circle(200, 150, 75)
    midpoint_circle(600, 450, 30)

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
    glutCreateWindow(b"Midpoint Circle Drawing Algorithm")
    glutDisplayFunc(show)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    start()
