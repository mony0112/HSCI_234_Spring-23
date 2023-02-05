import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(0)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

    #leaves
    for i in range(6):
        x = 20 + i * 50
        y = 20 + i * 50
        p5.fill(255, 102, 178, 50)
        p5.triangle(x, y, x + 25, y, x + 12.5, y + 25)
    for i in range(6):
        x = 10 + i * 50
        y = 70 + i * 50
        p5.fill(255, 102, 178, 50)
        p5.triangle(x, y, x + 20, y, x + 7.5, y + 20)

    for i in range(6):
        x = 10 + i * 50
        y = 130 + i * 50
        p5.fill(255, 102, 178, 50)
        p5.triangle(x, y, x + 15, y, x + 2.5, y + 15)

    for i in range(6):
        x = 10 + i * 40
        y = 200 + i * 40
        p5.fill(255, 102, 178, 50)
        p5.triangle(x, y, x + 10, y, x, y + 10)

    for i in range(3):
        x = 10 + i * 20
        y = 270 + i * 20
        p5.fill(255, 102, 178, 50)
        p5.triangle(x, y, x + 5, y, x, y + 5)

    #head

    p5.strokeWeight(2)
    p5.stroke(255,102,178)
    p5.fill(255,102,178,50)
    a = 100
    b = 150
    p5.quad(a,b,a+100,b,a+70,b+80,a+30, b+80)

    p5.strokeWeight(2)
    p5.stroke(255,0,127)
    p5.fill(0,0,127,50)
    x = 120
    y = 165
    p5.quad(x,y,x+60,y,x+40,y+50,x+20,y+50)

    #ear
    p5.strokeWeight(2)
    p5.fill(240,240,127,50)
    p5.stroke(0,204,204)
    p5.quad(100,150,70,80,100,50,135,150)
    p5.quad(170,150,180,50,220,80,200,150)

    #mouth
    p5.strokeWeight(2)
    p5.fill(0,240,240,50)
    p5.stroke(0,102,102)
    p5.rect(130,230,40,40)

    #sideface
    p5.strokeWeight(2)
    p5.fill(255,204,153)
    p5.stroke(255,102,178)
    p5.triangle(100,150,130,230,80,190)
    p5.triangle(170,230,200,150,220,190)

    #cheek
    p5.strokeWeight(2)
    p5.fill(255,102,255,80)
    p5.stroke(255,153,51)
    p5.quad(80,190,130,230,130,270,55,245)
    p5.quad(170,230,220,190,240,245,170,270)
