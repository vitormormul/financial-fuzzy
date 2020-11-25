from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.key import Key


pl = Key(-329.4, 4.8, 14.6, 26, 462.3)
pvp = Key(-8.4, 1.2, 1.9, 4.4, 21.6)
div_yield = Key(0, 0.4, 1.5, 3.9, 14.6)
roe = Key(-1159.1, 4.8, 10.5, 17.1, 526.8)

#
# pl_input = FuzzyInputVariable('P/L', pl.minimum, pl.maximum, 1_000_000)
# pl_input.add_trapezoidal('Negativo', pl.minimum, pl.bottom, pl.zero, pl.above_zero)
# pl_input.add_triangular('Baixo', pl.below_zero, pl.zero, pl.mean)
# pl_input.add_triangular('Medio', pl.lower_quartile, pl.mean, pl.upper_quartile)
# pl_input.add_triangular('Alto', pl.mean, pl.top, pl.maximum)

print(type(roe.input))