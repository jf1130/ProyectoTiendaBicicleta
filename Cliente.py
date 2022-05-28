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
        self.NumContacto=NumContacto
        self.PagoCliente= Pago("1130F",1.600, True, any)

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
    
    def __str__(self):
        result = f"Cliente: {str(self.Nombre)}\nApellido: {str(self.Apellido)}\nDni: {str(self.Dni)}\nTelefono: {str(self.Telefono)}\nDireccion: {str(self.Direccion)}\nEmail: {str(self.Email)}\nNumContacto: {str(self.NumContacto)}\n\nDatos del pago\n\n{str(self.PagoCliente)}"
        return result

# objCliente= Cliente('Juanito', 'Alimania', 'j4567891', 314558756, 'example@example.com', 'KR 41 # 30-58', "8885541")
# print(objCliente.__str__())
