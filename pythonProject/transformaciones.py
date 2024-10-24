import numpy as np
import matplotlib.pyplot as plt


def retorno_rango(img):
    max = img.max()
    min = img.min()
    k = 255
    _img = k * (img - min) / (max - min)
    return (k * (img - min)) / (max - min)


def transformacion_log(c, r):
    ones = np.ones(r.shape)
    temp = c * np.log(ones + r)
    return retorno_rango(temp)


def negativo(r):
    transformada = 255 - r
    return transformada


def transformacion_gamma(r, c, gamma):
    transformada = c * (r ** gamma)
    return retorno_rango(transformada)


def rebanada_de_bit(r, bit):
    transformada = r & (1 << bit)
    return transformada


def estiramiento_contraste(r, r1, s1, r2, s2):
    r1Matrix = np.ones(r.shape) * r1
    dif_r = r2 - r1
    dif_r_Mat = np.ones(r.shape) * dif_r
    transformada = (r - r1Matrix) / dif_r_Mat
    print(transformada.min(), transformada.max())
    return retorno_rango(transformada)


def rebanada_de_intensidad(r, a, b, tono_objetivo=255, tono_fondo=0, version=1):
    transformada = np.zeros(r.shape)
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if a <= r[i, j] <= b:
                transformada[i, j] = tono_objetivo
            else:
                if version == 1:
                    transformada[i, j] = r[i, j]
                else:
                    transformada[i, j] = tono_fondo
    return transformada


def cv2_imshow(img, title=''):
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    plt.show()


def mostrar_histograma(img, title=''):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title(title)
    plt.show()