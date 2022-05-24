from enum import Enum
class EnumTipoEquipamento (Enum):
    DownHill=1
    Ruta=2

class EnumTalla (Enum):
  S=1
  M=2
  L=3

class EnumTipoTela (Enum):
  Profila=1
  Sintetico=2
  Winstopper=3
  Thermoflex=4

class EnumColor(Enum):
  Negro=1
  Azul=2
  Dorado=3
  Metal=4
  Neon=5
  Rojo=6
  Verde=7

class EnumMetodoPago (Enum):
  Debito=1
  Credito=2
  PSE=3
  Nequi= 4
  PayPal= 5
  Movii=6