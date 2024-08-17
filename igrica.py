import pygame
import objekti
import ekrani
from pygame.locals import *
import time

class Igrica: 
    def __init__(self) -> None:
        self.ekran = pygame.display.set_mode((1000, 800)) #to je 25x20 blokova sa 40x40px
        self.ekran.fill((ekrani.POZADINA))

        self.moja_zmija = objekti.Zmiija(self.ekran)
        self.moja_zmija.crtaj()

        self.moja_hrana = objekti.Hrana(self.ekran)
        self.moja_hrana.crtaj()
        self.poena=0

    #provera da li dolazi do sudara
    def jel_sudar(self, x_zmija, y_zmija, x_sudar, y_sudar):
        if x_sudar >= x_zmija and x_sudar < x_zmija + ekrani.VELICINA:
            if y_sudar >= y_zmija and y_sudar < y_zmija + ekrani.VELICINA:
                return True
            
    #prikazivanje poena
    def koliko_poena(self): 
        font = pygame.font.SysFont("calibri", 20)
        score = font.render(f"Poeni: {self.poena}", True, (255, 255, 255))
        self.ekran.blit(score, (800,10))

    #ako se krene u novu igru
    def reset(self):
        self.poena = 0
        self.moja_zmija = objekti.Zmiija(self.ekran)
        self.moja_hrana = objekti.Hrana(self.ekran)

    #svaki korak
    def korak(self): 
        pygame.display.set_caption("Zmijica - Dejan Milanovic")
        self.moja_zmija.kreci_se()
        self.moja_hrana.crtaj()
        self.koliko_poena()
        pygame.display.flip()

        #ako zmija jede hranu
        if self.jel_sudar(self.moja_zmija.x[0], self.moja_zmija.y[0], self.moja_hrana.x, self.moja_hrana.y):
            self.moja_zmija.povecaj_se()
            if self.moja_hrana.getbojuvoca():
                self.poena+=1
            else: 
                self.poena+=2
            self.moja_hrana.pomeri_se()
            self.moja_hrana.pokusaj +=1
            print("NJAMNJAM")

        #ako zmija jede samu sebe
        for i in range (1, self.moja_zmija.duzina): 
            if self.jel_sudar(self.moja_zmija.x[0], self.moja_zmija.y[0], self.moja_zmija.x[i], self.moja_zmija.y[i]):
                raise ekrani.PojeoSe (self.ekran)
        #ako dolazi do ivice
        if not (0 <= self.moja_zmija.x[0] <= 960 and 0 <= self.moja_zmija.y[0] <= 760): 
            raise ekrani.PojeoZid(self.ekran)
            
    #crtanje "kraj" ekrana
    def kraj(self): 
        self.ekran.fill((ekrani.POZADINA))
        font_veci = pygame.font.SysFont("calibri", 25)
        font_manji = pygame.font.SysFont("calibri", 20)

        tekst1 = font_veci.render(f"Gotov si! Poena: {self.poena}", True, (255, 255, 255))
        self.ekran.blit(tekst1, (200,250))
        tekst2 = font_manji.render("Da krenes ponovo, pritisni ENTER. Da izadjes, pritisni ESC", True, (255, 255, 255))
        self.ekran.blit(tekst2, (200, 350))
        pygame.display.flip()

    
    #glavna funkcija igrice
    def igraj(self): 
        print ("krenuli")
        ikonica = pygame.image.load("Materijali/ikonica.png").convert()
        pygame.display.set_icon(ikonica)

        program = True
        pauza = False

        while program: 
            for event in pygame.event.get(): #sta raditi ako dodje do pritiska tastera
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        print("CAO")
                        program = False
                        pygame.quit()
                        quit()
                    if event.key == K_RETURN: 
                        print ("NOVA IGRA")
                        pauza = False

                    #kretanje zmije
                    if event.key == K_UP or event.key == K_w: 
                        if self.moja_zmija.smer== "dole": 
                            continue
                        self.moja_zmija.idi_gore()
                    if event.key == K_DOWN or event.key == K_s: 
                        if self.moja_zmija.smer== "gore": 
                            continue                        
                        self.moja_zmija.idi_dole()
                    if event.key == K_LEFT or event.key == K_a: 
                        if self.moja_zmija.smer== "desno": 
                            continue                        
                        self.moja_zmija.idi_levo()
                    if event.key == K_RIGHT or event.key == K_d: 
                        if self.moja_zmija.smer== "levo": 
                            continue
                        self.moja_zmija.idi_desno()
                elif event.type == QUIT: 
                    program = False
                    pygame.quit()
                    quit()

            try:
                if not pauza: 
                    self.korak()
            except ekrani.PojeoSe as e: 
                self.kraj()
                e.poruka(self.ekran)      
                pauza = True
                self.reset()
            except ekrani.PojeoZid as e: 
                self.kraj()
                e.poruka(self.ekran)      
                pauza = True
                self.reset()
            except Exception as e: 
                self.kraj()
                pauza = True
                self.reset()
                            
            time.sleep(0.1)

if __name__ == "__main__": 
    print ("OK")