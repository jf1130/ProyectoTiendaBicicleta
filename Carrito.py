import csv
from pickle import TRUE
from Pago import Pago
from Producto import Producto
class   Carrito:
    # IdVenta: int
    # DireccEntrega: str

    def __init__(self, IdVenta:int, DireccionEntrega:str, ProductoSeleccionado: str,InfoProducto=Producto):
     self.Idventa=IdVenta
     self.DireccionEntrega=DireccionEntrega
     self.ProductoSeleccionado=ProductoSeleccionado
     self.InfoProducto=InfoProducto

     self.Pago= Pago("3765H",5.600,TRUE)

    def GetIdVenta(self):
        return self.IdVenta
    
    def SetIdVenta(self, IdVenta):
        self.IdVenta = IdVenta

    def GetDireccEntrega(self):
        return self.DireccEntrega
    
    def SetDireccEntrega(self, DireccEntrega):
        self.DireccEntrega= DireccEntrega

    def GetProductoSeleccionado(self):
        return self.ProductoSeleccionado
    
    def SetProductoSeleccionado(self, ProductoSeleccionado):
        self.ProductoSeleccionado= ProductoSeleccionado

    def GetInfoProducto(self):
        return self.InfoProducto
    
    def SetInfoProducto(self, InfoProducto):
        self.InfoProducto= InfoProducto

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
    
    def __str__(self):
        result = f" Carrito: {str(self.IdVenta)}\nDireccionEntrega: {str(self.DireccEntrega)}\nProductoSeleccionado: {float(self.ProductoSeleccionado)}\nInfoProducto: {str(self.InfoProducto)}"
        return result

objCarrito= Carrito(7546,"Carrera 38 # 54-23")
print("El Id de venta es el:", str(objCarrito.GetIdVenta()), "La direccion de entrega es:", str(objCarrito.GetDireccionEntrega()), "La alerta es ")

