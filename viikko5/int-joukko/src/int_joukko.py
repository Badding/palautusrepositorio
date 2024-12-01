KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if n in self.ljono:
            return False
        
        if len(self.ljono) >= self.kapasiteetti:
            self.kasvata_listaa()
        
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True
        
    def kasvata_listaa(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)

        for i in range(0, self.alkioiden_lkm):
            uusi_lista[i] = self.ljono[i]

        self.ljono = uusi_lista
        self.kapasiteetti = self.alkioiden_lkm + self.kasvatuskoko


    def poista(self, n):
        if n not in self.ljono:
            return False
        
        index = self.ljono.index(n)
        for i in range(index, len(self.ljono) - 1):
            self.ljono[i] = self.ljono[i + 1]

        self.alkioiden_lkm -= 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for n in a.to_int_list():
            x.lisaa(n)
        for n in b.to_int_list():
            x.lisaa(n)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu:
            if n in b_taulu:
                y.lisaa(n)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu:
            if n not in b_taulu:
                z.lisaa(n)
        return z


    def __str__(self):

        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
