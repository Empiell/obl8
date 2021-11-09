from regneklynge import Regneklynge
from rack import Rack
from node import Node

class Datasenter:
    def __init__(self):
        self._datasenter = {}


    def lesInnRegneklynge(self , filnavn):
        navn = filnavn.split('.')[0]
        filLinjer = []

        #Lager en nøstet liste av filen
        for linje in open(filnavn):
            linje = linje.split()
            filLinjer.append(linje)
            maksNoderPerRack = filLinjer[0][0]

        nyRegneklynge = Regneklynge(maksNoderPerRack)
        #Lager den først racken, med maks antall noder
        nyRack = Rack(maksNoderPerRack)
        nyRegneklynge.leggTilRack(nyRack)

        #Oppretter noder
        #Hopper over linje 1
        for i in range(1 , len(filLinjer)):
            #Antall noder
            j = 0
            while j < int(filLinjer[i][0]):
                nyNode = Node(filLinjer[i][1] , filLinjer[i][2])
                nyRegneklynge.leggTilNode(nyNode)

                j += 1

        #Legger til regneklyngen i datasenteret
        self._datasenter[navn] = nyRegneklynge

    def skrivUtInfo(self , navn):
        print('--- Informasjon om regneklyngen "' + str(navn.capitalize()) + '" ---')
        print('Rack:' , self._datasenter[navn].hentAntRacks())
        print('Antall prosessorer:' , self._datasenter[navn].hentAntProsessorer())
        print('Noder med Minst 32 GB:' , self._datasenter[navn].noderMedNokMinne(32))
        print('Noder med Minst 64 GB:' , self._datasenter[navn].noderMedNokMinne(64))
        print('Noder med Minst 128 GB:' , self._datasenter[navn].noderMedNokMinne(128))
        print()

    def skrivUtAllInfo(self):
        for navn in self._datasenter:
            self.skrivUtInfo(navn)