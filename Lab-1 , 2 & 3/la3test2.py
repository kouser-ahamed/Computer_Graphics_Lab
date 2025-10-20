from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600





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
    glColor3f(0, 1.0, 0)

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
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    start()
