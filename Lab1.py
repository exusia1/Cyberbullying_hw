import numpy as np

def activisation(x):
    return 1 if x >= 0.5 else 0


# пишу нейросеть которая решает буду ли я смотреть видос на ютубе
def decider(length, subscribed, games_tag):
    x = np.array([length, subscribed, games_tag])
    w11 = np.array([-0.3, 0.5, 0])
    w12 = np.array([-0.1, 0.5, 0.3])
    w13 = np.array([0.3, 0.2, 0.4])
    #  первый слой я составил более-менее осознанно
    #  второй почти рандомно, чтобы показать что понимаю как работает вычиление значений
    w21 = np.array([0.3, 0.2, 0.3])
    w22 = np.array([0.8, 0.1, 0])
    w23 = np.array([0.3, 0, 0.4])
    weight1 = np.array([w11, w12, w13])
    weight2 = np.array([w21, w22, w23])
    weight3 = np.array([0.4, 0.6, 0.3])

    sum_hidden1 = np.dot(weight1, x)  # вычисляем сумму на входах нейронов скрытого слоя
    print(f"Значения сумм на нейронах 1 скрытого слоя: {sum_hidden1}")

    out_hidden1 = np.array([activisation(x) for x in sum_hidden1])
    print(f"Значения на выходах нейронов 1 скрытого слоя: {out_hidden1}")

    sum_hidden2 = np.dot(weight2, out_hidden1)  # вычисляем сумму на входах нейронов скрытого слоя
    print(f"Значения сумм на нейронах 2 скрытого слоя: {sum_hidden2}")

    out_hidden2 = np.array([activisation(x) for x in sum_hidden2])
    print(f"Значения на выходах нейронов 2 скрытого слоя: {out_hidden2}")

    result = np.dot(weight3, out_hidden2)
    y = activisation(result)
    print(f"Результат: {y}")
    return y


# микробонус: эмулируем мой мозг на ютубе
def emulation():
    watched = 0
    consecutive_skips = 0
    while watched < 2 and consecutive_skips < 3:
        l = 1 if int(input("Введите длительность видео в минутах:")) >= 15 else 0
        s = int(input("Введите 1, если я подписан на автора видео:"))
        g = int(input("Введите 1, если ролик связан с видеоиграми:"))

        res = decider(l, s, g)
        if res:
            watched += 1
            consecutive_skips = 0
            print("Смотрю видос")
        else:
            consecutive_skips += 1
            print("Не то, смотрим, что дальше")

    if consecutive_skips:
        print("На ютубе контента нет, Alt+F4")
    else:
        print("Надоело смотреть видосы, Alt+F4")


emulation()
