from Enums import EnumTipoEquipamento,EnumTipoTela,EnumTalla
from Producto import Producto

class Equipamento(Producto):
    

    def __init__(self, Nombre:str, CodSerie:str, Precio:float, Marca:str, EnStock:str,Talla:EnumTalla,TipoTela:EnumTipoTela,TipoEquipamento:EnumTipoEquipamento):
        Producto.__init__(self, Nombre, CodSerie, Precio, Marca, EnStock)
        self.Talla=Talla
        self.TipoTela= TipoTela
        self.TipoEquipamento= TipoEquipamento
    

    def GetTalla(self):
        return self.Talla
    
    def SetValor(self, Talla):
        self.Talla = Talla
    
    def GetTipoTela(self):
        return self.TipoTela
    
    def SetValor(self, TipoTela):
        self.TipoTela = TipoTela

    def GetTipoEquipamento(self):
        return self.TipoEquipamento
    
    def SetValor(self, TipoEquipamento):
        self.TipoEquipamento = TipoEquipamento
    
    def __str__(self):
        result = f"Nombre Del Equipamento: {str(self.Nombre)}\nCodSerie:{str(self.CodSerie)}\nPrecio:{float(self.Precio)}\nMarca:{str(self.Marca)}\nEnStock:{str(self.EnStock)}\nTalla:{str(self.Talla.value)}\nTipoTela:{str(self.TipoTela.value)}\nTipoEquipamneto:{str(self.TipoEquipamento.value)}"
        return result
objEquipamento= Equipamento("Bici","B420","50.000","Llanero",True,EnumTalla.L,EnumTipoTela.Thermoflex,EnumTipoEquipamento.DownHill)
print(objEquipamento)

