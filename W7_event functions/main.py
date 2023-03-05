import js
p5 = js.window

program_state = 'state1' # Initialize program state
program_timer = p5.millis() # Initialize program timer

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    global program_state, program_timer
    p5.background(255)
    if program_state == 'state1':
        p5.fill(255, 0, 0, 80) # Set fill color to red
        p5.circle(p5.width/2, p5.height/2, 100) # Draw a circle at the center of the canvas with a diameter of 100
    elif program_state == 'state2':
        p5.fill(0, 0, 255,80) # Set fill color to blue
        p5.rect(75, 75, 150, 150) # Draw a rectangle at (75, 75) with a width and height of 150
    elif program_state == 'state3':
        p5.fill(0, 255, 0, 80) # Set fill color to green
        p5.ellipse(p5.mouseX, p5.mouseY, 50, 50) # Draw an ellipse at the current mouse position with a diameter of 50
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)

    # Check if time interval has elapsed
    if p5.millis() - program_timer > 2000 and program_state == 'state1':
        program_state = 'state2' # Update program state to 'state2'
        program_timer = p5.millis() # Reset program_timer

def keyPressed(event):
    global program_state, program_timer
    if p5.key == '1':
        program_state = 'state1' # Switch to 'state1'
        program_timer = p5.millis() # Reset program_timer
    elif p5.key == '2':
        program_state = 'state2' # Switch to 'state2'
        program_timer = p5.millis() # Reset program_timer
    elif p5.key == '3':
        program_state = 'state3' # Switch to 'state3'
    print('keyPressed.. ' + str(p5.key))

def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))

def mousePressed(event):
    global program_state
    program_state = 'state3' # Change program state to 'state3' when mouse is pressed

def mouseReleased(event):
    print('mouseReleased..')
