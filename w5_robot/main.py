import js

p5 = js.window
eye_x1 = 125
eye_x2 = 175
eye_y = 80
leg_x1 = 120
leg_x2 = 180
leg_y = 250
leg_length = 50
arm_x1 = 210
arm_x2 = 90
arm_y = 140
arm_length = 40
pocket_x = 145
pocket_y = 155

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
def draw():
    p5.background("#83e2ee")# white background
    p5.strokeWeight(2)
    face()
    arms()
    legs()
    body()
    eyes()
    pocket()
    
def pocket():
    global pocket_x, pocket_y

    p5.stroke(0)
    p5.fill('#83e2ee')
    # rect1
    p5.rect(110, 125, 80, 100)

    # limit movement of rect2 within rect1
    pocket_x = max(min(pocket_x, 175), 115)
    pocket_y = max(min(pocket_y, 180), 130)

    #rect2
    p5.fill(0)
    p5.rect(pocket_x, pocket_y, 10, 40)

    # move rect2 with arrow keys
    if p5.keyIsPressed:
        if p5.key == 'd':
            pocket_x += 5
        elif p5.key == 'a':
            pocket_x -= 5
        elif p5.key == 'w':
            pocket_y -= 5
        elif p5.key == 's':
            pocket_y += 5
          
def face():
    p5.stroke(0)
    p5.fill('#ff7aae')
    p5.ellipse(150,100,120,100)
    
def body():
    p5.stroke(0)
    p5.fill('#fddc02')
    p5.rect(90,100,120,150)

def arms():
    global arm_x1, arm_x2, arm_y, arm_length
    p5.stroke(0)
    p5.fill('#ff7aae')
    p5.ellipse(arm_x1, arm_y, arm_length, 40)
    p5.ellipse(arm_x2, arm_y, arm_length, 40)

    if p5.keyCode == p5.UP_ARROW:
        arm_length = max(arm_length - 5, 10)
    elif p5.keyCode == p5.DOWN_ARROW:
        arm_length = min(arm_length + 10, 40)
  
def legs():
    global leg_x1, leg_x2, leg_y, leg_length
    p5.fill('#ff7aae')
    p5.ellipse(leg_x1, leg_y, 40, leg_length)
    p5.ellipse(leg_x2, leg_y, 40, leg_length)

    if p5.keyCode == p5.UP_ARROW:
        leg_length = max(leg_length - 5, 20)
    elif p5.keyCode == p5.DOWN_ARROW:
        leg_length = min(leg_length + 5, 50)

def eyes():

    global eye_x1, eye_x2, eye_y
    eye_size = 20
    p5.fill(0)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(0)  
            eye_size = 8 
        elif (p5.mouseButton == p5.RIGHT):
            p5.stroke(0)
            p5.strokeWeight(8)
            p5.fill(255) 
            eye_size = 20
    p5.ellipse(eye_x1, eye_y, eye_size, eye_size)
    p5.ellipse(eye_x2, eye_y, eye_size, eye_size)
