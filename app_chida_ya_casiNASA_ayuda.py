import periodictable 
from mendeleev import *
import periodictable as elements
from tkinter import *


root = Tk()
root.configure(background='black')
ecomunes=["Fe","C","Al", "Ni","Cu","Ti","W","Pb","N","P","B","Mg","Va","Be","Sr","Rb","Zr","Au","Ag","Pt","Si","Te"]
valencia=[3, 4, 3, 3, 2, 4, 7, 4, 5, 5, 3, 2, 5, 2, 2, 1, 4, 3, 3, 4, 4, 6]
cstruc=["bcc","hexagonal","fcc","fcc","fcc","hexagonal","bcc","fcc","hexagonal","bcc","rhombohedral", "hexagonal","bcc","hexagonal", "fcc", "bcc","hexagonal","fcc","fcc","fcc","fcd","hexagonal"]
m1= StringVar()
m2= StringVar()
respuesta=StringVar()
respuesta.set("")
ls1 = Label(root, text="elemeto 1")
lr1 = Label(root, text="Radio")
lv1 = Label(root, text="valencia")
ld1 = Label(root, text="Estructura")
le1 = Label(root, text="Ele")
# Configuración de la raíz
def createGUI():
    imgtabla=PhotoImage(file="TablaP2.png")
    imgsimple=imgtabla.subsample(2)
    limage=Label(root,image=imgsimple)
    limage.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    label = Label(root, text="elemento 1")
    label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    m1.set("")
    entry = Entry(root,textvariable=m1)
    entry.grid(row=1, column=1, padx=5, pady=5)
    entry.config(justify="center", state="normal")
    label2 = Label(root, text="elemento 2")
    label2.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    m1.set("")
    entry2 = Entry(root,textvariable=m2)
    entry2.grid(row=2, column=1, padx=5, pady=5)
    entry2.config(justify="center", state="normal")
    registrarButton = Button(root,text="ver propiedades",command= calculo)
    registrarButton.grid(column=1,row=4,ipadx=5,ipady=5,padx=10,pady=10)
    ls1.grid(row=5, column=1, sticky="w", padx=5, pady=5)
    label3 = Label(root, text="Radio Atomico:")
    label3.grid(row=6, column=0, sticky="w", padx=5, pady=5)
    lr1.grid(row=6, column=1, sticky="w", padx=5, pady=5)
    label4 = Label(root, text="Valencia:")
    label4.grid(row=7, column=0, sticky="w", padx=5, pady=5)
    lv1.grid(row=7, column=1, sticky="w", padx=5, pady=5)
    label5 = Label(root, text="EStructura:")
    label5.grid(row=8, column=0, sticky="w", padx=5, pady=5)
    ld1.grid(row=8, column=1, sticky="w", padx=5, pady=5)
    label6 = Label(root, text="Electronagatividad:")
    label6.grid(row=9, column=0, sticky="w", padx=5, pady=5)
    le1.grid(row=9, column=1, sticky="w", padx=5, pady=5)
    root.mainloop()

def calculo():
    elemento1=element(m1.get())
    elemento2=element(m2.get())
            
    #print("El elemento 1 es:"+elemento1)
    #print("El elemento 2 es:"+elemento2)
    ls1.config(text=elemento1.name)
    ratomico1=elemento2.atomic_radius
    lr1.config(text=ratomico1)
    print("el radio atomico del "+elemento2.name+" es:")
    ratomico2=elemento2.atomic_radius
    print(ratomico2)
    valencia1=elemento1.nvalence('d')
    lv1.config(text=valencia1)
    print("la valencia del "+elemento2.name+" es:")
    valencia2=elemento2.nvalence('d')
    print(valencia2)
    estructura1=elements.Co.crystal_structure['symmetry']
    ld1.config(text=estructura1)
    print("la estructura cristalina del "+elemento2.name+" es:")
    estructura2=elements.Ni.crystal_structure['symmetry']
    print(estructura2)
    electroneg1=elemento1.electronegativity('pauling')
    le1.config(text=electroneg1)
    print(electroneg1)
    print("la electronegatividad del "+elemento2.name+" es:")
    electroneg2=elemento2.electronegativity('pauling')
    print(electroneg2)
    if (abs((ratomico1-ratomico2)/ratomico1*100)<=15):
        if (valencia1-valencia2==0):
            if (estructura1==estructura2):
                if (abs(electroneg1-electroneg2)<=0.1):
                    respuesta="Se puede"
                else: 
                    respuesta="no se puede"
            else:
                respuesta="no se puede"
        else: 
            respuesta="no se puede"
    else: 
        respuesta="no se puede"
    
    
        






createGUI()
