from tkinter import *
from tkinter import ttk, font,messagebox
class Aplicacion():
    __ventana=None
    __peso=None
    __altura=None
    __mensaje1=None
    __mensaje2=None
    __mensaje1Label=None
    __mensaje2Label=None
    __entrada1=None
    __entrada2=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0,0)
        fuente = font.Font(weight='bold') 
        fuente2=font.Font(weight='bold',size=16)
        self.__peso =DoubleVar()
        self.__altura =DoubleVar()
        self.__mensaje1=StringVar()
        self.__mensaje2=StringVar()
        contenedor = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10,10)).grid(column=0,row=0)
        alturaLabel=ttk.Label(contenedor, text="Altura:",font=fuente, padding=(5,5)).grid(column=0, row=0)
        pesoLabel=ttk.Label(contenedor, text="Peso:",font=fuente, padding=(5,5)).grid(column=0, row=1)
        self.__mensaje1Label = ttk.Label(contenedor, textvariable=self.__mensaje1,font=fuente, foreground='green',anchor='center')
        self.__mensaje1Label.grid(column=1, row=5, sticky='EW',columnspan=3)
        self.__mensaje2Label = ttk.Label(contenedor, textvariable=self.__mensaje2,font=fuente2, foreground='green',anchor='center')
        self.__mensaje2Label.grid(column=1, row=6, sticky='EW',columnspan=3)
        self.__entrada1=ttk.Entry(contenedor, textvariable=self.__peso)
        self.__entrada1.grid(column=1, row=0, columnspan=3,sticky='EW')
        cmLabel=ttk.Label(contenedor, text="cm", borderwidth=1, relief="solid",padding=(3,3)).grid(padx=5,column=4, row=0, sticky='EW')
        kgLabel=ttk.Label(contenedor, text="kg", borderwidth=1, relief="solid",padding=(3,3)).grid(padx=5,column=4, row=1, sticky='EW')
        self.__entrada2=ttk.Entry(contenedor, textvariable=self.__altura)
        self.__entrada2.grid(column=1, row=1, columnspan=3,sticky='EW')
        separador1=ttk.Separator(contenedor, orient=HORIZONTAL).grid(column=0, row=3, columnspan=3)
        boton1=ttk.Button(contenedor,text="Calcular",padding=(5,5), command=self.calcular,width=15).grid(padx=5,pady=5,column=1, row=4,sticky='EW')
        boton2=ttk.Button(contenedor, text="Limpar",padding=(5,5), command=self.limpiar,width=15).grid(padx=5,pady=5,column=3, row=4,sticky='EW')
        self.__peso.set('')
        self.__altura.set('')
        self.__mensaje1.set('')
        self.__mensaje2.set('')
        self.__entrada1.focus()
        self.__ventana.mainloop()
    def calcular(self):
        try:
            valorAltura=float(self.__entrada1.get())
            valorPeso=float(self.__entrada2.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico y se permite .')
            self.__peso.set('')
            self.__altura.set('')
            self.__entrada1.focus()
        else:
            metros=valorAltura/100
            resultado=valorPeso/(metros*metros)
            self.__mensaje1.set('Tu indice de masa corporal es {} kg/m2'.format(round(resultado,2)))
            if resultado <18.5:
                self.__mensaje1Label.configure(foreground='#ffc107')
                self.__mensaje2Label.configure(foreground='#ffc107')
                self.__mensaje2.set('Peso inferior al normal')
            elif resultado >=18.5 and resultado< 25:
                self.__mensaje1Label.configure(foreground='green')
                self.__mensaje2Label.configure(foreground='green')
                self.__mensaje2.set('Peso normal')
            elif resultado>= 25.0 and resultado< 30:
                self.__mensaje1Label.configure(foreground='#ffc107')
                self.__mensaje2Label.configure(foreground='#ffc107')
                self.__mensaje2.set('Peso superior al normal')
            else:
                self.__mensaje1Label.configure(foreground='red')
                self.__mensaje2Label.configure(foreground='red')
                self.__mensaje2.set('Obesidad')            
    def limpiar(self):
        self.__mensaje2.set('')
        self.__peso.set('')
        self.__altura.set('')
        self.__mensaje1.set('')