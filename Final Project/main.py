import js
p5 = js.window

arr = []

class Pepper():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.img = p5.loadImage('pepper.jpg')
        
    def draw(self):
        p5.push()  # Save the current transformation state
        scaleX = p5.width / self.img.width
        scaleY = p5.height / self.img.height
        p5.scale(scaleX, scaleY)  # Scale the image based on the ratio of canvas size to image size
        p5.image(self.img, self.x, self.y)  # Draw the image
        p5.pop()  # Restore the transformation state
            

class State1(Pepper):
    def draw_dots(self, num_dots = 10, dot_size = 10):
        scaleX = p5.width / self.img.width
        scaleY = p5.height / self.img.height
    
        for i in range(num_dots):
            x = p5.random(0, self.img.width) * scaleX
            y = p5.random(0, self.img.height) * scaleY
            color = self.img.get(int(x / scaleX), int(y / scaleY))
            p5.fill(color)
            p5.noStroke()
            # p5.ellipse(x, y, dot_size, dot_size)
            arr.append({'x': x, 'y': y, 'color': color})

        for item in arr:

            if p5.mouseX - 50 < item['x'] < p5.mouseX + 50 and p5.mouseY - 50 < item['y'] < p5.mouseY + 50:
                continue

            p5.stroke('#FF3FB4')
            p5.strokeWeight(2)
            p5.noFill()
            p5.rect(p5.mouseX - 50, p5.mouseY - 50, 50, 50)


            p5.fill(item['color'])           
            p5.noStroke()
            p5.ellipse(item['x'], item['y'], dot_size, dot_size)
            
class State2(Pepper):
    def draw_dots(self, num_dots=10, dot_size=10):
        scaleX = p5.width / self.img.width
        scaleY = p5.height / self.img.height
        
        for i in range(num_dots):
            x = p5.random(0, self.img.width) * scaleX
            y = p5.random(0, self.img.height) * scaleY
            color = self.img.get(int(x / scaleX), int(y / scaleY))
            
            # Change color based on mouse position
            dist = p5.dist(x, y, p5.mouseX, p5.mouseY)
            if dist < 20:
                color = p5.color('#FF3FB4')
                
            p5.fill(color)
            p5.noStroke()
            arr.append({'x': x, 'y': y, 'color': color})
        
        for item in arr:
            p5.fill(item['color'])
            p5.noStroke()
            p5.ellipse(item['x'], item['y'], dot_size, dot_size)

        p5.fill('#FF3FB4')
        p5.noStroke()
        p5.ellipse(p5.mouseX, p5.mouseY, 10, 10)
        
class State3(Pepper):
    def draw_dots(self, num_dots=100, dot_size=10):
        scaleX = p5.width / self.img.width
        scaleY = p5.height / self.img.height

        for i in range(num_dots):
            x = p5.random(0, self.img.width) * scaleX
            y = p5.random(0, self.img.height) * scaleY
            color = self.img.get(int(x / scaleX), int(y / scaleY))

            # Change size and rotation based on distance from mouse position
            dist = p5.dist(x, y, p5.mouseX, p5.mouseY)
            size = p5.map(dist, 0, p5.width, dot_size, 0)
            angle = p5.map(dist, 0, p5.width, 0, p5.TWO_PI)
            p5.push()
            p5.translate(x, y)
            p5.rotate(angle)
            p5.noStroke()
            p5.fill(color)
            p5.ellipse(0, 0, size, size)
            p5.pop()

            # Change color based on y position
            if y < p5.height / 3:
                color = p5.color('#FF3FB4')
            elif y < 2 * p5.height / 3:
                color = p5.color('#4A90E2')
            else:
                color = p5.color('#51B46D')
            arr.append({'x': x, 'y': y, 'color': color})

        for item in arr:
            if p5.mouseX - 50 < item['x'] < p5.mouseX + 50 and p5.mouseY - 50 < item['y'] < p5.mouseY + 50:
                continue

            p5.stroke('#FF3FB4')
            p5.strokeWeight(2)
            p5.noFill()
            p5.rect(p5.mouseX - 50, p5.mouseY - 50, 50, 50)


            p5.fill(item['color'])           
            p5.noStroke()
            p5.ellipse(item['x'], item['y'], dot_size, dot_size)

    
pepper = Pepper()
pepper1 = State1()
pepper2 = State2()
pepper3 = State3()

def setup():
    p5.createCanvas(300, 300) 
    p5.frameRate(50)
    print('finished setup') 
    
def draw():
    # p5.background(255)           
    pepper.draw()

    if (p5.keyIsPressed):
        if (p5.key == '1'):
            pepper1.draw_dots()
        elif (p5.key == '2'):
            pepper2.draw_dots()
        elif (p5.key == '3'):
            pepper3.draw_dots()
    else:
        p5.background(255)

    
def keyPressed(event):
    pass 


def keyReleased(event):
    pass
    
def mousePressed(event):
    pass
    
def mouseReleased(event):
    pass
