def run():
    global X2, X1, Y2, Y1, X, Y
    if direction == "right":
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        X += 1
        if X > 4:
            X = 0
        led.plot_brightness(X2, Y2, bridg - 90)
        led.plot_brightness(X1, Y1, bridg - 45)
        led.plot_brightness(X, Y, bridg)
    if direction == "above":
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        Y += -1
        if Y < 0:
            Y = 4
        led.plot_brightness(X2, Y2, bridg - 90)
        led.plot_brightness(X1, Y1, bridg - 45)
        led.plot_brightness(X, Y, bridg)
    if direction == "left":
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        X += -1
        if X < 0:
            X = 4
        led.plot_brightness(X2, Y2, bridg - 90)
        led.plot_brightness(X1, Y1, bridg - 45)
        led.plot_brightness(X, Y, bridg)
    if direction == "down":
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        Y += 1
        if Y > 4:
            Y = 0
        led.plot_brightness(X2, Y2, bridg - 90)
        led.plot_brightness(X1, Y1, bridg - 45)
        led.plot_brightness(X, Y, bridg)

def on_button_pressed_a():
    global direction
    if direction == "right":
        direction = "above"
    elif direction == "above":
        direction = "left"
    elif direction == "left":
        direction = "down"
    else:
        direction = "right"
    if direction == "":
        direction = "above"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global paus, direction
    basic.clear_screen()
    paus = not (paus)
    if paus == True:
        led.plot_brightness(X2, Y2, bridg - 90)
        led.plot_brightness(X1, Y1, bridg - 45)
        led.plot_brightness(X, Y, bridg)
        randPoint()
    else:
        direction = ""
        basic.show_string("" + str((points)))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global direction
    if direction == "right":
        direction = "down"
    elif direction == "down":
        direction = "left"
    elif direction == "left":
        direction = "above"
    else:
        direction = "right"
    if direction == "":
        direction = "right"
input.on_button_pressed(Button.B, on_button_pressed_b)

def randPoint():
    global eatY, eatX
    eatY = randint(0, 4)
    eatX = randint(0, 4)
    if eatX == X or (eatX == X1 or eatX == X2) or (eatY == Y or (eatY == Y1 or eatY == Y2)):
        randPoint()
    else:
        led.plot_brightness(eatX, eatY, 100)
eatX = 0
eatY = 0
Y2 = 0
Y1 = 0
Y = 0
X2 = 0
X1 = 0
X = 0
direction = ""
bridg = 0
points = 0
basic.show_string("SNAKE")
points = 0
bridg = 100
score = 1000
paus = False
direction = ""
X = 2
X1 = 1
X2 = 0
Y = 4
Y1 = 4
Y2 = 4
basic.show_string("" + str((points)))

def on_forever():
    global points, score
    if paus == True:
        basic.pause(score)
        run()
        if X == eatX and Y == eatY:
            randPoint()
            points += 1
            score += -10
basic.forever(on_forever)
