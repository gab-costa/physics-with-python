import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim
from matplotlib import style

from kepler import Kepler

# Definição e solução
pause = True
n = 0
def runn():
    p = Kepler(v0=8.5)
    p.solve(N=200)

    # Gráficos
    plt.style.use('dark_background')


    fig = plt.figure(figsize=(14, 8))

    gs = fig.add_gridspec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0], polar=True)
    ax1.plot(p.th, p.r,'g--', 'origem')
    plt.scatter(820,2.3, s=350, color='yellow')
    ptraj, = ax1.plot([p.th[0]], [p.r[0]], 'ro')

    ## ax2 eh mais importante

    ax2 = fig.add_subplot(gs[0, 1], polar=False)
    r, V, Vcf, Vef = p.Energia_graficos(rmin=.2, rmax=p.r.max()+8)
    ax2.axvline(0, color='purple')
    ax2.axhline(0, color='purple')
    ax2.set_xlabel('$r$ (ua)')
    ax2.set_ylabel('Energias')
    ax2.set_ylim(-40, 40)
    ax2.plot(r, V, 'g--', label=f'$V(r)$')
    ax2.plot(r, Vcf, 'y--', label=f'$V_{{cf}}(r)$')
    ax2.plot(r, Vef, 'b', label=f'$V_{{ef}}(r)$')
    T, = ax2.plot([], [], 'k-', label=f'$T_{{ef}}(\\dot r)$')
    ax2.plot(p.r, p.E, label=f'$E$')
    E, = ax2.plot(p.r[0], p.E[0], 'ro', markersize=3)
    V, = ax2.plot(p.r[0], p.V[0], 'ro', markersize=3)
    Vef, = ax2.plot(p.r[0], p.Vef[0], 'ro', markersize=3)
    Vcf, = ax2.plot(p.r[0], p.Vcf[0], 'ro', markersize=3)
    tempo = ax2.text(.65, .02, 't = 0', transform=ax2.transAxes)
    plt.legend(loc='upper right')


    def updatefig(i):
        global n, pause
        if not pause:
            ptraj.set_data([p.th[n]], [p.r[n]])
            T.set_data([p.r[n], p.r[n]], [p.E[n], p.Vef[n]])
            V.set_data(p.r[n], p.V[n])
            Vcf.set_data(p.r[n], p.Vcf[n])
            Vef.set_data(p.r[n], p.Vef[n])
            E.set_data(p.r[n], p.E[n])
            tempo.set_text(f't={p.t[n]:.2f} anos')
            #rt.set_data([p.t[n]], [p.r[n]])
            #tht.set_data([p.t[n]], [p.th[n]])
            #rp.set_data([p.t[n]], [p.rp[n]])
            #thp.set_data([p.t[n]], [p.thp[n]])
            n = n+1 if n < p.t.size - 1 else 0
        return ptraj,  tempo, Vef, Vcf, V, E, T


    def onClick(event):
        global pause
        pause ^= True



    fig.canvas.mpl_connect('button_press_event', onClick)
    n = 0
    a = anim(fig, updatefig, frames=p.t.size, interval=2, blit=True)

    fig.tight_layout()

    plt.show()