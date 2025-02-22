def temp_covenverter(): #create function to convert temperature
    convert_from = input("What scale are you converting from? (C,F,K) ")
    convert_to = input("\nWhat scale are you converting to? (C,F,K) ")
   
    celsius = 0
    fahrenheit = 0
    kelvin = 0

    c_to_f = celsius*2 + 30
    c_to_k = celsius + 273.15
    f_to_c = fahrenheit - 30 / 2
    f_to_k = ((fahrenheit - 32) /1.8) + 273.15
    k_to_c = kelvin - 273.15
    k_to_f = ((kelvin - 273.15)*1.8) + 32

    if convert_from.lower() == "c" and convert_to.lower() == "f":
        celsius = int(input("Enter your temperature in Celsius: "))
        print(f"{celsius}°Celsius is {c_to_f}°Fahrenheit")
    elif convert_from.lower() == "c" and convert_to.lower() == "k":
        celsius = int(input("Enter your temperature in Celsius: "))    
        print(f"{celsius}°Celsius is {c_to_k}°Kelvin")
    elif convert_from.lower() == "f" and convert_to.lower() == "c":
        fahrenheit = int(input("Enter your temperature in Fahrenheit: "))
        print(f"{fahrenheit}°Fahrenheit is {f_to_c}°Celsius")
    elif convert_from.lower() == "f" and convert_to.lower() == "k":
        fahrenheit = int(input("Enter your temperature in Fahrenheit: "))
        print(f"{fahrenheit}°Fahrenheit is {f_to_k}°Kelvin")
    elif convert_from.lower() == "k" and convert_to.lower() == "c":
        kelvin = int(input("Enter your temperature in Kelvin: "))
        print(f"{kelvin}°Kelvin is {k_to_c}°Celsius")
    elif convert_from.lower() == "c" and convert_to.lower() == "f":
        kelvin = int(input("Enter your temperature in Kelvin: "))
        print(f"{kelvin}°Kelvin is {k_to_f}°Fahrenheit")
    else:
        print("Please enter a correct letter of temperature!")
    
temp_covenverter()