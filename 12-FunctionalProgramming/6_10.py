import matplotlib.pyplot as plt

# Temperature data
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Extract city names and temperature values
cities = list(temperatures.keys())
temps = list(temperatures.values())

# Create a bar chart
plt.bar(cities, temps, color='skyblue')

# Add title and axis labels
plt.title("Recorded Temperatures in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# Show the chart
plt.show()
