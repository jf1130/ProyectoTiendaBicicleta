class   Producto:
    # Nombre: str
    # CodSerie: str
    # Precio: float
    # Marca: str
    # EnStock: bool 

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

objProducto= Producto()
