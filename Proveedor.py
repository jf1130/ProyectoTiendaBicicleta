import csv
from unittest import result
class   Proveedor:
    # Nombre: str
    # Code: str
    # Telefono: str
    # Email: str
    # Direccion: str 

    def __init__(self, Nombre:str, Code:str, Telefono: int, Email: str, Direccion: str):
     self.Nombre=Nombre
     self.Code=Code
     self.Telefono=Telefono
     self.Email=Email
     self.Direccion=Direccion

    def GetNombre(self):
        return self.Nombre
    
    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def GetCode(self):
        return self.Code
    
    def SetCode(self, Code):
        self.Code = Code
    
    def GetTelefono(self):
        return self.Telefono
    
    def SetTelefono(self, Telefono):
        self.Telefono = Telefono
    
    def GetEmail(self):
        return self.Email
    
    def SetEmail(self, Email):
        self.Email = Email

    def GetDireccion(self):
        return self.Direccion
    
    def SetDireccion(self, Direccion):
        self.Direccion = Direccion

    def ContactarProveedor(self):
        print(self)
    
    def __str__(self):
        result = f"Nombre del proveedor: {str(self.Nombre)}\nCode: {str(self.Code)}\nTelefono: {str(self.Telefono)}\nEmail: {str(self.Email)}\n Direccion: {str(self.Direccion)}"
        return result

# objProveedor = Proveedor("specialized","3288G",3222435678,"specilized@gmail.com","carrera 33 #25-33")
# print(objProveedor)