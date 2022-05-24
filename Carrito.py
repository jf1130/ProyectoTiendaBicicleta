import csv
from pickle import TRUE
from Pago import Pago
class   Carrito:
    # IdVenta: int
    # DireccEntrega: str

    def __init__(self, IdVenta:int, DireccionEntrega:str):
     self.Idventa=IdVenta
     self.DireccionEntrega=DireccionEntrega

     self.Pago= Pago("3765H",5.600,TRUE)

    def GetIdVenta(self):
        return self.IdVenta
    
    def SetIdVenta(self, IdVenta):
        self.IdVenta = IdVenta

    def GetDireccEntrega(self):
        return self.DireccEntrega
    
    def SetDireccEntrega(self, DireccEntrega):
        self.DireccEntrega= DireccEntrega

    def UpdateDireccionEntrega(self, DireccionEntrega):
        self.DireccionEntrega = DireccionEntrega
    
    def ListarProductos(self):
        print(self.Productos)

    def PagoConfirmado(self):
        EsPagoConfirmado:bool = self.Pago.GetEstado()
        if EsPagoConfirmado == True:
            print("El pago a sido confirmado")
        else:
            print("El pago No a sido confirmado")

objCarrito= Carrito(7546,"Carrera 38 # 54-23")
print("El Id de venta es el:", str(objCarrito.GetIdVenta()), "La direccion de entrega es:", str(objCarrito.GetDireccionEntrega()), "La alerta es ")