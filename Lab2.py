import numpy as np


def f(x):
    return 2 / (1 + np.exp(-x)) - 1


def df(x):
    return 0.5 * (1 + x) * (1 - x)


def hypertang(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def dhypertang(x):
    return 1 - hypertang(x) ** 2


W1 = np.array(
    [[-0.2, 0.3, -0.4]
    , [0.1, -0.3, -0.4]]
)
W2 = np.array([0.2, 0.3])

W1h = np.array(
    [[-0.2, 0.3, -0.4]
    , [0.1, -0.3, -0.4]]
)
W2h = np.array([0.2, 0.3])

def go_forward_hyper(inp):
    sum = np.dot(W1h, inp)
    out = np.array([hypertang(x) for x in sum])
    sum = np.dot(W2h, out)
    y = hypertang(sum)
    return y, out


def go_forward(inp):
    sum = np.dot(W1, inp)
    out = np.array([f(x) for x in sum])
    sum = np.dot(W2, out)
    y = f(sum)
    return y, out


def train_with_hyper(epoch):
    global W2h, W1h
    lmd = 0.01  # шаг обучения
    N = 10000  # число итераций при обучении
    count = len(epoch)
    for k in range(N):
        x = epoch[np.random.randint(0, count)]  # случайных выбор входного сигнала из обучающей выборки
        y, out = go_forward_hyper(x[0:3])  # прямой проход по НС и вычисление выходных значений нейронов
        e = y - x[-1]  # ошибка
        delta = e * dhypertang(y)  # локальный градиент
        W2h[0] = W2h[0] - lmd * delta * out[0]  # корректировка веса первой связи
        W2h[1] = W2h[1] - lmd * delta * out[1]  # корректировка веса второй связи
        delta2 = W2h * delta * dhypertang(out)  # вектор из 2-х величин локальных градиентов
        # корректировка связей первого слоя
        W1h[0, :] = W1h[0, :] - np.array(x[0:3]) * delta2[0] * lmd
        W1h[1, :] = W1h[1, :] - np.array(x[0:3]) * delta2[1] * lmd  # обучающая выборка (она же полная выборка)


def train(epoch):
    global W2, W1
    lmd = 0.01  # шаг обучения
    N = 10000  # число итераций при обучении
    count = len(epoch)
    for k in range(N):
        x = epoch[np.random.randint(0, count)]  # случайных выбор входного сигнала из обучающей выборки
        y, out = go_forward(x[0:3])  # прямой проход по НС и вычисление выходных значений нейронов
        e = y - x[-1]  # ошибка
        delta = e * df(y)  # локальный градиент
        W2[0] = W2[0] - lmd * delta * out[0]  # корректировка веса первой связи
        W2[1] = W2[1] - lmd * delta * out[1]  # корректировка веса второй связи
        delta2 = W2 * delta * df(out)  # вектор из 2-х величин локальных градиентов
        # корректировка связей первого слоя
        W1[0, :] = W1[0, :] - np.array(x[0:3]) * delta2[0] * lmd
        W1[1, :] = W1[1, :] - np.array(x[0:3]) * delta2[1] * lmd  # обучающая выборка (она же полная выборка)



epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)]

train_with_hyper(epoch)  # запуск обучения сети

# проверка полученных результатов
print("Веса первого слоя:\n", W1h)
print("Веса второго слоя:\n", W2h)

mse = 0
for x in epoch:
    y, out = go_forward_hyper(x[0:3])
    print(f"Выходное значение НС: {y} => {x[-1]}")
    mse += (y - x[-1]) ** 2

print(f"mse = {mse}\n")

train(epoch)  # запуск обучения сети

# проверка полученных результатов
print("Веса первого слоя:\n", W1)
print("Веса второго слоя:\n", W2)

mse = 0
for x in epoch:
    y, out = go_forward(x[0:3])
    print(f"Выходное значение НС: {y} => {x[-1]}")
    mse += (y - x[-1]) ** 2

print(f"mse = {mse}\n")