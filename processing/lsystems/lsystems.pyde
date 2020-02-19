from LSystem import LSystem, Turtle

def setup():
    size(500, 500)

    global turtle, lsys
            
    lsys = LSystem("F", {"F": "FF+[+F-F-F]-[-F+F+F]"})
    turtle = Turtle(lsys.generate(), height/10, radians(25))

def draw():
    background(255)
    fill(0)
    
    translate(width/2, height)
    rotate(-PI/2)
    turtle.render()

def mousePressed():
    pushMatrix()
    turtle.sentence = lsys.generate()
    turtle.linelen *= 0.5
    turtle.render()
    popMatrix()
    redraw()
