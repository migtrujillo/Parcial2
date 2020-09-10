class cola(object):
    def __init__(self):
        self.items=[]

    def encolar (self,x):
        self.items.append(x)

    def vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def desencolar(self):
        if self.vacia():
            return None
        else:
            return self.items.pop(0)
def registro():
    c =cola()
    print(" ---------------------------------- ")
    while True:
        x=0
        print("""
        1. Para añadir empleado
        2. Saber la cantidad de empleados que hay
        3. Para pagarle al empleado
        4. salir""")
        x= input("Seleccione una opcion ")
        x=int(x)
        if x==1:
            Trabajador=input("Digite el nombre del empleado: ")
            c.encolar(Trabajador)
            identifi=int(input("Digite Identificacion del empleado: "))
            htrabajadas = int(input("Digite las horas laboradas: "))
            sueldo = int(input("Digite el sueldo por horas: "))
            st=htrabajadas*sueldo
        elif x==2:
            print("La cantidad de empleados que hay son :")
            print(len(c.items))
        elif x==3:
            print("    Registro     ")
            print("El Empleado:",Trabajador,"\n tiene un sueldo de :",st)
        elif x==4:
            break
        else: 
            print("Opcion no valida")
registro()
