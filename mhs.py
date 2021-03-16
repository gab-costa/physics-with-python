import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.animation import FuncAnimation as anim
pause = True
n = 0
def run_mhs():



    class dp_mola:

        def __init__(self, mu=.5, k=2):
            self.mu = mu
            self.k = k
            self.w2 = k / mu
            self.tau = 2 * np.pi / np.sqrt(self.w2)

        def EDO(self, Y, t):
            x, y, xp, yp = Y
            dx = xp
            dy = yp
            dxp = -self.w2 * x
            dyp = -self.w2 * y
            return dx, dy, dxp, dyp

        def set_CI(self, x0=1., y0=0, v0x=0, v0y=1):
            self.Y0 = [x0, y0, v0x, v0y]
            self.L = self.mu * (x0 * v0y - y0 * v0x)

        def solve(self, tmax=None, N=1000):
            if tmax is None:
                tmax = self.tau
            self.t = np.linspace(0, tmax, N)

            self.Y = spi.odeint(self.EDO, self.Y0, self.t)
            self.x, self.y, self.vx, self.vy = self.Y.T

            self.r2 = self.x**2 + self.y**2
            self.v2 = self.vx**2 + self.vy**2
            self.r = np.sqrt(self.r2)
            self.v = np.sqrt(self.v2)
            self.th = np.fmod(np.arctan2(self.y, self.x), 2*np.pi)
            self.th[self.th < 0] = self.th[self.th < 0] + 2 * np.pi
            self.thp = self.L / self.mu / self.r2
            self.rp = np.sqrt(self.v2 - (self.r * self.thp)**2)

            self.Energia()

        def Energia(self):
            self.T = .5 * self.mu * self.v2
            self.V = .5 * self.k * self.r2
            self.E = self.T + self.V
            self.Vcf = .5 * self.L**2 / self.mu / self.r2
            self.Veq = self.V + self.Vcf

        def Energia_graficos(self, N=200, rmin=.3, rmax=1.6):
            r = np.linspace(rmin, rmax, N)
            V = .5 * self.k * r**2
            Vcf = .5 * (self.L / r)**2 / self.mu
            Veq = V + Vcf
            return r, V, Vcf, Veq


    s = dp_mola()
    s.set_CI()
    s.solve()

    # gráficos
    style.use('dark_background')
    fig = plt.figure(figsize=(10, 6))
    gs = fig.add_gridspec(2, 1)

    ax2 = fig.add_subplot(gs[0, 0])
    ax2.set_xlabel('$r$')
    ax2.set_ylabel('Energias')
    r, V, Vcf, Veq = s.Energia_graficos()
    ax2.plot(r, V, '--', label='V')
    ax2.plot(r, Vcf, '--', label='Vcf')
    ax2.plot(r, Veq, 'b', label='Veq')
    Teq, = ax2.plot([s.r[0], s.r[0]], [s.Veq[0], s.E[0]], 'b-',
                    marker='o', markerfacecolor='red', label='Teq')
    ax2.plot(s.r, s.E, label='E')
    V, = ax2.plot(s.r[0], s.V[0], 'ro')
    Vcf, = ax2.plot(s.r[0], s.Vcf[0], 'ro')
    plt.legend()

    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_xlabel('$t$')
    ax3.set_ylabel('$r$')
    ax3.plot(s.t, s.r, 'b--')
    rplot, = ax3.plot(s.t[0], s.r[0], 'ro')


    def updatefig(i):
        global n
        if not pause:

            Teq.set_data([s.r[n], s.r[n]], [s.Veq[n], s.E[n]])
            V.set_data(s.r[n], s.V[n])
            Vcf.set_data(s.r[n], s.Vcf[n])
            rplot.set_data(s.t[n], s.r[n])

            n = n + 1 if n < s.t.size - 1 else 0
        return Teq, Vcf, V, rplot


    def onClick(event):
        global pause
        pause ^= True




    fig.canvas.mpl_connect('button_press_event', onClick)
    a = anim(fig, updatefig, frames=s.t.size, interval=1, blit=True)

    fig.tight_layout()

    plt.show()