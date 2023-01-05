conversion = 273
temp_in_kelvin = [275, 280, 350, 370, 400, 500, 600, 238, 648, 200]
my_temp_in_fahr = [1.8 * (temp - conversion) + 32 for temp in temp_in_kelvin]
print("temperature in Farenheit",my_temp_in_fahr)