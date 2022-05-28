from pickle import TRUE
import csv

class   Producto:
    # Nombre: str
    # CodSerie: str
    # Precio: float
    # Marca: str
    # EnStock: bool 
    # Proveedor: Proveedor

    def __init__(self, Nombre:str, CodSerie:str, Precio: float, Marca: str, EnStock: bool):
        self.Nombre=Nombre
        self.CodSerie=CodSerie
        self.Precio=Precio
        self.Marca=Marca
        self.EnStock=EnStock

    def GetNombre(self):
        return self.Nombre
    
    def SetNombre(self, Nombre):
        self.Nombre = Nombre
    
    def GetCodSerie(self):
        return self.CodSerie
    
    def Set(self, CodSerie):
        self.CodSerie = CodSerie
    
    def GetPrecio(self):
        return self.Precio
    
    def SetMarca(self, Marca):
        self.Marca = Marca
    
    def ListarProducto(self):
        print(self.ListarProducto)
    
    def BuscarProducto(self):
        print(self.BuscarProducto)

    def __str__(self) -> str:
        result = f'Nombre Producto: {str(self.Nombre)}\nCod Serie: {str(self.CodSerie)}\nPrecio: {self.Precio}\nMarca: {str(self.Marca)}\nStock: {str(self.EnStock)}'
        return result

# objProducto= Producto("BICICLETA","3022G",3.700,"YT", True)
# print(objProducto.__str__())

