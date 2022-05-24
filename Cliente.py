import csv
from Pago import Pago
class   Cliente:
    # Nombre:str
    # Aperllido:str
    # Dni: str
    # Telefono: int
    # Email: str
    # Direccion: str
    # NumContacto:str
    # PagoCliente= Pago    

    def __init__(self, Nombre:str,Apellido:str, Dni:str, Telefono: int, Email: str, Direccion: str, NumContacto:str):
     self.Nombre=Nombre
     self.Apellido= Apellido
     self.Dni=Dni
     self.Telefono=Telefono
     self.Email=Email
     self.Direccion=Direccion
     
     self.PagoCliente= Pago ("Carlos","Martinez","df3459",3214356756,"cr@gmail.com","cra 34 # 33_12","camila-324534444")

    def Registrar(Nombre:str,Apellido:str, Dni:str, Telefono: int, Email: str, Direccion: str, NumContacto:str):str
    def Actualizar(Nombre:str,Apellido:str, Dni:str, Telefono: int, Email: str, Direccion: str, NumContacto:str):str

    def GetNombre(self):
        return self.Nombre
    
    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def GetApellido(self):
        return self.Apellido
    
    def SetApellido(self, Apellido):
        self.Apellido = Apellido

    def GetDni(self):
        return self.Dni
    
    def SetDni(self, Dni):
        self.Dni = Dni
    
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

    def GetNumContacto(self):
        return self.NumContacto
    
    def SetNumContacto(self,NumContacto):
        self.NumContacto = NumContacto

    

objCliente= Cliente("camilo","ramirez","325789-f",3213456754,"camilor56455@gmial.com","Carrera 70# 67-44","3213456754")
