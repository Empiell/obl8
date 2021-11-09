from rack import Rack

class Regneklynge:
    def __init__(self , antNoderPerRack):
        self._rackListe = []
        self._noderPerRack = antNoderPerRack


    def leggTilRack(self , rack):
        self._rackListe.append(rack)


    def leggTilNode(self , node):
        #Sjekker om siste rack i racklisten er full
        if not self._rackListe[-1].leggTilNode(node):
            nyRack = Rack(self._noderPerRack)
            self._rackListe.append(nyRack)
            self.leggTilNode(node)


    def hentAntRacks(self):
        return len(self._rackListe)


    def hentAntProsessorer(self):
        antProsessorer = 0
        for rack in self._rackListe:
            antProsessorer += rack.hentAntProsessorer()

        return antProsessorer


    def noderMedNokMinne(self , paakrevdMinne):
        antNoderMedNokMinne = 0
        for rack in self._rackListe:
            antNoderMedNokMinne += rack.noderMedNokMinne(paakrevdMinne)
        
        return antNoderMedNokMinne