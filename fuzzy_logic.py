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
investment.add_trapezoidal('Forte', 50, 75, 99.9, 100)

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

#1
system.add_rule(
    {'P/L': 'Negativo'},
    {'Investimento': 'Fraco',
     'Preco': 'Favoravel'}
)
#2
system.add_rule(
    {'P/L': 'Baixo'},
    {'Investimento': 'Avaliar',
     'Preco': 'Favoravel'}
)
#3
system.add_rule(
    {'P/L': 'Medio'},
    {'Investimento': 'Forte',
     'Preco': 'Avaliar'}
)
#4
system.add_rule(
    {'P/L': 'Alto'},
    {'Investimento': 'Avaliar',
     'Preco': 'Desfavoravel'}
)
#5
system.add_rule(
    {'P/VPA': 'Negativo'},
    {'Investimento': 'Fraco',
     'Preco': 'Favoravel'}
)
#6
system.add_rule(
    {'P/VPA': 'Baixo'},
    {'Investimento': 'Forte',
     'Preco': 'Favoravel'}
)
#7
system.add_rule(
    {'P/VPA': 'Medio'},
    {'Investimento': 'Forte',
     'Preco': 'Avaliar'}
)
#8
system.add_rule(
    {'P/VPA': 'Alto'},
    {'Investimento': 'Avaliar',
     'Preco': 'Desfavoravel'}
)
#9
system.add_rule(
    {'Yield': 'Baixo'},
    {'Investimento': 'Avaliar',
     'Preco': 'Desfavoravel'}
)
#10
system.add_rule(
    {'Yield': 'Medio'},
    {'Investimento': 'Forte',
     'Preco': 'Avaliar'}
)
#11
system.add_rule(
    {'Yield': 'Alto'},
    {'Investimento': 'Fraco',
     'Preco': 'Favoravel'}
)
#12
system.add_rule(
    {'ROE': 'Negativo'},
    {'Investimento': 'Fraco'}
)
#13
system.add_rule(
    {'ROE': 'Baixo'},
    {'Investimento': 'Fraco'}
)
#14
system.add_rule(
    {'ROE': 'Medio'},
    {'Investimento': 'Avaliar'}
)
#15
system.add_rule(
    {'ROE': 'Alto'},
    {'Investimento': 'Forte'}
)

# output = system.evaluate_output(
#     {'P/L': 1,
#      'P/VPA': 1,
#      'Yield': 1,
#      'ROE': 1}
# )
# print(output)

# system.plot_system()
