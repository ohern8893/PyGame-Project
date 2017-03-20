#Steelbox Inc.
#Steeled Reperccusions
#Objects: Platform, music, ANQ File, Explosion, Steelbox


from gamelib import *

game = Game (800, 600, "Steeled Reperccusions")
bk = Image("images\\background.jpg",game)
bk.resizeTo(game.width*2 , game.height)

bks = Sound("music.wav",1) #Music that is playing: Big Giant Circles - The Glory Days Viceroy Danny von B. Music belongs to them.

game.setBackground(bk)

platform = Image("images\\platform.png",game)
platform.resizeBy(10)

explosion = Animation("images\\explosion.png",22,game,1254/22,64/1) #Used for later

bk.draw()
game.drawText("Steeled Reperccusions",game.width/10 ,game.height/10,Font(green,90,yellow))
game.drawText("Press [SPACE] to Start the Game!",420,400)
game.drawText("Use the Left and Right keys to move and avoid steelboxes.",game.width/10+50 ,game.height/10+55)

game.update(1)
game.wait(K_SPACE)

steelbox = [] #Loop

    

for times in range(450): #Fill Loop
    steelbox.append( Image("Steelbox.png",game) ) 

for steel in steelbox: #Make steelboxes fall
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(4,10)
    h = -90
    steel.moveTo(x,y)
    steel.setSpeed(s,180)
    steel.resizeBy(h)

platform.moveTo(850,650)


anqwalk = Animation("ANQ\\walk1_",3,game)


anqwalk.moveTo(245,525)
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)#Show background moving as you walk

    bks.play()

    bk.draw()
    platform.draw()
    anqwalk.draw()
    
    if keys.Pressed[K_RIGHT]: #Move Right
        anqwalk.x+=8
    if keys.Pressed[K_LEFT]: #Move Left
        anqwalk.x-=8

    for steel in steelbox:
        steel.move()
        if anqwalk.collidedWith(steel): #If character gets hit, -5 health
            steel.visible=False
            anqwalk.health-=5
            
        if steel.collidedWith(platform,"rectangle")and steel.y >500: #Steelbox reset if it hits the platform
            steel.visible = False
            explosion.moveTo(steel.x,steel.y) #Steelboxes explode on impact
            explosion.draw() #Where they explode
            
    if anqwalk.isOffScreen("right"): #Prevents leaving screen
        anqwalk.moveTo(anqwalk.x-100,anqwalk.y)

    if anqwalk.isOffScreen("left"): #Prevents leaving screen
        anqwalk.moveTo(anqwalk.x+100,anqwalk.y)
        
    if anqwalk.health<=0: #Game Over requirements
        game.over=True
        game.drawText("Game Over!",game.width/10 ,game.height/10,Font(green,90,yellow))
        
    
    game.drawText("Health =  " + str(anqwalk.health),500,0) #Display Health
    game.update(16)
    game.displayScore()
    
#Categories: Code, Art, Gameplay
