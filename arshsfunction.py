#function file
def tree(t):
    for times in range (20):
        c=(139,64,19)
        t.color(c)
        polygon(t,4,5)
        t.forward(1)

def tree0(t, size):
    t.forward(size)

def tree1(t, size):
    for angle in [60, -120, 60, 0]:
       tree0(t, size/3)
       t.left(angle)

def tree2(t, size):
    for angle in [60, -120, 60, 0]:
       tree1(t, size/3)
       t.left(angle)

def tree3(t, size):
    for angle in [60, -120, 60, 0]:
       tree2(t, size/3)
       t.left(angle)

def tree4(t,size):
    for angle in [60,-120,60,0]:
        tree3(t,size/2)
        t.left(angle)
def tree5(t,size):
    for angle in [60,-120,60,0]:
        tree3(t,size/4)
        t.left(angle)
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
