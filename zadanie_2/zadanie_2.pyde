def setup():
    size(400,600)
    frameRate(25)
    rectMode(CENTER)
    global slownik_kolorow
    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80), "zielony":(0,255,0,80)}
    
    global lista_kolorow
    lista_kolorow = []
    
    for k, w in slownik_kolorow.items():
        lista_kolorow.append(w)
    global x, y, dx, dy, iteracja, bok_kwadratu # można też w jednej linii
    x = 50
    y = 300
    dx = 2
    dy = 3
    iteracja = 0
    bok_kwadratu = 100 # z taką zmienną kod będzie czytelniejszy i wystarczy zmienić tylko w tymmiejscu aby zmienić jego rozmiar a wszędzie dalej działało
    clear()
def draw():
    background(0)
    global dx, dy, x, y, iteracja, bok_kwadratu
    iteracja +=1
    
    fill(*lista_kolorow[iteracja%len(lista_kolorow)])
    rect(x,y,bok_kwadratu, bok_kwadratu)
    x += dx
    y += dy
    
    if(x > (width-bok_kwadratu/2)):
        dx = -2    
    elif(x < (bok_kwadratu/2)):
        dx = 2
        
    if(y > (height-bok_kwadratu/2)):
        dy = -3    
    elif(y < (bok_kwadratu/2)):
        dy = 3
        
    if mousePressed:
        exit()
        
# 2 pkt
