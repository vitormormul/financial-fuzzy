from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.key import Key


pl = Key(-329.4, 4.8, 14.6, 26, 462.3)
pvp = Key(-8.4, 1.2, 1.9, 4.4, 21.6)
div_yield = Key(0, 0.4, 1.5, 3.9, 14.6)
roe = Key(-1159.1, 4.8, 10.5, 17.1, 526.8)

system = FuzzySystem()
system.add_input_variable(pl.input)
system.add_input_variable(pvp.input)
system.add_input_variable(div_yield.input)
system.add_input_variable(roe.input)

