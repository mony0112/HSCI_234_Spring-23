import js
p5 = js.window


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
        #p5.image(self.img, self.x, self.y)  # Draw the image
        p5.pop()  # Restore the transformation state
        
    def draw_dots(self, num_dots = 10, dot_size = 10):
        scaleX = p5.width / self.img.width
        scaleY = p5.height / self.img.height
    
        for i in range(num_dots):
            x = p5.random(0, self.img.width) * scaleX
            y = p5.random(0, self.img.height) * scaleY
            color = self.img.get(int(x / scaleX), int(y / scaleY))
            p5.fill(color)
            p5.noStroke()
            p5.ellipse(x, y, dot_size, dot_size)


pepper = Pepper()


def setup():
    p5.createCanvas(800, 1000) 
    p5.frameRate(50)
    print('finished setup') 
    
def draw():
    # p5.background(255)           
    pepper.draw()
    pepper.draw_dots()
    
def keyPressed(event):
    pass 


def keyReleased(event):
    pass
    
def mousePressed(event):
    pass


def mouseReleased(event):
    pass
