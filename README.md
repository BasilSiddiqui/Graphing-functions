# Function Plotter

This Python script allows you to visualize **any mathematical function** using Matplotlib. It supports **customizable x-range, colors, and titles**, making it versatile for plotting different types of functions, including **linear, quadratic, exponential, and trigonometric functions**.

## Features
✅ Plot **any mathematical function** using lambda expressions
✅ Set a **custom x-range**
✅ Choose a **color** for the function line
✅ Add a **custom title** to the plot
✅ Includes **axis lines, grid styling, and a legend** for better visualization

## Installation
Make sure you have Python installed along with the following dependencies:
```sh
pip install numpy matplotlib
```

## Usage
Import the function and call `plot_function()` with your desired parameters:

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, x_range=(-10, 10), num_points=100, title="Function Plot", color="b"):
    """
    Plots any given mathematical function.

    Parameters:
    - func: A Python function (e.g., lambda x: x**2)
    - x_range: Tuple specifying the range of x values (default: -10 to 10)
    - num_points: Number of points to generate (default: 100)
    - title: Custom title for the plot
    - color: Color of the plot line (default: 'b' for blue)
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=title, color=color, linewidth=2)

    # Add axis lines
    plt.axhline(0, color="black", linewidth=1, linestyle="--", alpha=0.7)
    plt.axvline(0, color="black", linewidth=1, linestyle="--", alpha=0.7)

    # Add labels and title
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title(title)

    # Improve grid style
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Add a legend
    plt.legend()

    plt.show()
```

## Examples

### Plot a Linear Function:
```python
plot_function(lambda x: 2*x - 5, x_range=(-20, 20), color="red", title="y = 2x - 5")
```

### Plot a Quadratic Function:
```python
plot_function(lambda x: x**2, x_range=(-5, 5), color="green", title="y = x^2")
```

### Plot a Sine Wave:
```python
plot_function(lambda x: np.sin(x), x_range=(-2*np.pi, 2*np.pi), color="purple", title="y = sin(x)")
```

### Plot an Exponential Function:
```python
plot_function(lambda x: np.exp(x), x_range=(-2, 2), color="orange", title="y = e^x")
```

## License
This project is open-source and free to use. Feel free to modify and improve it!

---
🚀 **Now you can visualize any mathematical function dynamically!** 🎨

