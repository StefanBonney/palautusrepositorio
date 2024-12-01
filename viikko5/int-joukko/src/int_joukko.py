class IntJoukko:
    
    # LISTAN LUONTI
    #=======================================================================
    KAPASITEETTI = 5
    OLETUS_KASVATUS = 5

    def __init__(self, kapasiteetti:int=None, kasvatuskoko:int=None):
        """ Alustaa uuden joukon annetulla kapasiteetilla ja kasvatuskoolla.
        """
        self.kapasiteetti = kapasiteetti if isinstance(kapasiteetti, int) and kapasiteetti >= 0 else IntJoukko.KAPASITEETTI
        self.kasvatus = kasvatuskoko if isinstance(kasvatuskoko, int) and kasvatuskoko >= 0 else IntJoukko.OLETUS_KASVATUS
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.koko = 0

    def _luo_lista(self, koko):
        """ Luo kiinteän kokoisen listan, joka alustetaan nollilla.
        """
        return [0] * koko  

    # ALKION LISÄÄMINEN LISTAAN 
    #=======================================================================
    def kuuluu(self, n:int) -> bool:
        """ Tarkistaa, kuuluuko annettu luku joukkoon. 
        """
        return n in self.alkiot[:self.koko] # leikkaa taulukko huomioimaan vain käytetyt alkiot

    def lisaa(self, n:int) -> bool:
        """ Lisää uuden luvun joukkoon, jos se ei ole siellä jo. 
        """
        if self.kuuluu(n):
            return False
        self._lisaa_listaan(n)
        self._kasvata_jos_tarvetta()
        return True

    def _lisaa_listaan(self, n:int):
        """ Apufunktio metodille - lisaa.
            Lisää luvun joukon sisäiseen listaan. 
        """
        self.alkiot[self.koko] = n
        self.koko += 1

    def _kasvata_jos_tarvetta(self):
        """ Apufunktio metodille - lisaa.
            Kasvattaa sisäisen listan kokoa, jos se on täynnä. 
        """
        if self.koko >= len(self.alkiot):
            uusi_lista = self._luo_lista(len(self.alkiot) + self.kasvatus)
            self.kopioi_lista(self.alkiot, uusi_lista)
            self.alkiot = uusi_lista

    def kopioi_lista(self, vanha_lista:list, uusi_lista:list):
        """ Kopioi alkiot vanhasta listasta uuteen listaan. 
        """
        for i in range(self.koko):
            uusi_lista[i] = vanha_lista[i]

    # ALKION POISTAMINEN LISTALTA 
    #=======================================================================    
    def poista(self, n: int) -> bool:
        """ Poistaa annetun luvun n joukosta, jos se löytyy.
        """
        # tarkistetaan listan alkiot kokoon asti 
        for i in range(self.koko):
            if self.alkiot[i] == n:  # jos luku n
                # siirretään alkiot vasemmalle
                # n ylikirjoittuu ekalla kierroksella, sitä seuraavilla kierrokisilla tuodaan seuraava edeltävään
                # lopputuloksena on lista  jossa viimeinen on dupplikaatti toisesksi viimeisestä ja voidaan poistaa
                for j in range(i, self.koko - 1):
                    self.alkiot[j] = self.alkiot[j + 1] 
                self.alkiot[self.koko - 1] = 0  
                self.koko -= 1 
                return True 
        return False  # Jos silmukka päättyy eikä lukua löytynyt, palautetaan False
    
    # MUOKATUN LISTAN PALAUTTAMINEN
    #=======================================================================  
    @staticmethod
    def yhdiste(vanha_joukko: "IntJoukko", uusi_joukko: "IntJoukko") -> "IntJoukko":
        """ Palauttaa kahden joukon yhdisteen uutena joukkona. 
        """
        x = IntJoukko()  # luo uusi IntJoukko
        yhdistetty_lista = vanha_joukko.to_int_list() + uusi_joukko.to_int_list()  # yhdistää molempien joukkojen alkiot
        for n in yhdistetty_lista:
            x.lisaa(n)  # lisää alkiot yhteen joukkoon
        return x  # palauttaa uuden IntJoukko-instanssin
    
    @staticmethod
    def leikkaus(vanha_joukko: "IntJoukko", uusi_joukko: "IntJoukko") -> "IntJoukko":
        """ Palauttaa kahden joukon leikkauksen uutena joukkona. 
        """
        leikkaus_joukko = IntJoukko()  # Luo uusi joukko
        vanhan_alkiot = vanha_joukko.to_int_list()
        uuden_alkiot= uusi_joukko.to_int_list()
        # lisää kaikki alkiot, jotka löytyvät molemmista joukoista
        for n in vanhan_alkiot:
            if n in uuden_alkiot:
                leikkaus_joukko.lisaa(n)
        return leikkaus_joukko
    
    @staticmethod
    def erotus(vanha_joukko: "IntJoukko", uusi_joukko: "IntJoukko") -> "IntJoukko":
        """ Palauttaa kahden joukon erotuksen uutena joukkona. 
        """
        erotus_joukko = IntJoukko()  # luo uusi joukko
        vanhan_alkiot = vanha_joukko.to_int_list()
        uuden_alkiot = uusi_joukko.to_int_list()
        # lisää kaikki alkiot, jotka eivät kuulu toiseen joukkoon
        for n in vanhan_alkiot:
            if n not in uuden_alkiot:
                erotus_joukko.lisaa(n)
        return erotus_joukko
    
    def to_int_list(self):
        """ Palauttaa joukon aktiiviset alkiot Pythonin listana.
        """
        return self.alkiot[:self.koko]

    # LISTAN PIIRTEIDEN TIEDUSTELU
    #=======================================================================  
    def mahtavuus(self):
        """ Palauttaa joukon aktiivisten alkioiden lukumäärän. 
        """
        return self.koko
    
    # LISTAN ESITYS
    #=======================================================================
    def __str__(self):
        """ Palauttaa joukon merkkijonoesityksen. 
        """
        if self.koko == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.alkiot[:self.koko])) + "}"
