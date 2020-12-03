#!/usr/bin/python

import math
import cairo

f = open("./input", "r")
c = f.read()
f.close()

lines = c.split("\n")
lines.pop()
w = len(lines[0]) - 1

def trees(down, right):
    curx = 0
    cury = 0
    trees = 0

    while cury < len(lines) - 1:
        line = lines[cury]
        if curx > w:
            curx -= (w+1)
        if(line[curx] == "#"):
            #print ("oh a tree at ", cury, curx)
            trees += 1
        curx += right
        cury += down

    print(trees, "trees for ", down, right)

#t1 = trees(1,1)
#t2 = trees(1,3)
#t3 = trees(1,5)
#t4 = trees(1,7)
#t5 = trees(2,1)

#h = len(lines)
w = 10
h = 10

width, height = w*30, h*30



uw = 1./w
uh = 1./h

def draw_grid():
    print(uw, uh, w)
    ctx.set_line_width(0.001)
    ctx.set_source_rgba(0,0,0,0.5)  # Solid color, 50% opacity
    #ctx.translate(0.1, 0.1)  # Changing the current transformation matrix
    i = 0
    while i < w:
        ctx.move_to(i*uw, 0)
        ctx.line_to(i*uw, 1) # vertical line
        i += 1
        ctx.stroke()
    i = 0
    while i < len(lines):
        ctx.move_to(0, i*uh)
        #ctx.line_to(1, i*uh) # horiz line
        i += 1
        #ctx.stroke()

def draw_tree(x,y):
    #ctx.move_to(x*uw + uw/2, y*uh + uh/2)
    #ctx.set_line_width(0.001)
    ctx.move_to(x*uw+ uw/2, y*uh + uh/16) # tree top
    ctx.rel_line_to(-uw/4, 3*uh/4)
    ctx.rel_line_to(+uw/2, 0)
    ctx.close_path()
    #ctx.rectangle(x*uw + uw/2 - uw/16, y*uh + uh/4, uw/8, uh/2)  # Rectangle(x0, y0, w, h
    #ctx.arc(x*uw + uw/2, y*uh + uh/2, uw, -math.pi / 2, 0)
    ctx.set_source_rgb(0,1,0.5)  # Solid color
    ctx.fill()



surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

ctx.scale(width, height)  # Normalizing the canvas

ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(1,1,1)  # Solid color
ctx.fill()

# Arc(cx, cy, radius, start_angle, stop_angle)
#ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
#ctx.line_to(0.5, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
#ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
#ctx.close_path()


ctx.translate(0, 0)  # Changing the current transformation matrix
ctx.move_to(0, 0)


draw_grid()
draw_tree(0,0) # x,y
draw_tree(0,1)
draw_tree(1,0)
draw_tree(2,2)


surface.write_to_png("img/example.png")  # Output to PNG
