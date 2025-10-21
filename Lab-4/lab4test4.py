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
                 y = y - 1
        else:
            d = d + 2 * (x - y) + 5
            
        x = x + 1

        Circlepoints(x, y, x0, y0)
    
def Circlepoints(x, y, x0, y0):


    draw_points(x + x0, y + y0)
    draw_points(y + y0, x + x0)
    draw_points(y + y0, -x + x0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + y0, -x + x0)
    draw_points(-y + y0, x + x0)
    draw_points(-x + x0, y + y0)




def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    x = 250
    y = 250
    radius = 150
    
    x1=250+75
    y1=250
    
    x2=250
    y2=250+75
    
    x3=250-75
    y3=250
    
    x4=250
    y4=250-75
    
    x5=250+53
    y5=250+53    
    x6=250-53
    y6=250+53
    
    x7=250-53
    y7=250-53
    
    x8=250+53
    y8=250-53
    
    
    MidpointCircle(radius, x, y)
    MidpointCircle(75,x1,y1)
    MidpointCircle(75,x2,y2)
    MidpointCircle(75,x3,y3)
    MidpointCircle(75,x4,y4)
    MidpointCircle(75,x5,y5)
    MidpointCircle(75,x6,y6)
    MidpointCircle(75,x7,y7)
    MidpointCircle(75,x8,y8)
    
    
    
   
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)


glutMainLoop()