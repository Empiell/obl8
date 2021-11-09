class Node:
    def __init__(self , minneStørrelse , antProsessorer):
        self._minne = int(minneStørrelse)
        self._prosessorer = int(antProsessorer)

    def hentMinneStorrelse(self):
        return self._minne

    def hentAntProsessorer(self):
        return self._prosessorer