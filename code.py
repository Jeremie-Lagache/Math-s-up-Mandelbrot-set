import matplotlib.pyplot as plt
import numpy as np

def suite(c, n):
    z = c
    values = [z]
    for i in range(n):
        z = z**2 + c
        values.append(z)
    return values

def next(z, c):
    return z**2 + c

def mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    mandelbrot_set = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 1000
        Z[mask] = next(Z[mask], X[mask] + 1j * Y[mask])
        mandelbrot_set += mask.astype(int)

    return mandelbrot_set

def plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    mandelbrot_set = mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
    plt.imshow(np.log(mandelbrot_set), cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.show()
    
plot_mandelbrot(800, 800, -2, 2, -2, 2, 100)

    

