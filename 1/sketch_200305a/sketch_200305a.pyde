def setup():
    size(400,600)
    point(50,50)
    rectMode(CORNER)
    
def draw():
    print(mouseX,mouseY,mousePressed)
    clear()
    
    if mousePressed:
        rect(mouseX,400,200,50)
        c = color(255,254,0)
        fill(c)
    else:
        rect(100,400,200,50)
        w = color(255,0,0)
        fill(w)
