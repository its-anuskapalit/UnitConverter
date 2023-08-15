class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'length': {
                'meter': 1.0,
                'kilometer': 0.001,
                'centimeter': 100,
                'millimeter': 1000,
                'inch': 39.3701,
                'foot': 3.28084,
                'yard': 1.09361,
                'mile': 0.000621371,
            },
            'weight': {
                'gram': 1.0,
                'kilogram': 0.001,
                'milligram': 1000,
                'ounce': 0.03527396,
                'pound': 0.00220462,
                'tonne': 1e-6,
            },
            'temperature': {
                'celsius': [('fahrenheit', lambda x: x * 9/5 + 32),
                            ('kelvin', lambda x: x + 273.15)],
                'fahrenheit': [('celsius', lambda x: (x - 32) * 5/9),
                               ('kelvin', lambda x: (x + 459.67) * 5/9)],
                'kelvin': [('celsius', lambda x: x - 273.15),
                           ('fahrenheit', lambda x: x * 9/5 - 459.67)],
            }
        }

    def convert(self, value, from_unit, to_unit, unit_type):
        if from_unit == to_unit:
            return value

        if unit_type in self.conversion_factors:
            if from_unit in self.conversion_factors[unit_type] and to_unit in self.conversion_factors[unit_type]:
                conversion_factor = self.conversion_factors[unit_type][from_unit] / self.conversion_factors[unit_type][to_unit]
                return value * conversion_factor
            else:
                return None
        else:
            return None


def main():
    converter = UnitConverter()

    print("Unit Converter")
    print("Available unit types: length, weight, temperature")

    unit_type = input("Enter unit type: ").lower()
    if unit_type not in converter.conversion_factors:
        print("Invalid unit type.")
        return

    from_unit = input(f"Enter {unit_type} unit to convert from: ").lower()
    to_unit = input(f"Enter {unit_type} unit to convert to: ").lower()
    value = float(input(f"Enter value in {from_unit}: "))

    converted_value = converter.convert(value, from_unit, to_unit, unit_type)
    if converted_value is not None:
        print(f"{value} {from_unit} is equal to {converted_value:.4f} {to_unit}")
    else:
        print("Conversion not supported for the specified units.")

if __name__ == "__main__":
    main()
