import js
p5 = js.window

class Sky1():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.img1 = p5.loadImage('sky_1.jpg')
        
    def draw(self):
        p5.push()  # Save the current transformation state
        scaleX = p5.width / self.img1.width
        scaleY = p5.height / self.img1.height
        p5.scale(scaleX, scaleY)  # Scale the image based on the ratio of canvas size to image size
        p5.image(self.img1, self.x, self.y)  # Draw the image
        p5.pop()  # Restore the transformation state
        
    def draw_dots(self, num_dots = 200, dot_size = 15):
        scaleX = p5.width / self.img1.width
        scaleY = p5.height / self.img1.height
    
        for i in range(num_dots):
            x = p5.random(0, self.img1.width) * scaleX
            y = p5.random(0, self.img1.height) * scaleY
            color = self.img1.get(int(x / scaleX), int(y / scaleY))
            p5.fill(color)
            p5.noStroke()
            p5.ellipse(x, y, dot_size, dot_size)

sky1 = Sky1()

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)           
    sky1.draw()
    sky1.draw_dots()
    
def keyPressed(event):
    pass 

def keyReleased(event):
    pass
    
def mousePressed(event):
    pass

def mouseReleased(event):
    pass

