from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MidpointCircle(radius, x0, y0):
    x = 0
    y = radius
    d = 1 - radius
    
    Circlepoints(x, y, x0, y0)
    
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        
        Circlepoints(x, y, x0, y0)

def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)

    x = 250
    y = 250
    x1 = 250 + 75
    y1 = 250
    x2 = 250 - 75
    y2 = 250
    x3 = 250
    y3 = 250 + 75
    x4 = 250
    y4 = 250 - 75

    MidpointCircle(150, x, y)
    MidpointCircle(75, x1, y1)
    MidpointCircle(75, x2, y2)
    MidpointCircle(75, x3, y3)
    MidpointCircle(75, x4, y4)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Midpoint Circle Pattern - 1 Large + 4 Small (No Axis)")
glutDisplayFunc(showScreen)
glutMainLoop()
