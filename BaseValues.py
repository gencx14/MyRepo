import cmath
class BaseValues:
    def __init__(self, Pbase, Vbase):
        self.Pbase = Pbase
        self.Vbase = Vbase
        self.Zbase = Vbase**2/Pbase
