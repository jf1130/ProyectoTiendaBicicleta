from Enums import EnumTipoEquipamento,EnumTipoTela,EnumTalla
from Producto import Producto

class Equipamento(Producto):
    

    def __init__(self, Nombre:str, CodSerie:int, Precio:float, Marca:str, EnStock:bool,Talla:EnumTalla,TipoTela:EnumTipoTela,TipoEquipamento:EnumTipoEquipamento):
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
    
    def