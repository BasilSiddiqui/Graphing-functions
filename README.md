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

