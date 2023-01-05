conversion = 273
temp_in_kelvin = [275, 280, 350, 370, 400, 500, 600, 238, 648, 200]
my_temp_in_cel = [(temp - conversion) for temp in temp_in_kelvin]
print("temperature in celcius",my_temp_in_cel)