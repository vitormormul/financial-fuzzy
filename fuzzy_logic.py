from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.key import Key
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable


def plot_fuzzy():
    pl_ = Key('P/L', -329.4, 4.8, 14.6, 26, 462.3)
    pvp_ = Key('P/VPA', -8.4, 1.2, 1.9, 4.4, 21.6)
    div_yield_ = Key('Yield', 0, 0.4, 1.5, 3.9, 14.6, negative=False)
    roe_ = Key('ROE', -1159.1, 4.8, 10.5, 17.1, 526.8)

    investment = FuzzyOutputVariable('Investimento', 0, 100, 1000)
    investment.add_trapezoidal('Fraco', 0, 0.1, 20, 40)
    investment.add_trapezoidal('Avaliar', 20, 40, 60, 80)
    investment.add_trapezoidal('Forte', 60, 80, 99.9, 100)

    price = FuzzyOutputVariable('Preco', 0, 100, 1000)
    price.add_trapezoidal('Desfavoravel', 0, 0.1, 20, 40)
    price.add_trapezoidal('Avaliar', 20, 40, 60, 80)
    price.add_trapezoidal('Favoravel', 60, 80, 99.9, 100)

    system = FuzzySystem()
    system.add_input_variable(pl_.input)
    system.add_input_variable(pvp_.input)
    system.add_input_variable(div_yield_.input)
    system.add_input_variable(roe_.input)
    system.add_output_variable(investment)
    system.add_output_variable(price)
    system.plot_system()


def run_fuzzy(pl, pvp, div_yield, roe, ticker):
    pl_ = Key('P/L', -329.4, 4.8, 14.6, 26, 462.3)
    pvp_ = Key('P/VPA', -8.4, 1.2, 1.9, 4.4, 21.6)
    div_yield_ = Key('Yield', 0, 0.4, 1.5, 3.9, 14.6, negative=False)
    roe_ = Key('ROE', -1159.1, 4.8, 10.5, 17.1, 526.8)

    investment = FuzzyOutputVariable('Investimento', 0, 100, 1000)
    investment.add_trapezoidal('Fraco', 0, 0.1, 20, 40)
    investment.add_trapezoidal('Avaliar', 20, 30, 70, 80)
    investment.add_trapezoidal('Forte', 60, 80, 99.9, 100)

    price = FuzzyOutputVariable('Preco', 0, 100, 1000)
    price.add_trapezoidal('Desfavoravel', 0, 0.1, 20, 40)
    price.add_trapezoidal('Avaliar', 20, 30, 70, 80)
    price.add_trapezoidal('Favoravel', 60, 80, 99.9, 100)

    system = FuzzySystem()
    system.add_input_variable(pl_.input)
    system.add_input_variable(pvp_.input)
    system.add_input_variable(div_yield_.input)
    system.add_input_variable(roe_.input)
    system.add_output_variable(investment)
    system.add_output_variable(price)

    # 1
    system.add_rule(
        {'P/L': 'Negativo'},
        {'Investimento': 'Fraco',
         'Preco': 'Favoravel'}
    )
    # 2
    system.add_rule(
        {'P/L': 'Baixo'},
        {'Investimento': 'Avaliar',
         'Preco': 'Favoravel'}
    )
    # 3
    system.add_rule(
        {'P/L': 'Medio'},
        {'Investimento': 'Forte',
         'Preco': 'Avaliar'}
    )
    # 4
    system.add_rule(
        {'P/L': 'Alto'},
        {'Investimento': 'Forte',
         'Preco': 'Desfavoravel'}
    )
    # 5
    system.add_rule(
        {'P/VPA': 'Negativo'},
        {'Investimento': 'Fraco',
         'Preco': 'Favoravel'}
    )
    # 6
    system.add_rule(
        {'P/VPA': 'Baixo'},
        {'Investimento': 'Avaliar',
         'Preco': 'Favoravel'}
    )
    # 7
    system.add_rule(
        {'P/VPA': 'Medio'},
        {'Investimento': 'Forte',
         'Preco': 'Avaliar'}
    )
    # 8
    system.add_rule(
        {'P/VPA': 'Alto'},
        {'Investimento': 'Forte',
         'Preco': 'Desfavoravel'}
    )
    # 9
    system.add_rule(
        {'Yield': 'Baixo'},
        {'Investimento': 'Avaliar',
         'Preco': 'Desfavoravel'}
    )
    # 10
    system.add_rule(
        {'Yield': 'Medio'},
        {'Investimento': 'Forte',
         'Preco': 'Avaliar'}
    )
    # 11
    system.add_rule(
        {'Yield': 'Alto'},
        {'Investimento': 'Fraco',
         'Preco': 'Favoravel'}
    )
    # 12
    system.add_rule(
        {'ROE': 'Negativo'},
        {'Investimento': 'Fraco'}
    )
    # 13
    system.add_rule(
        {'ROE': 'Baixo'},
        {'Investimento': 'Fraco'}
    )
    # 14
    system.add_rule(
        {'ROE': 'Medio'},
        {'Investimento': 'Avaliar'}
    )
    # 15
    system.add_rule(
        {'ROE': 'Alto'},
        {'Investimento': 'Forte'}
    )

    print(f"Ticker: {ticker}, P/L:{pl}, P/VPA: {pvp}, Dividend Yield: {div_yield}, ROE: {roe}")

    output = system.evaluate_output(
        {'P/L': pl,
        'P/VPA': pvp,
        'Yield': div_yield,
        'ROE': roe}
    )
    print(output)
    return (output['Investimento'], output['Preco'])


if __name__ == "__main__":
    plot_fuzzy()

