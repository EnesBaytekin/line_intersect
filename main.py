import pygame
import pygame.display
import pygame.event
import pygame.draw
import pygame.mouse

screen = pygame.display.set_mode( (320, 180) , pygame.SCALED )

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        return (self.x, self.y)

class Line:
    def __init__(self, a:Point, b:Point):
        self.points = [a, b]
    def is_intersect(self, line):
        a, b = self.points
        c, d = line.points
        oc = (a.y-b.y) * (c.x-a.x) - (a.x-b.x) * (c.y-a.y)
        od = (a.y-b.y) * (d.x-a.x) - (a.x-b.x) * (d.y-a.y)
        if (oc < 0) and (od < 0): return False
        if (oc > 0) and (od > 0): return False
        oa = (c.y-d.y) * (a.x-c.x) - (c.x-d.x) * (a.y-c.y)
        ob = (c.y-d.y) * (b.x-c.x) - (c.x-d.x) * (b.y-c.y)
        if (oa < 0) and (ob < 0): return False
        if (oa > 0) and (ob > 0): return False
        return True

class Rect:
    def __init__(self, x, y, w, h):
        self.lines = [
            Line(Point(x  , y)  ,   Point(x+w,  y  )),
            Line(Point(x+w, y)  ,   Point(x+w,  y+h)),
            Line(Point(x+w, y+h),   Point(x  ,  y+h)),
            Line(Point(x  , y+h),   Point(x  ,  y  )),
        ]
    def collide_line(self, line:Line):
        for _line in self.lines:
            if line.is_intersect(_line):
                return True
        return False

line = Line(Point(0,0), Point(0,0))
rect = Rect(100, 50, 100, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                line.points[0] = Point(mx, my)
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        mx, my = pygame.mouse.get_pos()
        line.points[1] = Point(mx, my)
    screen.fill((192, 192, 192))
    if rect.collide_line(line):
        color = (192, 0, 0)
    else:
        color = (0, 0, 0)
    pygame.draw.polygon(screen, color, [line.points[0].get() for line in rect.lines], 1)
    pygame.draw.line(screen, color, *[point.get() for point in line.points])
    pygame.display.flip()
