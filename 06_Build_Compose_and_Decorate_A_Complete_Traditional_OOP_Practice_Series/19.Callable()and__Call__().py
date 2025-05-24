class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiplier(5)
print(callable(m))  # True
print(m(10))        # 50
