from TipoTela import EnumTipoTela
from TipoEquipamento import EnumTipoEquipamento
from Talla import EnumTalla
from Equipamento import Producto

class Equipamento(Producto):
    

    def __init__(self,Talla:EnumTalla,TipoTela:EnumTipoTela,TipoEquipamento:EnumTipoEquipamento):
        self.Talla=Talla
        self.TipoTela= TipoTela
        self.TipoEquipamento= TipoEquipamento
    
        Producto.__init__(self, Nombre, CodSerie, Precio, Marca, EnStock)

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