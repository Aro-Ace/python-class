tempf = float(input('what is the temperature in farenhight (°F): '))
tempc = (tempf - 32) * 5 / 9
tempk = (tempf - 32) * 5 / 9 + 273.15
print (f'{tempf}in celsius (°C) is {tempc:.2f} and the temperature in kelvin (°K) {tempk:.2f}')