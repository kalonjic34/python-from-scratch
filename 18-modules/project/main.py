import feature.subfeature.calculator
import feature.copyright

print(feature.subfeature.calculator.subtract(10,5))
print(feature.copyright.date_of_copyright)

from feature.subfeature import calculator
print(calculator.subtract(10,3))

from feature.subfeature.calculator import subtract
print(subtract(10,6))