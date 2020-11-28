from cmu_112_graphics import *

def appStarted(app):
    app.level = 0
    app.colors = ['red', 'orange', 'gold', 'lime','green', 'light blue', 'blue','purple', 'magenta', 'violetred', 'black', 'brown']

def drawSierpinskiTriangle(app, canvas, level, x, y, size):
    if level == 0:
        topY = y - (size**2 - (size/2)**2)**0.5
        color = app.colors[app.level]
        canvas.create_polygon(x, y, x+size, y, x+size/2, topY, fill=color)
    else:
        drawSierpinskiTriangle(app, canvas, level-1, x, y, size/2)
        drawSierpinskiTriangle(app, canvas, level-1, x+size/2, y, size/2)
        midY = y - ((size/2)**2 - (size/4)**2)**0.5
        drawSierpinskiTriangle(app, canvas, level-1, x+size/4, midY, size/2)

def keyPressed(app, event):
    if event.key in ['Up', 'Right']:
        app.level += 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1

def redrawAll(app, canvas):
    margin = min(app.width, app.height)//10
    x, y = margin, app.height-margin
    size = min(app.width, app.height) - 2*margin
    drawSierpinskiTriangle(app, canvas, app.level, x, y, size)
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')

runApp(width=1000, height=1000)