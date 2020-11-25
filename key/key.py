

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
