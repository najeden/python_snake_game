import pygame
import random
# from ekrani import VELICINA as VELICINA
# from ekrani import POZADINA as ekrani
import ekrani

class Zmiija: 
    def __init__(self, pozadina)  -> None:
        self.pozadina = pozadina
        self.kocka = pygame.image.load("Materijali/kocka.jpg").convert()
        self.duzina = 2
        self.x = [200]*self.duzina
        self.y = [240]*self.duzina
        self.smer = "desno"

    def crtaj(self): 
        self.pozadina.fill(ekrani.POZADINA)
        for i in range(self.duzina): 
            self.pozadina.blit(self.kocka, (self.x[i], self.y[i]))

    def povecaj_se(self):
        self.duzina+=1
        self.x.append(-1)
        self.y.append(-1)

    def idi_gore(self): 
        self.smer = "gore"
    def idi_dole(self): 
        self.smer = "dole" 
    def idi_levo(self):
        self.smer = "levo"
    def idi_desno(self): 
        self.smer = "desno"

    def kreci_se(self): 
        #pometanje tela, prethodna kockica zauzima mesto sa kojeg se prva pomerila
        for i in range(self.duzina-1, 0, -1): 
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        #[0] je zapravo glava zmije
        if self.smer == "gore": 
            self.y[0] -= ekrani.VELICINA
        if self.smer == "dole": 
            self.y[0] += ekrani.VELICINA
        if self.smer == "levo":
            self.x[0] -= ekrani.VELICINA
        if self.smer == "desno": 
            self.x[0] += ekrani.VELICINA
    
        self.crtaj()

class Hrana: 
    def __init__(self, pozadina) -> None:
        self.pozadina = pozadina
        self.slika_jabuke = pygame.image.load("Materijali/jabuka.png")
        self.slika_ananasa = pygame.image.load("Materijali/ananas.png")

        self.x = random.randint(0,24)*ekrani.VELICINA
        self.y = random.randint(0,19)*ekrani.VELICINA
        self.pokusaj = 3
        self.crvenovoce = True

    def crtaj(self): 
        if self.pokusaj % 5 == 0: 
            self.pozadina.blit(self.slika_ananasa, (self.x, self.y))
            self.crvenovoce = False

        else: 
            self.pozadina.blit(self.slika_jabuke, (self.x, self.y))
            self.crvenovoce = True
    
    def getbojuvoca(self): 
        return self.crvenovoce

    def pomeri_se(self): 
        self.x = random.randint(0,24)*ekrani.VELICINA
        self.y = random.randint(0,19)*ekrani.VELICINA


if __name__ == "__main__": 
    print ("OK")