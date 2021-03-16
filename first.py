import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from copy import deepcopy
import window
import gravitação
import mhs


def run():
    plt.style.use('dark_background')
    k= window.pegar()
    lista=list(k)



    def fazer_campo(xs, ys):
        """ esta função faz produz o campo elétrico( vetor) como vários pontos perto das cargas"""
        qtopos = {1: (float(lista[0]),float(lista[1])), -1: (float(lista[2]),float(lista[3]))}
        n = len(xs)
        Exs = [[0. for k in range(n)] for j in range(n)]
        Eys = deepcopy(Exs) #cria uma lista diferente, porém uma cópia
        for j,x in enumerate(xs):
            for k,y in enumerate(ys):
                for q,pos in qtopos.items():
                    posx, posy = pos
                    R = sqrt((x - posx)**2 + (y - posy)**2)
                    Exs[k][j] += q*(x - posx)/R**3
                    Eys[k][j] += q*(y - posy)/R**3
        return Exs, Eys
    def plotar_campo(boxl,n):


        xs = [-boxl + i*2*boxl/(n-1) for i in range(n)]
        ys = xs[:]
        Exs, Eys = fazer_campo(xs, ys)
        xs=np.array(xs); ys=np.array(ys) # O streamplot não aceita listas, somente arrays
        Exs=np.array(Exs); Eys=np.array(Eys)
        plt.streamplot(xs, ys, Exs, Eys, density=2, color='m')
        plt.scatter(float(lista[0]),float(lista[1]), s=300, color='red')
        plt.scatter(float(lista[2]),float(lista[3]), s=300, color='green')

        plt.xlabel('$x$')

        plt.ylabel('$y$')
        plt.show()

    plotar_campo(10.,400)
