class ScaleConverter:
    def  __init__(self, units_form, units_to, factor):
        self.units_form = units_form
        self.units_to = units_to
        self.factor = factor

    def description(self):
        return  'Convert '+ self.units_form+' to '+self.units_to

    def convert(self, value):
        return value*self.factor