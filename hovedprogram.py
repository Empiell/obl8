from datasenter import Datasenter

def hovedprogram():
    hovedDatasenter = Datasenter()

    hovedDatasenter.lesInnRegneklynge('abel.txt')
    hovedDatasenter.lesInnRegneklynge('saga.txt')

    hovedDatasenter.skrivUtInfo('abel')
    hovedDatasenter.skrivUtInfo('saga')
    hovedDatasenter.skrivUtAllInfo()
    

hovedprogram()