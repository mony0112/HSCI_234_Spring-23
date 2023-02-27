import js
p5 = js.window

x = 150
y = 150
size = p5.random(50, 100)
random_size2 = p5.random(25, 125)
random_size3 = p5.random(25, 125)
random_size4 = p5.random(25, 125)



def setup():
    p5.createCanvas(300, 300)
    print('finished setup')


def draw():
    p5.background(255)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)


    # Question 1
    random_size = p5.random(25, 125)
    p5.text(random_size, 10, 30)
    
    global x
    global y
    global size
    
    size = p5.random(50, 100)
    p5.push()
    p5.translate(x, y)
    random_square(size)
    p5.pop()


    # Question 2
    a = p5.random(0, p5.width - random_size)
    b = p5.random(0, p5.height - random_size)


    p5.line(a, b, a + random_size, b)
    p5.line(a + random_size, b, a + random_size, b + random_size)
    p5.line(a + random_size, b + random_size, a, b + random_size)
    p5.line(a, b + random_size, a, b)


    # Question 6
    # random_square(x, y, size)


    global random_size2
    global random_size3
    global random_size4


    p5.push()
    p5.translate(20, 20)
    p5.stroke(127, 0, 255)
    random_square_at(0, 0, random_size)
    p5.pop()


    p5.push()
    p5.translate(p5.width - 20, 20)
    p5.stroke(255, 127, 54)
    random_square_at(0, 0, random_size2)
    p5.pop()


    p5.push()
    p5.translate(p5.width - 20, p5.height - 20)
    p5.stroke(127, 200, 0)
    random_square_at(0, 0, random_size3)
    p5.pop()


    p5.push()
    p5.translate(20, p5.height - 20)
    p5.stroke(255, 0, 127)
    random_square_at(0, 0, random_size4)
    p5.pop()


#question 7
    if p5.mouseIsPressed: 
        p5.push()
        p5.translate(20, p5.height - 20)
        p5.stroke(255,0,127)
        random_square_at(0, 0, random_size4)
        p5.pop()
#question 3
def random_square(x, y, size):
    p5.rect(x - size / 2, y - size / 2, size, size)


#question 5
def random_square_at(x, y, size):
    p5.rect(x - size / 2, y - size / 2, size, size)

