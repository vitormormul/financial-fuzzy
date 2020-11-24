from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem


pl = FuzzyInputVariable('P/L', -329.4, 462.4, 1_000_000)
pl.add_trapezoidal('Negativo', -329.3, -329.2, 0, 0.1)
pl.add_triangular('Baixo', -0.1, 0, 14.6)
pl.add_triangular('Medio', 4.8, 14.6, 26)
pl.add_triangular('Alto', 14.6, 462.2, 462.3)

