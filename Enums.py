from enum import Enum
class EnumTipoEquipamento (Enum):
    DownHill="DownHill"
    Ruta="Ruta"

class EnumTalla (Enum):
  S="S"
  M="M"
  L="L"

class EnumTipoTela (Enum):
  Profila="Profila"
  Sintetico="Sintetico"
  Winstopper="Winstopper"
  Thermoflex="Thermoflex"

class EnumColor(Enum):
  Negro="Negro"
  Azul="Azul"
  Dorado="Dorado"
  Metal="Metal"
  Neon="Neon"
  Rojo="Rojo"
  Verde="Verde"

class EnumMetodoPago (Enum):
  Debito="Debito"
  Credito="Credito"
  PSE="PSE"
  Nequi= "Nequi"
  PayPal= "PayPal"
  Movii="Movii"