def OpcionMenu(opcionMenu):
    if (3 > opcionMenu > 1):
        return True
    else:
        return False
        
def ValidarMontoBase(MontoBaseDolares):
    valor  = float(MontoBaseDolares)
    if valor > 0:
        return True
    else:
        return False
    
def ValidarCategoria(Categoria):
    if (Categoria.upper() == 'A' or Categoria.upper() == 'B' or Categoria.upper() == 'C' or Categoria.upper() == 'D' or Categoria.upper() == 'E'):
        return True
    else:
        return False
    
def ValidarTipoCambio(TipoCambio):
    valor = float(TipoCambio)
    if valor > 0:
        return True
    else:
        return False
    
def ValidarRpta(respuesta):
    if (respuesta.upper() == 'S' or respuesta.upper() == 'N'):
        return True
    else:
        return False