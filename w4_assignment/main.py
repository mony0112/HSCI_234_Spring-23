import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background("#B0E0E6")
    hair()
    face()
    neck()
    leftsidehair()
    rightsidehair()
    body()
    cheeks()
    mouth()
    eyes()

    #draw orange flower
    orange_flower(x=60,y=240)
    # draw another orangeflower at smaller scale:
    p5.push()
    p5.translate(180, 240)  # move coordinates
    p5.scale(0.50)  # then scale
    orange_flower(x = 0, y = 0)  # draw at origin (0, 0)
    p5.pop()
    
    #draw pink flower
    pink_flower(x=270,y=200)
    # draw another pink flower at smaller scale:
    p5.push()
    p5.translate(110, 264)  # move coordinates
    p5.scale(0.50)  # then scale
    pink_flower(x = 0, y = 0)  # draw at origin (0, 0)
    p5.pop()

    #draw blue flowers randomwly
    for i in range(5): 
        x = p5.random(0, 300)
        y = p5.random(200, 300)
        blue_flower(x = 0, y = 0)

    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

def blue_flower(x, y):
    p5.push()
    p5.translate(x, y)
    for i in range(15):
        p5.noStroke()
        p5.fill("#1E90FF")
        p5.rotate(p5.radians(30)) 
        petal()
    p5.pop()
    
def pink_flower(x,y):
     p5.push()
     p5.translate(x, y);
     for i in range (15):
         p5.noStroke()
         p5.fill("#E24FAC")
         p5.rotate(p5.radians(30)) 
         petal()
     p5.pop()
    
def orange_flower(x,y):
     p5.push()
     p5.translate(x, y);
     for i in range (15):
         p5.noStroke()
         p5.fill("#FFAA1D")
         p5.rotate(p5.radians(30)) 
         petal()
     p5.pop()

def petal():
    p5.ellipse(50, 0, 65, 25)

   
def eyes ():
    p5.fill("#10104c")
    p5.noStroke()
    p5.ellipse(130,120,10,(p5.mouseY)/10)
    p5.ellipse(170,120,10,(p5.mouseY)/10)
    
def mouth():
    p5.fill("#f370cc")
    p5.noStroke()
    p5.ellipse(150,150,15,(p5.mouseX)/15)

def cheeks():
    p5.fill("#ff5f74")
    p5.noStroke()
    p5.ellipse(130,140,10,10)
    p5.ellipse(170,140,10,10)
def hair():
    p5.fill("#10104c")
    p5.noStroke()
    p5.ellipse(150, 120, 100, 120)
    p5.quad(105,110,197,110,220,180,75,180)
    
def face():
    p5.noStroke()
    p5.fill("#E4B1AB")
    p5.circle(150,120,80)
    
def leftsidehair():
    p5.fill("#10104c")
    p5.noStroke()
    p5.quad(141,66,150,75,108,130,108,105)
    
def rightsidehair():
    p5.fill("#10104c")
    p5.noStroke()
    p5.quad(145,80,164,70,197,112,193,128)

def neck():
    p5.noStroke()
    p5.fill("#E4B1AB")
    p5.quad(138,155,159,155,160,180,135,180)

def body():
    p5.noStroke()
    p5.fill("#E4B1AB")
    p5.quad(135,180,161,211,78,263,70,200)
    p5.quad(161,180,217,206,212,263,113,263)
    p5.quad(135,180,161,180,113,263,78,263)
