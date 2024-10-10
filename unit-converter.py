def length_conversion(value, from_unit, to_unit):
    if from_unit == "meter" and to_unit == "inch":
        return value * 39.3701
    elif from_unit == "inch" and to_unit == "meter":
        return value / 39.3701
    else:
        return value  # No conversion needed

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    else:
        return value  # No conversion needed

def weight_conversion(value, from_unit, to_unit):
    if from_unit == "kilogram" and to_unit == "pound":
        return value * 2.20462
    elif from_unit == "pound" and to_unit == "kilogram":
        return value / 2.20462
    else:
        return value  # No conversion needed

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length Conversion")
        print("2. Temperature Conversion")
        print("3. Weight Conversion")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == '1':
            print("\nLength Conversion")
            print("1. Meter to Inch")
            print("2. Inch to Meter")
            unit_choice = input("Enter your choice (1-2): ")
            value = float(input("Enter the value to convert: "))
            
            if unit_choice == '1':
                result = length_conversion(value, "meter", "inch")
                print(f"{value} meters is equal to {result:.2f} inches")
            elif unit_choice == '2':
                result = length_conversion(value, "inch", "meter")
                print(f"{value} inches is equal to {result:.2f} meters")
            else:
                print("Invalid choice.")
        
        elif choice == '2':
            print("\nTemperature Conversion")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            unit_choice = input("Enter your choice (1-2): ")
            value = float(input("Enter the value to convert: "))
            
            if unit_choice == '1':
                result = temperature_conversion(value, "celsius", "fahrenheit")
                print(f"{value}°C is equal to {result:.2f}°F")
            elif unit_choice == '2':
                result = temperature_conversion(value, "fahrenheit", "celsius")
                print(f"{value}°F is equal to {result:.2f}°C")
            else:
                print("Invalid choice.")
        
        elif choice == '3':
            print("\nWeight Conversion")
            print("1. Kilogram to Pound")
            print("2. Pound to Kilogram")
            unit_choice = input("Enter your choice (1-2): ")
            value = float(input("Enter the value to convert: "))
            
            if unit_choice == '1':
                result = weight_conversion(value, "kilogram", "pound")
                print(f"{value} kilograms is equal to {result:.2f} pounds")
            elif unit_choice == '2':
                result = weight_conversion(value, "pound", "kilogram")
                print(f"{value} pounds is equal to {result:.2f} kilograms")
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
