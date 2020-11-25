from 

class Key:
    def __init__(self, minimum, lower_quartile, mean, upper_quartile, maximum):
        self.minimum = minimum
        self.lower_quartile = lower_quartile
        self.mean = mean
        self.upper_quartile = upper_quartile
        self.maximum = maximum
        self.zero = 0

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

    def input(self):
        input = FuzzyInputVariable('P/L', self.minimum, self.maximum, 1_000_000)
        input.add_trapezoidal('Negativo', self.minimum, self.bottom, self.zero, self.above_zero)
        input.add_triangular('Baixo', self.below_zero, self.zero, self.mean)
        input.add_triangular('Medio', self.lower_quartile, self.mean, self.upper_quartile)
        input.add_triangular('Alto', self.mean, self.top, self.maximum)