from .fuzzy_variable_input import FuzzyInputVariable
from .fuzzy_variable_output import FuzzyOutputVariable

class Key:
    def __init__(self, name, minimum, lower_quartile, mean, upper_quartile, maximum, negative=True):
        self.minimum = minimum
        self.lower_quartile = lower_quartile
        self.mean = mean
        self.upper_quartile = upper_quartile
        self.maximum = maximum
        self.zero = 0
        self.input = self._input(name, negative)

    @property
    def bottom(self):
        return self.minimum + 0.1

    @property
    def top(self):
        return self.maximum - 0.1

    @property
    def below_zero(self):
        return self.zero - 0.1

    @property
    def above_zero(self):
        return self.zero + 0.1

    def _input(self, name, negative):
        fuzzy_variable = FuzzyInputVariable(name, self.minimum, self.maximum, 1_000_000)
        if negative:
            fuzzy_variable.add_trapezoidal('Negativo', self.minimum, self.bottom, self.zero, self.above_zero)
        fuzzy_variable.add_triangular('Baixo', self.below_zero, self.zero, self.mean)
        fuzzy_variable.add_triangular('Medio', self.lower_quartile, self.mean, self.upper_quartile)
        fuzzy_variable.add_triangular('Alto', self.mean, self.top, self.maximum)
        return fuzzy_variable
