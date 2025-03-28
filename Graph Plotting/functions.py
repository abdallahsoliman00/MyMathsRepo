import numpy as np

def step(x, lower=0, upper=np.inf):
    return np.array([1 if lower <= i <= upper else 0 for i in x])

def mexican_hat(x, a=0.002, b:float=0):
    coefficient = 2 / (np.sqrt(3 * a) * np.pi**0.25)
    return 0.06*coefficient * (1 - ((x - b) / a)**2) * np.exp(-((x - b)**2) / (2 * a**2))

def custom_morlet(x, f=1000, a=0.5, b=0):
    return a * np.exp(- 10000 * (x - b)**2) * np.sin(f * (x - b))

def triangle(x, m=1, shift=0):
    return np.array([m*(i-shift) + m if -1 <= i - shift <= 0 else -m*(i-shift) + m if 0 <= i - shift <= 1 else 0 for i in x])

def impulse(x, shift=0, sigma=0.01):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x-shift)**2 / (2 * sigma**2))
