from node import Node

class Rack:
    def __init__(self, maksAntNoder):
        self._rack = []
        self._maksNoder = int(maksAntNoder)

    #Legger til Node om det er plass i rack, hvis ikke, returner False
    def leggTilNode(self , node):
        if len(self._rack) < self._maksNoder:
            self._rack.append(node)
            return True
        return False

    def hentAntProsessorer(self):
        antProsessorer = int(0)
        for node in self._rack:
            antProsessorer += node.hentAntProsessorer()

        return antProsessorer

    def noderMedNokMinne(self, paakrevdMinne):
        antNoderMedNokMinne = int(0)
        for node in self._rack:
            if node.hentMinneStorrelse() >= int(paakrevdMinne):
                antNoderMedNokMinne += 1

        return antNoderMedNokMinne