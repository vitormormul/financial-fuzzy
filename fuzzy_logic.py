from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.key import Key
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable


pl = Key('P/L', -329.4, 4.8, 14.6, 26, 462.3)
pvp = Key('P/VPA', -8.4, 1.2, 1.9, 4.4, 21.6)
div_yield = Key('Yield', 0, 0.4, 1.5, 3.9, 14.6, negative=False)
roe = Key('ROE', -1159.1, 4.8, 10.5, 17.1, 526.8)

investment = FuzzyOutputVariable('Investimento', 0, 100, 1_000_000)
investment.add_trapezoidal('Fraco', 0, 0.1, 25, 50)
investment.add_triangular('Avaliar', 25, 50, 75)
investment.add_trapezoidal('Fraco', 50, 75, 99.9, 100)

price = FuzzyOutputVariable('Preco', 0, 100, 1_000_000)
price.add_trapezoidal('Favoravel', 0, 0.1, 25, 50)
price.add_triangular('Avaliar', 25, 50, 75)
price.add_trapezoidal('Desfavoravel', 50, 75, 99.9, 100)

system = FuzzySystem()
system.add_input_variable(pl.input)
system.add_input_variable(pvp.input)
system.add_input_variable(div_yield.input)
system.add_input_variable(roe.input)
system.add_output_variable(investment)
system.add_output_variable(price)

system.plot_system()
