from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
from random import *
from numpy import *

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
corBase = ((1, 1, 1))
corTopo = ((0.5, 0.5, 0.5))

x = 0
y = 0
z = 0
pontos = []
r = 10
i = 0
l = 3
o = -0.5
p = 0

# for o in arange(-0.5, 0.5, 0.01):
while (o < 0.5):
    p = 0
    # for p in arange(0, 2, 0.02):
    while (p < 2):
        x = r * cos(pi * o) * cos(pi * p)
        y = r * sin(pi * o)
        z = r * cos(pi * o) * sin(pi * p)
        pontos.insert(i, (x, y, z))
        i += 1
        p += 0.2 / l
    o += 0.1 / l


def rev():
    glBegin(GL_TRIANGLES)
    for i in range(0, len(pontos)):
        if i >= len(pontos) - ((10 * l) + 1):
            break

        glColor3f(0.5, 1, 1)
        # glVertex3fv(pontos[i*l], pontos[i+(1*l)], pontos[i+(10*l)])
        # glVertex3fv(pontos[i+(10*l)], pontos[i+(11*l)], pontos[i+(1*l)])

        glVertex3fv(pontos[i])
        glVertex3fv(pontos[i + 1])
        glVertex3fv(pontos[i + (10 * l)])
        glColor3f(0.5, 0.5, 1)
        glVertex3fv(pontos[i + (10 * l)])
        glVertex3fv(pontos[i + ((10 * l) + 1)])
        glVertex3fv(pontos[i + 1])
    glEnd()


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    rev()
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1000, 1000)
glutCreateWindow("Rev")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(100, 800.0 / 800.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -20)
glRotatef(45, 0, 0, 0)
glutTimerFunc(100, timer, 1)
glutMainLoop()