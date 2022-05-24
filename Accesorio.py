from pickle import TRUE
from Color import Enum
from Producto import Producto

class Accesorio(Producto):
    

    def __init__(self, Nombre:str, CodSerie:str, Precio: float, Marca: str, EnStock: bool,TamanioRin:float):
        Producto.__init__(self, Nombre, CodSerie , Precio , Marca , EnStock)
        self.TamanioRin=TamanioRin
    
            
    
    def GetTamanioRin(self):
        return self.TamanioRin
    
    def SetTamanioRin(self, TamanioRin):
        self.TamanioRin = TamanioRin

    def __str__(self):
        result = f"Nombre del Accesorio: {str(self.Nombre)}\nCodSerie: {str(self.CodSerie)}\nPrecio: {float(self.Precio)}\nMarca: {str(self.Marca)}\nEnstock: {str(self.EnStock)}"
        return result
objAccesorio= Accesorio("Bici","A12A",3600,"GADO",True,27.5)
print(objAccesorio)


