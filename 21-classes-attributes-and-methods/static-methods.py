class WeatherForecast():
    def __init__(self, tempretures):
        self.tempretures = tempretures
        
    @staticmethod
    def convert_from_fahrenheit_to_celcius(fahr):
        calculation = (5/9) * (fahr - 32)
        return round(calculation, 2)
        
    def in_celcius(self):
        return [self.convert_from_fahrenheit_to_celcius(temp) for temp in self.tempretures]
        
wf = WeatherForecast([100,90,80,70,60])
print(wf.in_celcius())