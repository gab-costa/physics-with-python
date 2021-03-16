import numpy as np
import scipy.integrate as spi


class CalcEnergia:

    def Energia(self):

        self.thp = self.thetap(self.r)
        self.v = np.sqrt(self.rp**2 + (self.r * self.thp)**2)
        self.Tef = .5 * self.mu * self.rp**2
        self.V = - self.gamma / self.r
        self.Vcf = .5 * self.L**2 / self.mu / self.r**2
        self.Vef = self.V + self.Vcf
        self.E = self.Tef + self.Vef

    def Energia_graficos(self, N=200, rmin=.4, rmax=10):
        r = np.linspace(rmin, rmax, N)
        V = -self.GM * self.mu / r
        Vcf = .5 * (self.L / r)**2 / self.mu
        Vef = V + Vcf
        return r, V, Vcf, Vef

    def thetap(self, r):
        thp = self.L / (self.mu * r**2)
        return thp


class Kepler(CalcEnergia):
    ''' Sistema Sol-Terra
            unidades: m: massa da Terra
                      t: ano terrestre
                      r: raio da órbita da Terra
                      th: radianos
            otimizado para órbitas elípticas
    '''

    def __init__(self, mu=1., r0=1., v0=2*np.pi, GM=39.6):
        # input
        self.GM = GM
        self.mu = mu
        self.r0 = r0
        self.v0 = v0
        # grandezas relevantes
        self.gamma = GM * mu
        self.L = mu * r0 * v0
        self.E = .5 * mu * v0**2 - self.gamma / r0
        self.exc = np.sqrt(1 + 2 * self.L**2 * self.E / (self.gamma**2 * mu))
        self.c = self.L**2 / (self.gamma * mu)

        if self.exc < 1:
            basq = (1 - self.exc**2)
            self.a = self.c / basq
            self.b = self.c / np.sqrt(basq)
            self.tau = 2 * np.pi * np.sqrt(self.a**3 * mu / self.gamma)

    def rorbita(self, theta):
        return self.c / (1. + self.exc * np.cos(theta))

    def solve(self, N=1000, tmax=20., TOL=1.e-10):

        def EDOthetap(theta, t):
            return self.L / self.mu / self.rorbita(theta)**2

        if self.exc < 1:
            tmax = self.tau
        self.t = np.linspace(0, tmax, N+1)
        self.th = spi.odeint(EDOthetap, 0., self.t, rtol=TOL)
        self.th = np.fmod(self.th, 2*np.pi)
        self.r = self.rorbita(self.th)
        self.rp = self.exc * self.L / self.mu / self.c * np.sin(self.th)
        self.Energia()


class Kepler_num(CalcEnergia):
    ''' Sistema Sol-Terra
        unidades: m: massa da Terra
                  t: ano terrestre
                  r: raio da órbita da Terra
                  th: radianos
    '''
    def __init__(self, mu=1, GM=39.6):
        self.GM = GM
        self.mu = mu
        self.gamma = GM * mu

    def kepler(self, Y, t):
        r, th, vr, vth = Y
        dr = vr
        dth = vth
        dvr = r * vth**2 - self.GM / r**2
        dvth = -2. * vr * vth / r
        return [dr, dth, dvr, dvth]

    def set_CI(self, r0=1., th0=np.pi/2, vr0=5., vth0=2*np.pi):
        self.L = self.mu * r0 * r0 * vth0
        self.Y0 = [r0, th0, vr0, vth0]

    def solve(self, tmax=25, N=200, TOL=1.e-10):
        self.t = np.linspace(0, tmax, N+1)
        Y = spi.odeint(self.kepler, self.Y0, self.t, rtol=TOL)
        self.r, self.th, self.rp, self.thp = Y.T
        self.x = self.r * np.cos(self.th)
        self.y = self.r * np.sin(self.th)
        self.Energia()
