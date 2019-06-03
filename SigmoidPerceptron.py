import numpy as np


class SigmoidPerceptron:

    def __init__(self, n):
        self.w = np.random.rand(n)
        self.b = np.random.rand()

    def predict(self, x):
        return 1 / (1 + np.exp(-sum(x * self.w) + self.b))

    def grad_w(self, x, y):
        p = self.predict(x)
        return (p - y) * p * (1 - p) * x

    def grad_b(self, x, y):
        p = self.predict(x)
        return (p - y) * p * (1 - p)

    def train(self, x, y, alpha, beta):
        p = self.predict(x)
        self.w = self.w - alpha * self.grad_w(x, y)
        self.b = self.b - beta * self.grad_b(x, y)

    def err(self, x, y):
        return 0.5 * (self.predict(x) - y) ** 2

    def teach_on_dataset(self, x, y, alpha, beta, iterations):
        n = x.shape[0]

        for j in range(0, iterations):
            square_err = 0
            for i in range(0, n):
                self.train(x[i], y[i], alpha, beta)

            for i in range(0, n):
                square_err += self.err(x[i], y[i])

            print(square_err)
