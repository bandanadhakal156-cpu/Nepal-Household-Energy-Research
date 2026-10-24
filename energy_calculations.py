LPG Energy Conversion Calculations
Nepal Household Energy Research

Demonstration of energy-conversion equations
described in the research manuscript.
"""

# Constants from the manuscript
LPG_CYLINDER_MASS = 14.2 # kg
LPG_CALORIFIC_VALUE = 47.3 # MJ/kg
LPG_STOVE_EFFICIENCY = 0.51

# Energy supplied by one full LPG cylinder
fuel_energy = LPG_CYLINDER_MASS * LPG_CALORIFIC_VALUE

# Useful cooking heat from one cylinder
useful_heat = fuel_energy * LPG_STOVE_EFFICIENCY

# Illustrative central monthly consumption
monthly_cylinders = 0.72

monthly_fuel_energy = fuel_energy * monthly_cylinders
monthly_useful_heat = useful_heat * monthly_cylinders

print("NEPAL HOUSEHOLD ENERGY RESEARCH")
print("--------------------------------")
print(f"Fuel energy per cylinder: {fuel_energy:.2f} MJ")
print(f"Useful heat per cylinder: {useful_heat:.2f} MJ")
print(f"Illustrative monthly LPG use: {monthly_cylinders:.2f} cylinders")
print(f"Monthly fuel energy: {monthly_fuel_energy:.2f} MJ")
print(f"Monthly useful heat: {monthly_useful_heat:.2f} MJ")
