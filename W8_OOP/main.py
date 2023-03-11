import js
p5 = js.window

#1
class Player:
    #2
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
        self.size = 20  # initial size of the player
        self.timer = 0  # elapsed time since the last size change
    
    def draw(self):
        if self == player1:
            p5.noStroke()
            p5.fill(234, 102, 102)  # red color for player1
        else:
            p5.noStroke()
            p5.fill(0, 102, 153)  # blue color for player2
        p5.push()
        p5.translate(self.x, self.y)
        p5.rect(0, 0, self.size, self.size)
        p5.pop()
    
    def move_point(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    #4 function to determine if the 2 pplayers are getting too close
    def check_collision(self, other_player):
        distance = p5.dist(self.x, self.y, other_player.x, other_player.y)
        return distance < self.size + other_player.size

    #3 animate automatically the size of player1 
    def update(self):
        if self == player1 and p5.millis() > self.timer + 1000:
            self.size = self.size + 10 if self.size == 20 else 20  # toggle between two sizes
            self.timer = p5.millis()  # reset the timer
        

player1 = Player(100, 100)
player2 = Player(200, 200)


def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(245, 245, 245)           
    player1.draw()
    player2.draw()

    #4 check for collison, if in collision, player 1 reset to the original size
    if player1.check_collision(player2):
        player1.x, player1.y = 100, 100  # reset player1 position
        player1.size = 20  # reset player1 size
        player1.timer = p5.millis()  # reset the timer
        
    player1.update()  # update the size of player1

#3 animate player 2 with arrow keys
def keyPressed(event):
    if p5.keyCode == p5.RIGHT_ARROW:
        player2.move_point(10, 0)
    elif p5.keyCode == p5.LEFT_ARROW:
        player2.move_point(-10, 0)
    elif p5.keyCode == p5.UP_ARROW:
        player2.move_point(0, -10)
    elif p5.keyCode == p5.DOWN_ARROW:
        player2.move_point(0, 10)
    
def keyReleased(event):
    pass
    
def mousePressed(event):
    pass
    
def mouseReleased(event):
    pass
