import numpy as np
import matplotlib.pyplot as plt

# Generate x values (range from -10 to 10)
x = np.linspace(-10, 10, 100)  # Creates 100 points between -10 and 10

# Calculate y values (very simple example)
y = 2*x - 5

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="y = 2x - 5", color="b")

# Add labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of y = 2x - 5")

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
