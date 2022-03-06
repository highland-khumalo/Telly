from pygame.locals import *
def game():
    import pygame, sys
    import os
    from random import randrange
    from random import randint
    
    telly = "tely.bk011.png"
    box = 'box1.png'
    
    pygame.init()
    
    font = pygame.font.SysFont("arial", 16);
    
    BLACK = (0, 0, 0)
    
    def stereo_pan(x_coord, screen_width):
        right_volume = float(x_coord) / screen_width
        left_volume = 1.0 - right_volume
        return (left_volume, right_volume)
    
    def play(obje):
        explosion_channel = obje.play()
        if explosion_channel is not None:
            left, right = stereo_pan(BOX.x, 340)
            explosion_channel.set_volume(left, right)
    
    TIME = 0
    LEVEL = 0
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    HEART = 3
    HIGHSCORE = 0
    
    telly = pygame.image.load("tely.bk011.png")
    box = pygame.image.load("box1.png")
    box2 = pygame.image.load("box1.png")
    TELLY = telly.get_rect()
    BOX = box.get_rect()
    BOX.x = randrange(180)
    BOX.y = 0
    
    BOX2 = box2.get_rect()
    BOX2.x = randrange(200) * 3 / 2
    BOX2.y = 0
    
    TELLY.x = 120
    TELLY.y = 300
    
    hp = pygame.image.load("point_h1.png")
    hpr = hp.get_rect()
    hpr.x = randrange(180)
    hpr.y = 0
    
    sp = pygame.image.load("point_s1.png")
    spr = sp.get_rect()
    spr.x = randrange(180)
    spr.y = 0
    
    if os.path.isfile("game.one"):
        with open("game.one", "r+") as game:
            game = game.read().split("\n")
            for line in game:
                if line.startswith("time: "):
                    time_new = int(line.replace("time: ", ""))
                    TIME -= TIME
                    TIME += time_new
                elif line.startswith("by:"):
                    box_new = int(line.replace("by:", ""))
                    BOX.y -= BOX.y
                    BOX.y += box_new
                elif line.startswith("b2y: "):
                    box_new = int(line.replace("b2y: ", ""))
                    BOX2.y -= BOX2.y
                    BOX2.y += box_new
                elif line.startswith("hpry: "):
                    h_new = int(line.replace("hpry: ", ""))
                    hpr.y -= hpr.y
                    hpr.y += h_new
                elif line.startswith("spry: "):
                    s_new = int(line.replace("spry: ", ""))
                    spr.y -= spr.y
                    spr.y += s_new
                elif line.startswith("Telly: "):
                    telly_new = line.replace("Telly: ", "").split("/")
                    TELLY.x -= TELLY.x
                    TELLY.x += int(telly_new[0])
                    TELLY.y -= TELLY.y
                    TELLY.y += int(telly_new[1])
                elif line.startswith("HEART: "):
                    hea_new = int(line.replace("HEART: ", ""))
                    HEART -= HEART
                    HEART += hea_new
                elif line.startswith("LEVEL: "):
                    lev_new = int(line.replace("LEVEL: ", ""))
                    LEVEL -= LEVEL
                    LEVEL += lev_new
                elif line.startswith("HIGHSCORE: "):
                    lev_new = int(line.replace("HIGHSCORE: ", ""))
                    HIGHSCORE -= HIGHSCORE
                    HIGHSCORE += lev_new
    
    pygame.display.set_caption('Telly')
    screen = pygame.display.set_mode((340, 500), 0, 32)
    scr = screen.get_rect()
    
    point = ["0", "s", "0", "s", "0", "h", "s", "0", "e", "0"] 
    t = randint(1, 9)
    ht = 1
    st = 1
    
    music = pygame.mixer.music
    
    clock = pygame.time.Clock()
    while True:
        TIME += 1
        BOX.y += 1
        BOX2.y += 1
        hpr.y += 1
        spr.y += 1
    
        if TIME == randint(1, 300000):
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
    
        if HEART < 1:
            fo = pygame.font.SysFont("arial", 100)
            screen.blit(font.render("GAME OVER!", True, (0,0,0)), (50, 100))
            if (TIME > HIGHSCORE):
                HIGHSCORE -= HIGHSCORE
                HIGHSCORE += TIME
                screen.blit(font.render("NEW HIGHSCORE!", True, (0,0,0)), (50, 200))
            pygame.display.update()
            with open("game.one", 'w') as f:
                f.write("time: " + str(TIME) + "\nby:" + str(BOX.y) + "\nb2y: " + str(BOX2.y) + "\nhpry: "\
                 + str(hpr.y) + "\nspry: " + str(spr.y) + "\nTelly: " + str(TELLY.x) + "/" + str(TELLY.y) + "\nHEART: "\
                      + str(HEART) + "\nLEVEL: " + str(LEVEL) + "\nHIGHSCORE: " + str(HIGHSCORE))
            
            pygame.time.delay(2000)
            TELLY.x -= TELLY.x
            TELLY.y -= TELLY.y
            TELLY.x += 120
            TELLY.y += 300
    
            BOX.x -= BOX.x 
            BOX.y -= BOX.y
            BOX.x += randrange(120)
            BOX.y += 0
    
            HEART += 3
            LEVEL -= LEVEL
            TIME -= TIME
    
    
        # Speed Frame
        if TIME > 900:
            BOX.y += 0.1
            BOX2.y += 0.3
        if TIME > 10000:
            BOX.y += 0.7
            BOX2.y += 0.7
        if TIME > 20000:
            BOX.y += 0.9
            BOX2.y += 0.9
        if TIME > 40000:
            BOX.y += 1
            BOX2.y += 1
        if TIME > 85000:
            BOX.y += 1.2
            BOX2.y += 1.3
        if TIME > 100000 or TIME > 550000 or TIME > 600000 or TIME > 300000:
            BOX.y += 0.3
            BOX2.y += 0.3
    
        # Level
    
        if TIME == 900:
            pygame.mixer.pre_init(44100, 16, 2, 4096)
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 10000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 20000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 35000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 40000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 85000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 100000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        if TIME == 130000 or TIME ==  140000:
            play(pygame.mixer.Sound("level.wav"))
            LEVEL += 1
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
        pygame.init()
    
    
        if BOX.y > 610:
            BOX.y -= BOX.y
            BOX.x -= BOX.x
    
            BOX.x += randrange(240)
    
        if BOX2.y > 610:
            BOX2.y -= BOX2.y
            BOX2.x -= BOX2.x
    
            BOX2.x += randrange(240)
    
        if point[t] == "h":
          if hpr.y > 610:
            hpr.y -= hpr.y
            hpr.x -= hpr.x
    
            hpr.x += randrange(240)
    
        if point[t] == "s":
          if spr.y > 610:
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
    
        for event in pygame.event.get():
            if event.type == QUIT:
                if (TIME > HIGHSCORE):
                    HIGHSCORE -= HIGHSCORE
                    HIGHSCORE += TIME
                screen.blit(font.render("NEW HIGHSCORE!", True, (0,0,0)), (50, 200))
                with open("game.one", 'w') as f:
                  f.write("time: " + str(TIME) + "\nby:" + str(BOX.y) + "\nb2y: " + str(BOX2.y) + "\nhpry: "\
                    + str(hpr.y) + "\nspry: " + str(spr.y) + "\nTelly: " + str(TELLY.x) + "/" + str(TELLY.y) + "\nHEART: "\
                      + str(HEART) + "\nLEVEL: " + str(LEVEL) + "\nHIGHSCORE: " + str(HIGHSCORE))
                pygame.quit()
                break
        screen.fill((255, 255, 255))
    
    
        # Touch
        if BOX.colliderect(TELLY):
            HEART -= 1
            BOX.y -= BOX.y
            BOX.x -= BOX.x
            play(pygame.mixer.Sound("punch.wav"))
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
    
            spr.x += randrange(240)
    
        if BOX2.colliderect(TELLY):
            HEART -= 1
            BOX2.y -= BOX2.y
            BOX2.x -= BOX2.x
            play(pygame.mixer.Sound("punch.wav"))
            t -= t
            t += randint(1, 9)
            ht += 1
            hpr.y -= hpr.y
            hpr.x -= hpr.x
            hpr.x += randrange(240)
            st += 1
            spr.y -= spr.y
            spr.x -= spr.x
            spr.x += randrange(240)
        
        if st > 2:
            st -= st
            st += 1
        if ht > 2:
            ht -= ht
            ht += 1
    
        if point[t] == "h":
         if ht > 1 and not HEART > 3 :
          if hpr.colliderect(TELLY):
            HEART += 1
            play(pygame.mixer.Sound("heart.wav"))
            hpr.y += hpr.y
            hpr.x -= hpr.x
            ht -= 1
        if point[t] == "s":
         if st > 1:
          if spr.colliderect(TELLY):
            BOX.y -= BOX.y
            BOX2.y -= BOX2.y + 50
            play(pygame.mixer.Sound("speed.wav"))
            spr.x -= spr.x
            hpr.y += hpr.y/2
            st -= 1
    
    
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            if TELLY.x > 0:
                TELLY.x -= 1.50
                if TIME > 40000:
                    TELLY.x -= 1
                if TIME > 80000:
                    TELLY.x += 1
        elif pressed_keys[K_RIGHT]:
            if TELLY.x < 238:
                TELLY.x += 1.50
                if TIME > 40000:
                    TELLY.x += 1
                if TIME > 80000:
                    TELLY.x += 1
        elif pressed_keys[K_SPACE]:
            if (TIME > HIGHSCORE):
                HIGHSCORE -= HIGHSCORE
                HIGHSCORE += TIME
                screen.blit(font.render("NEW HIGHSCORE!", True, (0,0,0)), (50, 200))
            with open("game.one", 'w') as f:
                f.write("time: " + str(TIME) + "\nby:" + str(BOX.y) + "\nb2y: " + str(BOX2.y) + "\nhpry: "\
                 + str(hpr.y) + "\nspry: " + str(spr.y) + "\nTelly: " + str(TELLY.x) + "/" + str(TELLY.y) + "\nHEART: "\
                      + str(HEART) + "\nLEVEL: " + str(LEVEL) + "\nHIGHSCORE: " + str(HIGHSCORE))
            pygame.quit()
            break
    
    
        score = font.render("Score: " + str(TIME), True, (255,255,255), (77,166,255))
        level = font.render("Level: " + str(LEVEL), True, (255,255,255), (77,166,255))
    
      
        screen.blit(telly, TELLY)
        screen.blit(box, (BOX.x, BOX.y))
        screen.blit(box2, (BOX2.x, BOX2.y))
    
        # Points
        if point[t] == "h":
            if ht > 1:
                spr.y -= spr.y / 2
                screen.blit(hp, (hpr.x, hpr.y))
        if point[t] == "s":
            if st > 1:
                screen.blit(sp, (spr.x, spr.y))
        # Achivement
        screen.blit(score, (0, 10))
        screen.blit(level, (150, 10))
        with open("game.one", 'w') as f:
            f.write("time: " + str(TIME) + "\nby:" + str(BOX.y) + "\nb2y: " + str(BOX2.y) + "\nhpry: "\
             + str(hpr.y) + "\nspry: " + str(spr.y) + "\nTelly: " + str(TELLY.x) + "/" + str(TELLY.y) + "\nHEART: "\
                  + str(HEART) + "\nLEVEL: " + str(LEVEL) + "\nHIGHSCORE: " + str(HIGHSCORE))
    
        
        if HEART == 1:
            screen.blit(pygame.image.load("h11.png"), (260, 10))
        if HEART == 2:
            screen.blit(pygame.image.load("h21.png"), (260, 10))
        if HEART == 3:
            screen.blit(pygame.image.load("h31.png"), (260, 10))
        if HEART == 4:
            screen.blit(pygame.image.load("h41.png"), (260, 10))
    
        pygame.display.update()
        clock.tick(210)
    