from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def draw_points(x, y):
    glVertex2i(int(x), int(y))

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    glBegin(GL_POINTS)
    
    while x <= y:
    
        draw_points(xc + x, yc + y)
        draw_points(xc - x, yc + y)
        draw_points(xc + x, yc - y)
        draw_points(xc - x, yc - y)
        draw_points(xc + y, yc + x)
        draw_points(xc - y, yc + x)
        draw_points(xc + y, yc - x)
        draw_points(xc - y, yc - x)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3.0)
    glColor3f(0, 1, 0)

    # Large 
    midpoint_circle(250, 250, 150)

    # 4 smaller
    midpoint_circle(250 + 75, 250, 75)   
    midpoint_circle(250 - 75, 250, 75)   
    midpoint_circle(250, 250 + 75, 75)   
    midpoint_circle(250, 250 - 75, 75)
     

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
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"Midpoint Circle Pattern - Inner Circles (No Axis)")
    glutDisplayFunc(show)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    start()
