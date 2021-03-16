import tkinter as tk
from tkinter import ttk
import first
import gravitação
import numpy as np
import mhs
window = tk.Tk()# criando uma janela tkinter




window.geometry('950x950')

frame_a = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=10, height=300, width=400)
frame_a.pack()

frame_b= tk.Frame(master=window, height=200, width=250, pady=10, relief=tk.GROOVE, borderwidth=10)
# configurando o frambe b, onde ficará a parte de mecanica clássica
frame_b.pack()


frame_c = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=10, height=300, width=400)
frame_c.pack()



label_nome_eletrico=tk.Label(frame_a, text='CAMPO ELÉTRICO', width=20, font=("Times New Roman", 20))
# label para escrever o campo elétrico
label_nome_eletrico.grid(row=0,column=2)

ttk.Label(frame_a, text="QUANTIDADE DE CARGAS:",
          font=("Times New Roman", 12)).grid(column=2,
                                             row=19)





n = tk.StringVar()
funcoes = ttk.Combobox(frame_a, width=27,
                            textvariable=n)

# Adicionando a quantidade de cargas
funcoes['values'] = ('2 cargas',
                     '3 cargas',
                     '4 cargas',
                     '5 cargas',
                     '6 cargas'
                          )

funcoes.grid(row=20, column=2)

k = tk.StringVar()
cor = ttk.Combobox( frame_a, width=15,
                            textvariable=k)

# Adding combobox drop down list
cor['values'] = ('Amarelo',
                 'Azul',
                 'cinza',
                 'laranja',
                 'preto',
                 'vermelho','verde'
                          )


cor.grid(column=0, row=20)
label_cor2 = tk.Label(frame_a, text='Escolha a cor da carga 1',font=("Times New Roman", 12) )
label_cor2.grid(row=19, column=0)


j = tk.StringVar()
cor2 = ttk.Combobox( frame_a, width=15,
                            textvariable=j)


# adicionando a cor da carga 2
cor2['values'] = ('Amarelo',
                 'Azul',
                 'cinza',
                 'laranja',
                 'preto',
                 'vermelho',
                  'verde'
                          )
cor2.grid(column=3, row=20)



label_cor2 = tk.Label(frame_a, text='Escolha a cor da carga 2',font=("Times New Roman", 12) )
label_cor2.grid(row=19, column=3)

ord_c1 = tk.Label( frame_a, text='Ordenada da carga 1 - Y', font=('Times New Roman', 12))
ord_c1.grid(row=16, column=0)
abs_c1 = tk.Label(frame_a, text='Abscissa da carga 1 - X', font=('Times New Roman', 12))
abs_c1.grid(row=17, column=0)

entord_c1 = tk.Entry(frame_a)
entord_c1.grid(row= 16,column=1)
entabs_c1= tk.Entry(frame_a)
entabs_c1.grid(row=17,column=1)

modulo_c1 = tk.Label(frame_a, text='Módulo da carga 1 (Coulombs):', width=25, font=('Times New Roman', 12))
modulo_c1.grid(row=18, column=0)
entmod_c1= tk.Entry(frame_a)
entmod_c1.insert(0, '-1,602×10^^−19')
entmod_c1.grid(row=18, column=1)

def pegar():
    c1x= entabs_c1.get()
    c1y=entord_c1.get()

    c2x=entabs_c2.get()
    c2y=entord_c2.get()





    print(c1x)

    return c1x, c1y, c2x, c2y


#---------------------------------------------------- carga 2

ord_c2 = tk.Label( frame_a, text='ordenada da carga 2 - Y', font=('Times New Roman', 12))
ord_c2.grid(row=16, column=3, padx=55)
abs_c2 = tk.Label(frame_a, text='abscissa da carga 2 - X', font=('Times New Roman', 12))
abs_c2.grid(row=17, column=3)

entord_c2 = tk.Entry(frame_a)
entord_c2.grid(row= 16,column=4)
entabs_c2= tk.Entry(frame_a)
entabs_c2.grid(row=17,column=4)

modulo_c2 = tk.Label(frame_a, text='Módulo da carga 2 (Coulombs):', width=25, font=('Times New Roman', 12))
modulo_c2.grid(row=18, column=3)
entmod_c2= tk.Entry(frame_a)
entmod_c2.insert(0, '+1,602×10^^−19')
entmod_c2.grid(row=18, column=4, padx=20)



botao1 = tk.Button(frame_a, text='EXECUTAR CAMPO ELÉTRICO', bg='gray', fg='black', relief=tk.GROOVE,width=30, command= first.run)
botao1.grid(row=21, column=2, pady=20)

##--------------------------------------------------------- mecanica clássica ---------------------------

label_mecanica=tk.Label(frame_b,pady=10,padx=240, text='3° lei de Kepler', width=40, font=("Times New Roman", 15))
label_mecanica.pack()
sobre_mecanica = tk.Label(frame_b, text='num referencial fixo no Sol, o quadrado do período de revolução de um planeta ao'
                                        ,
                          font=("Times New Roman",15))
sobre_mecanica2 = tk.Label(frame_b, text=' redor do Sol é proporcional ao cubo do semi-eixo maior da elipse que representa a órbita do planeta.',
                          font=("Times New Roman",15))

sobre_mecanica3 = tk.Label(frame_b, text=' T ** 2 = K a**3',
                          font=("Times New Roman",15))
sobre_mecanica.pack()
sobre_mecanica2.pack()
sobre_mecanica3.pack()




botao_mecanica = tk.Button(frame_b,text='EXECUTAR', width=30 , pady=10, bg='gray', fg='black', command=gravitação.runn)
botao_mecanica.pack()




##--------------------------------------------------- MHS ---------------------------------------------------------------

label_mhs=tk.Label(frame_c, padx=240, pady=10, text='MOVIMENTO HARMÔNICO SIMPLES', width=40, font=("Times New Roman", 15))
label_mhs.pack()

sobre_mhs = tk.Label(frame_c, text='Movimento oscilatório que se repete periodicamente, quando submetido a uma força restauradora, '
                                        ,
                          font=("Times New Roman",15))
sobre_mhs1 = tk.Label(frame_c, text=' como por exemplo uma mola, ou um pendulo. Energia potencial + cinética = energia total. ',
                          font=("Times New Roman",15))

sobre_mhs2 = tk.Label(frame_c, text='A solução mais geral é : r(t) = A cos(wt + teta)',
                          font=("Times New Roman",15))
sobre_mhs.pack()
sobre_mhs1.pack()
sobre_mhs2.pack()



botao_mecanica = tk.Button(frame_c, text='EXECUTAR', width=30, pady=10, bg='gray', fg='black', command=mhs.run_mhs)
botao_mecanica.pack()


window.mainloop()
