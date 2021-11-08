function run () {
    if (direction == "right") {
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        X += 1
        if (X > 4) {
            X = 0
        }
        led.plotBrightness(X2, Y2, bridg - 90)
        led.plotBrightness(X1, Y1, bridg - 45)
        led.plotBrightness(X, Y, bridg)
    }
    if (direction == "above") {
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        Y += -1
        if (Y < 0) {
            Y = 4
        }
        led.plotBrightness(X2, Y2, bridg - 90)
        led.plotBrightness(X1, Y1, bridg - 45)
        led.plotBrightness(X, Y, bridg)
    }
    if (direction == "left") {
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        X += -1
        if (X < 0) {
            X = 4
        }
        led.plotBrightness(X2, Y2, bridg - 90)
        led.plotBrightness(X1, Y1, bridg - 45)
        led.plotBrightness(X, Y, bridg)
    }
    if (direction == "down") {
        led.unplot(X2, Y2)
        X2 = X1
        X1 = X
        Y2 = Y1
        Y1 = Y
        Y += 1
        if (Y > 4) {
            Y = 0
        }
        led.plotBrightness(X2, Y2, bridg - 90)
        led.plotBrightness(X1, Y1, bridg - 45)
        led.plotBrightness(X, Y, bridg)
    }
}
input.onButtonPressed(Button.A, function () {
    if (direction == "right") {
        direction = "above"
    } else if (direction == "above") {
        direction = "left"
    } else if (direction == "left") {
        direction = "down"
    } else {
        direction = "right"
    }
    if (direction == "") {
        direction = "above"
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    paus = !(paus)
    if (paus == true) {
        led.plotBrightness(X2, Y2, bridg - 90)
        led.plotBrightness(X1, Y1, bridg - 45)
        led.plotBrightness(X, Y, bridg)
        randPoint()
    } else {
        direction = ""
        basic.showString("" + (points))
    }
})
input.onButtonPressed(Button.B, function () {
    if (direction == "right") {
        direction = "down"
    } else if (direction == "down") {
        direction = "left"
    } else if (direction == "left") {
        direction = "above"
    } else {
        direction = "right"
    }
    if (direction == "") {
        direction = "right"
    }
})
function randPoint () {
    eatY = randint(0, 4)
    eatX = randint(0, 4)
    if (eatX == X || (eatX == X1 || eatX == X2) || (eatY == Y || (eatY == Y1 || eatY == Y2))) {
        randPoint()
    } else {
        led.plotBrightness(eatX, eatY, 100)
    }
}
let eatX = 0
let eatY = 0
let paus = false
let Y2 = 0
let Y1 = 0
let Y = 0
let X2 = 0
let X1 = 0
let X = 0
let direction = ""
let bridg = 0
let points = 0
basic.showString("SNAKE")
points = 0
bridg = 100
let score = 1000
direction = ""
X = 2
X1 = 1
X2 = 0
Y = 4
Y1 = 4
Y2 = 4
basic.showString("" + (points))
basic.forever(function () {
    if (paus == true) {
        basic.pause(score)
        run()
        if (X == eatX && Y == eatY) {
            randPoint()
            points += 1
            score += -10
        }
    }
})
