from ClassAlerta import Alerta
from EnumMetodoPago import Enum

class   Pago:
    # NumeroCuenta: str
    # Valor: float
    # Estado: bool

    def __init__(self, NumeroCuenta:str, Valor: float, Estado: bool,CodConfirmacion: Alerta):
     self.NumeroCuenta=NumeroCuenta
     self.Valor=Valor
     self.Estado=Estado
     self.CodConfirmacion=CodConfirmacion

    def GetNumeroCuenta(self):
        return self.NumeroCuenta
    
    def SetValor(self, NumeroCuenta):
        self.NumeroCuenta = NumeroCuenta
    
    def GetValor(self):
        return self.Valor
    
    def SetValor(self, Valor):
        self.Valor = Valor

    def GetEstado(self):
        return self.Estado
    
    def SetEstado(self, Estado):
        self.Estado = Estado

    def GetCodConfirmacion(self):
        return self.CodConfirmacion
    
    def SetCodConfirmacion(self, CodConfirmacion):
        self.CodConfirmacion = CodConfirmacion
    
    def LeerCodConfirmacion(self):
        print(self)
    
    def DatosCliente(self):
        print(self.Cliente)
    
    def Pagar(self):
        print(self)
        
objPago= Pago("1130F",1.600,True, Alerta.GetAlertaPago())
    

