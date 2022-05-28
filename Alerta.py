class   Alerta:
    # AlertaPago: str
       def __init__(self, AlertaPago:str):
              self.AlertaPago=AlertaPago

       def GetAlertaPago(self):
              return self.AlertaPago
       
       def SetTotalpago(self, AlertaPago):
              self.AlertaPago = AlertaPago

       def EnviarCodConfirmacion(self):
              print(self)

       def AlertaPago(self):
              print(self)

       def __str__(self):
               result = f"alerta: {str(self.AlertaPago)}"
               return result

# objAlerta= Alerta("Si se confirma el pedido")
