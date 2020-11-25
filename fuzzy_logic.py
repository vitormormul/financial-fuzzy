from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from key.key import Key


pl = Key(-329.4, 4.8, 14.6, 26, 462.3)

# pl_input = FuzzyInputVariable('P/L', -329.4, 462.4, 1_000_000)
# pl_input.add_trapezoidal('Negativo', -329.3, -329.2, 0, 0.1)
# pl_input.add_triangular('Baixo', -0.1, 0, 14.6)
# pl_input.add_triangular('Medio', 4.8, 14.6, 26)
# pl_input.add_triangular('Alto', 14.6, 462.2, 462.3)

pl_input = FuzzyInputVariable('P/L', pl.minimum, pl.maximum, 1_000_000)
pl_input.add_trapezoidal('Negativo', pl.minimum, pl.bottom, pl.zero, pl.above_zero)
pl_input.add_triangular('Baixo', pl.below_zero, pl.zero, pl.mean)
pl_input.add_triangular('Medio', pl.lower_quartile, pl.mean, pl.upper_quartile)
pl_input.add_triangular('Alto', pl.mean, pl.top, pl.maximum)
