class   Pago:
    # NumeroCuenta: str
    # Valor: float
    # Estado: bool

    def __init__(self, NumeroCuenta:str, Valor: float, Estado: bool):
     self.NumeroCuenta=NumeroCuenta
     self.Valor=Valor
     self.Estado=Estado

     def GetNumeroCuenta(self):
        return self.NumeroCuenta
    
    def SetNit(self, NumeroCuenta):
        self.NumeroCuenta = NumeroCuenta
    
    def GetValor(self):
        return self.Valor
    
    def SetValor(self, Valor):
        self.Valor = Valor

    def GetEstado(self):
        return self.Estado
    
    def SetEstado(self, Estado):
        self.Estado = Estado
    
objPago= Pago()
    
    

