from secrets import randbelow
import numpy as np
from sklearn.model_selection import learning_curve


def gradient_descent(x, y):
    m_current = b_current = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.01
    for i in range(iterations):
        y_preditcion = m_current * x + b_current
        cost = (1/n) * sum([val**2 for val in (y-y_preditcion)])
        md = -(2/n) * sum(x * (y-y_preditcion))
        bd = -(2/n) * sum(y - y_preditcion)
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print('m {}, b {}, cost {}'.format(m_current, b_current, cost))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 6, 5, 6])

gradient_descent(x, y)
