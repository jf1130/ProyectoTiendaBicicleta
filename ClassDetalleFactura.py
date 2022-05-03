import csv
from pickle import TRUE
from ClassProducto import Producto
class DetalleFactura:
  

  def __init__(self, TotalPago:int, Cantidad:int):
    self.TotalPago=TotalPago
    self.Cantidad=Cantidad

    self.ProductoSeleccionado = Producto("Bicicleta","CF344",3.500,"Sepecialized",TRUE)

  
  def GetTotalPago(self):
        return self.TotalPago
    
  def SetTotalpago(self, TotalPago):
        self.TotalPago = TotalPago

  def GetCantidad(self):
        return self.Cantidad
    
  def SetCantidad(self, Cantidad):
        self.Cantidad = Cantidad

  def GetProductoSeleccionado(self):
        return self.ProductoSeleccionado
    
  def SetProductoSeleccionado(self, ProductoSeleccionado):
        self.ProductoSeleccionado = ProductoSeleccionado
        
  def CalcularTotalProducto(self):
    print(self.TotalPago)

  def EliminarProducto(self):
      print(self.ProductoSeleccionado)

objDetalleFactura= DetalleFactura(3.600,12)
