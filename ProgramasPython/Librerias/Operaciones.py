def CalcularPenalidadYMontos(MontoBase, Categoria, TipoCambioSoles):
    MontoBaseSoles = MontoBaseDolares * TipoCambioSoles
    MontoPenalidadSoles = MontoBaseSoles * PorcPenalidad
    MontoAPagarSoles = MontoBaseSoles + MontoPenalidadSoles