import csv
from typing import Any
from Carrito import Carrito
from Pago import Pago

class   Factura:
    # CodFactura: str
    # Nit: str

    def __init__(self, CodFactura:str, Nit: str):
     self.CodFactura=CodFactura
     self.Nit=Nit
     self.InfoVenta = Pago("1130F",1.600, True, Any)

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
    
    def __str__(self) -> str:
        return f"Codigo de factura: {str(self.CodFactura)}\nNIT: {str(self.Nit)}\nInformación del producto:\n{str(self.InfoVenta)}"

# objFactura = Factura("S32345","4233F")
# print(objFactura.__str__())