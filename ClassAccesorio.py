from EnumColor import Enum
from ClassAccesorio import Producto

class Accesorio(Producto):
    #TamanioRin:float

    def __init__(self,TamanioRin:float):
        self.TamanioRin=TamanioRin
    
        Producto.__init__(self,Nombre, CodSerie, Precio, Marca, EnStock)
    
    def GetTamanioRin(self):
        return self.TamanioRin
    
    def SetTamanioRin(self, TamanioRin):
        self.TamanioRin = TamanioRin