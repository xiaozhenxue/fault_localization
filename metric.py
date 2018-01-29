
class Metric:

    def __init__(self, cp, cf, np, nf):
        self.cp = cp
        self.cf = cf
        self.np = np
        self.nf = nf

    def odds_ratio(self):
        return ((self.cf + 0.01) * (self.np + 0.01)) / ((self.cp + 0.01) * (self.nf + 0.01))
