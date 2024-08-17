import pygame
VELICINA = 40 #slika kocke koju koristim je 40x40px
POZADINA = 67, 55, 196
BELA = 255, 255, 255



class PojeoSe(Exception): 
    def __init__(self, message= "Pojeo si se!") -> None:
        super().__init__(message)
        pygame.display.set_caption("Kraj")

        # self.pozadina= pozadina

    def poruka(self, pozadina):
        print("POJEO SI SE!")
        font = pygame.font.SysFont("calibri", 20)
        tekst1 = font.render(f"Sledeci put ne jedi sebe, nego hranu.", True, (BELA))
        pozadina.blit(tekst1, (200,325))       
        pygame.display.flip() 

class PojeoZid(Exception): 
    def __init__(self, message= "Pojeo si se!", ) -> None:
        super().__init__(message)
        pygame.display.set_caption("Kraj")

    def poruka(self, pozadina):
        print ("POJEO SI ZID")
        font = pygame.font.SysFont("calibri", 20)
        tekst1 = font.render(f"Nemoj bas glavom kroz zid sledeci put.", True, (BELA))
        pozadina.blit(tekst1, (200,325))       
        pygame.display.flip() 

class PocetniEkran(): 
    def __init__(self) -> None:
        pygame.display.set_caption("Zmijica - Dejan Milanovic")

        self.pozadina = pygame.display.set_mode((1000, 800)) #to je 27x20 blokova sa 40x40px
        self.pozadina.fill((POZADINA))
        self.ikonica = pygame.image.load("Materijali/ikonica.png").convert()
        self.naslov_font = pygame.font.SysFont("calibri", 60)
        self.naslov = self.naslov_font.render(f"Dobrodosli u Zmijicu", True, (BELA))
        obican_font = pygame.font.SysFont("calibri", 20)
        self.enter = obican_font.render(f"Za pokretanje igrice, pritisnite ENTER.", True, (BELA))
        self.esc = obican_font.render(f"Za kraj, u bilo kom momentu pritisnite ESC.", True, (BELA))
        self.kolikopoena = obican_font.render(f"Jabuka donosi 1 poen, ananas 2 poena.", True, (BELA))
        self.pravila = obican_font.render(f"Pazi da ne pojedes sebe ili zid!", True, (BELA))


    def pokreni(self): 
        pygame.init()
        pygame.display.set_caption("Pocetni ekran")
        pygame.display.set_icon(self.ikonica)
        self.pozadina.blit(self.naslov, (200,300))

        self.pozadina.blit(self.enter, (200,400))
        self.pozadina.blit (self.esc, (200,425))

        self.pozadina.blit (self.kolikopoena, (200,475))
        self.pozadina.blit (self.pravila, (200,500))
        pygame.display.flip()
        pygame.event.clear()

if __name__ == "__main__": 
    print ("OK")