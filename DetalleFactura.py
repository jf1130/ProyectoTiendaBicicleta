from Producto import Producto

class DetalleFactura:
      def __init__(self, TotalPago:int, Cantidad:int):
            self.TotalPago=TotalPago
            self.Cantidad=Cantidad
            self.ProductoSeleccionado = Producto("Bicicleta","CF344",3.500,"Sepecialized",True)


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
      
      def __str__(self) -> str:
          return f"Total Pago: {str(self.TotalPago)}\nCantidad: {str(self.Cantidad)}\nProducto Seleccionado: \n{str(self.ProductoSeleccionado)}"

# objDetalleFactura= DetalleFactura(3.600,12)
# print(objDetalleFactura.__str__())
