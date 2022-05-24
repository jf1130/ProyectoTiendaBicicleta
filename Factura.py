import csv
from Carrito import Infoventa

class   Factura:
    # CodFactura: str
    # Nit: str

    def __init__(self, CodFactura:str, Nit: str):
     self.CodFactura=CodFactura
     self.Nit=Nit
     
     self.InfoVenta

    def GetCodFactura(self):
        return self.CodFactura
    
    def SetCodFactura(self, CodFactura):
        self.CodFactura = CodFactura

    def GetNit(self):
        return self.Nit
    
    def SetNit(self, Nit):
        self.Nit = Nit

    def DetalleVenta(self):
        print(self.CodFactura)

objFactura= Factura("S32345","4233F")