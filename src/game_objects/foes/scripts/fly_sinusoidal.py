from math import sin, pi


class FlySinusoidal:
    
    def __init__(self, speed, amplitude, period, x_shift, y_shift):
        self.speed = speed
        self.amplitude = amplitude
        self.period = period
        self.x_shift = x_shift
        self.y_shift = y_shift
        # y = amplitude * cos(period * x)

    def update(self):
        self.host.dx = -self.speed
        self.host.y = self.amplitude * sin(2 * pi * self.host.x / self.period - self.x_shift) + self.y_shift