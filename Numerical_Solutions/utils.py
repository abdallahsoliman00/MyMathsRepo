from abc import ABC, abstractmethod
import numpy as np


class Function(ABC):
    """Abstract base class for functions"""
    def __init__(self, *params):
        self.func = self.function(*params)

    def __call__(self, x):
        return self.func(x)

    @abstractmethod
    def function(self, *params):
        """Example
        ---------
        ::
        
            def function(self, m, c):
                return lambda x: m*x + c"""
        ...


class Linear(Function):
    def function(self, m, c):
        return lambda x: m*x + c

class Quadratic(Function):
    def function(self, a, b, c):
        return lambda x: a*x**2 + b*x + c
    
class Cubic(Function):
    def function(self, a, b, c, d):
        return lambda x: a*x**3 + b*x**2 + c*x + d

class Exponential(Function):
    def function(self, a, b, k):
        return lambda x: a * (b ** (k*x))  # b is the base

class NaturalExponential(Function):
    def function(self, a, k):
        return lambda x: a * np.exp(k * x)

class Logarithmic(Function):
    def function(self, a, b):
        return lambda x: a * np.log(x) / np.log(b)  # log base b

class Sine(Function):
    def function(self, amplitude, frequency, phase):
        return lambda x: amplitude * np.sin(2 * np.pi * frequency * x + phase)

class Cosine(Function):
    def function(self, amplitude, frequency, phase):
        return lambda x: amplitude * np.cos(2 * np.pi * frequency * x + phase)

class Tangent(Function):
    def function(self, amplitude, frequency, phase):
        return lambda x: amplitude * np.tan(2 * np.pi * frequency * x + phase)

class Reciprocal(Function):
    def function(self, a):
        return lambda x: a / x

class Absolute(Function):
    def function(self, a):
        return lambda x: a * np.abs(x)

