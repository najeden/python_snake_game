import pygame
import ekrani
import igrica

if __name__ == "__main__": 
    pygame.init()  
    pocetni = ekrani.PocetniEkran()
    pocetni.pokreni()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("CAO")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        igra = igrica.Igrica()
                        igra.igraj()
                    elif event.key == pygame.K_ESCAPE: 
                        print ("CAO")
                        pygame.quit()
                        quit()       