from typing import Any
from Enums import EnumColor, EnumTalla, EnumTipoTela, EnumTipoEquipamento
from Alerta import Alerta
from Proveedor import Proveedor
from Carrito import Carrito
from Pago import Pago
from Accesorio import Accesorio
from Producto import Producto
from Equipamento import Equipamento
from DetalleFactura import  DetalleFactura
from Cliente import Cliente
from Factura import Factura


def polimorfismo(Producto:Producto):
        print(Producto.__str__()) 

objAlerta = Alerta("Si se confirma el pedido")
print(objAlerta.__str__())
print("----//----"*4,'\n')

objProveedor = Proveedor("specialized","3288G",3222435678,"specilized@gmail.com","carrera 33 #25-33")
print(objProveedor.__str__(),'\n')
print("----//----"*4,'\n')

objPago= Pago("1130F",1.600, True, objAlerta.GetAlertaPago())
print(objPago.__str__(),'\n')
print("----//----"*4,'\n')

objProducto= Producto("BICICLETA","3022G",3.700,"YT", True)
print(objProducto.__str__(),'\n')

objAccesorio= Accesorio("Bici","A12A",3600,"GADO",True,27.5, EnumColor.Dorado)
print(objAccesorio.__str__(),'\n')

objEquipamento= Equipamento("Bici","B420","50.000","Llanero",True,EnumTalla.L,EnumTipoTela.Thermoflex,EnumTipoEquipamento.DownHill)
print(objEquipamento.__str__(),'\n')
print("----//----"*4,'\n')

objDetalleFactura= DetalleFactura(3.600,12)
print(objDetalleFactura.__str__())
print("----//----"*4,'\n')

objFactura = Factura("S32345","4233F")
print(objFactura.__str__())
print("----//----"*4,'\n')

objCliente= Cliente('Juanito', 'Alimania', 'j4567891', 314558756, 'example@example.com', 'KR 41 # 30-58', "8885541")
print(objCliente.__str__())
print("----//----"*4,'\n')

# objCarrito= Carrito(1234, "Batallon", 'Bicicleta', objProducto.GetNombre())
# print(objCarrito.__str__())
# print("----//----"*4,'\n')

