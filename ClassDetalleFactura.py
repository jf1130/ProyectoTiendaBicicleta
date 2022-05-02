class DetalleFactura:
  

  def __init__(self, TotalPago:int, Cantidad:int):
    self.TotalPago=TotalPago
    self.Cantidad=Cantidad
    # self.ProductoSeleccionado=Producto()
  
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

objDetalleFactura= DetalleFactura()