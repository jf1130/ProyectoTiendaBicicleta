class   Carrito:
    # IdVenta: int
    # DireccEntrega: str

    def __init__(self, IdVenta:int, DireccionEntrega:str):
     self.Idventa=IdVenta
     self.DireccionEntrega=DireccionEntrega

    def GetIdVenta(self):
        return self.IdVenta
    
    def SetIdVenta(self, IdVenta):
        self.IdVenta = IdVenta

    def GetDireccEntrega(self):
        return self.DireccEntrega
    
    def SetDireccEntrega(self, DireccEntrega):
        self.DireccEntrega= DireccEntrega

objCarrito= Carrito()